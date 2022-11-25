# python reverse_ollvm.py -f input.exe -s 400000 -o out.exe
from collections import defaultdict
import angr
from angr.state_plugins.inspect import BP_BEFORE
from angrmanagement.utils.graph import to_supergraph
import argparse
import sys
import claripy
import logging
import pyvex
from keystone import *
logging.getLogger('angr.storage.memory_mixins.default_filler_mixin').setLevel(logging.ERROR)


def get_cfg():
    cfg = proj.analyses.CFGFast(normalize=True, force_complete_scan=False)
    function_cfg = cfg.functions.get(start).transition_graph
    super_cfg = to_supergraph(function_cfg)
    return super_cfg

def analyse_blocks():
    retn_nodes = []
    for node in cfg.nodes:
        if cfg.in_degree(node) == 0:
            prologue_node = node
        elif cfg.out_degree(node) == 0:
            retn_nodes.append(node)
    main_dispatcher_node = list(cfg.successors(prologue_node))[0]
    for node in cfg.predecessors(main_dispatcher_node):
        if node.addr != prologue_node.addr:
            predispatcher_node = node
            break
    relevant_nodes = [prologue_node]
    sub_dispatcher_nodes = []
    for node in cfg.nodes:
        if node in cfg.predecessors(predispatcher_node):
            relevant_nodes.append(node)
        elif node != prologue_node and node not in retn_nodes:
            sub_dispatcher_nodes.append(node)
    return prologue_node, main_dispatcher_node, sub_dispatcher_nodes, retn_nodes, relevant_nodes, predispatcher_node

def preprocess(block_addr):
    def nop_proc(state):
        pass
    block = proj.factory.block(block_addr)
    has_branch = False
    for insn in block.capstone.insns:
        if insn.mnemonic == 'call':
            proj.hook(insn.address, hook=nop_proc, length=5)
            print('Hook [%s\t%s] at %#x' % (insn.mnemonic, insn.op_str, insn.address))
        elif insn.mnemonic.startswith('cmov'):
            has_branch = True
            patch_addrs[block_addr] = insn.address
            cmov_types[block_addr] = insn.mnemonic
    return has_branch

def symbolic_execute(block_addr, modify_cond=None):
    def modify_ITE_cond(state):
        expressions = list(state.scratch.irsb.statements[state.inspect.statement].expressions)
        if len(expressions) != 0 and isinstance(expressions[0], pyvex.expr.ITE):
            state.scratch.temps[expressions[0].cond.tmp] = modify_cond
            state.inspect._breakpoints['statement'] = []

    state = proj.factory.blank_state(addr=block_addr, remove_options={
                                        angr.sim_options.LAZY_SOLVES})
    if modify_cond is not None:
        state.inspect.b('statement',when=BP_BEFORE, action=modify_ITE_cond)
    simgr = proj.factory.simgr(state)
    simgr.step()
    while len(simgr.active):
        for active in simgr.active:
            if active.addr in relevant_addrs:
                flow[block_addr].append(active.addr)
                return
        simgr.step()
    print('Error at block %#x' % block_addr)

def fill_nops(addr, size):
    offset = addr - base_addr
    content[offset:offset + size] = b'\x90' * size

def fill_jmp(src, dest):
    offset = src - base_addr
    if dest != src + 5:
        content[offset] = 0xE9
        content[offset + 1:offset + 5] = (dest - src - 5).to_bytes(4, 'little', signed=True)
    else:
        fill_nops(src, 5)

def get_jx_opcode(jx_type):
    ks = Ks(KS_ARCH_X86, KS_MODE_32)
    code, count = ks.asm(f'{jx_type} 0xFFFFFFFF')
    return b''.join(map(lambda x: x.to_bytes(1, sys.byteorder), code[0:2]))

def fill_jx(src, dest, cmov_type):
    offset = src - base_addr
    content[offset:offset + 2] = get_jx_opcode(cmov_type.replace('cmov', 'j'))
    content[offset + 2:offset + 6] = (dest - src - 6).to_bytes(4, 'little', signed=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Deobfuscate OLLVM Control Flow Flatten')
    parser.add_argument('-f', '--file', help='binary to deobfuscate')
    parser.add_argument('-s', '--start', help='start address of the deobfuscation')
    parser.add_argument('-o', '--out', help='output file path')
    args = parser.parse_args()
    if args.file is None or args.start is None or args.out is None:
        parser.print_help()
        sys.exit(0)
    filename = args.file            # 文件名
    start = int(args.start, 16)     # 起始地址
    # load_options={'auto_load_libs': False}
    # 避免生成cfg时解析到共享库的函数
    proj = angr.Project(filename, load_options={'auto_load_libs': False})

    # 第一步：获取函数CFG（类似于IDA的CFG）
    # 分析CFG得到入口块（序言）、主分发器、返回块、真实块、预分发块
    print('**************** Step-1 Static Analysis(1/3) ****************')
    cfg = get_cfg()
    prologue_node, main_dispatcher_node, sub_dispatcher_nodes, retn_nodes, relevant_nodes, predispatcher_node = analyse_blocks()
    print('Prologue block at %#x' % prologue_node.addr)
    print('Main dispatcher block at %#x' % main_dispatcher_node.addr)
    print('Sub dispatcher blocks at ', [hex(node.addr) for node in sub_dispatcher_nodes])
    print('Return blocks at ', [hex(node.addr) for node in retn_nodes])
    print('Relevant blocks at ', [hex(node.addr) for node in relevant_nodes])
    print('Predispatcher blocks at %#x' % predispatcher_node.addr)

    # 第二步：恢复真实块前后关系，重建控制流
    # 从一个真实块开始符号执行
    # 如果没有分支，计算出下一个到达的真实块
    # 如果有分支，条件为True时到达的真实块和条件为False时到达的真实块
    print('**************** Step-2 Recover Control Flow(2/3) ****************')
    relevant_addrs = [node.addr for node in relevant_nodes]
    relevant_addrs += [node.addr for node in retn_nodes]
    patch_addrs = {}
    cmov_types = {}
    flow = defaultdict(list)
    for node in relevant_nodes:
        block_addr = node.addr
        has_branch = preprocess(block_addr)
        if has_branch:
            symbolic_execute(block_addr, modify_cond=claripy.BVV(1, 1))
            symbolic_execute(block_addr, modify_cond=claripy.BVV(0, 1))
        else:
            symbolic_execute(block_addr)
    for node in relevant_nodes:
        block_addr = node.addr
        print('Real successors of block %#x: ' % block_addr, [hex(child) for child in flow[block_addr]])

    # 第三步：Patch程序，输出恢复后的可执行文件
    print('**************** Step-3 Patch Binary(3/3) ****************')
    base_addr = proj.loader.main_object.mapped_base
    with open(filename, 'rb') as file:
        content = bytearray(file.read())
    for node in sub_dispatcher_nodes:
        fill_nops(node.addr, node.size)
        print('Fill nops from %#x to %#x' % (node.addr, node.addr + node.size))
    for node in relevant_nodes:
        childs = flow[node.addr]
        if len(childs) == 1:
            patch_addr = node.addr + node.size - 5
            if node.addr == prologue_node.addr:
                patch_addr = node.addr + node.size
            fill_jmp(patch_addr, childs[0])
            print('Patch jmp %#x at %#x' % (childs[0], patch_addr))
        elif len(childs) == 2:
            patch_addr = patch_addrs[node.addr]
            cmov_type = cmov_types[node.addr]
            fill_nops(patch_addr, node.addr + node.size - patch_addr)
            fill_jx(patch_addr, childs[0], cmov_type)
            fill_jmp(patch_addr + 6, childs[1])
            print('Patch jz %#x at %#x' % (childs[0], patch_addr))
            print('Patch jmp %#x at %#x' % (childs[1], patch_addr + 6))
        else:
            print('Error')
            sys.exit(-1)
    with open(args.out, 'wb') as file:
        file.write(content)