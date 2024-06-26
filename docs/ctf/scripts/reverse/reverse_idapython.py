# https://github.com/Mas0nShi/utools_idapython_docs
# CheatSheet https://gist.github.com/icecr4ck/7a7af3277787c794c66965517199fc9c
# idautils.py 中可以看看列表

# https://hex-rays.com/products/ida/support/ida74_idapython_no_bc695_porting_guide.shtml

# create_insn(ea)         # makecode
# del_items(0x0140009624) # idc.MakeUnknown, Undefine addr,  del_items(ea, flags=0, nbytes=1, ...)
# del_items(0x0140009624, 0, 6) 

from ida_bytes import *
from ida_bytes import get_bytes, get_byte

def print_bytes_addr():
    from idaapi import *
    bytes_addr = 0xCFFFD6F8
    bytes_size = 32
    data = get_bytes(bytes_addr, bytes_size)
    L = [hex(ch) for ch in data]
    print(L)


# 假密文
# ['0xdd', '0x9f', '0x58', '0xb3', '0x72', '0x80', '0xef', '0x96', '0xc1', '0x2', '0x3b',


# https://www.52pojie.cn/thread-1117330-1-1.html
def print_dword_addr():
    addr = 0x08048A90  # 数组的地址
    arr = []
    for i in range(6):  # 数组的个数
        arr.append(Dword(addr + 4 * i))
    print(arr)


def patch_batch1():
    import idaapi
    from ida_search import find_binary
    from idaapi import *
    from idc import *
    from idautils import *

    ea = 0x00014000327C
    end_ea = ea + 0x3000
    while ea < end_ea:
        ea = find_binary(ea, SEARCH_DOWN, 'EB 00 48')
        if ea == idaapi.BADADDR or ea > end_ea:
            break
        patch_word(ea, 0x9090)
        create_insn(ea) # makecode

# CTF特训营 P117
def patch_batch():
    import idaapi
    from idaapi import *
    from idc import *
    from idautils import *

    start_ea = 0x401000

    patterns = [('73 02', 2), ('EB 03', 1), ('72 03 73 01', 1), ('74 03 75 01', 1), ('7E 03 7F 01', 1), ('74 04 75 02', 2)]

    for pattern in patterns:
        ea = start_ea
        while True:
            ea = FindBinary(ea, SEARCH_DOWN, pattern[0])
            if ea == idaapi.BADADDR:
                break
            ea += len(pattern[0].replace(' ', '')) / 2

            for i in range(pattern[1]):
                PatchByte(ea + i, 0x90)
                MakeCode(ea + i) # create_insn(0x014000332c)


# https://bbs.pediy.com/thread-260297.htm
def goInitarray(self):
    # _get_modules是idc提供的接口，如其名
    for module in idc._get_modules():
        # 遍历所有module，找到linker
        module_name = module.name
        if 'linker' in module_name:
            print('linker address is ' + str(hex(module.base + 0x2464)))
            # 0x2464是Android某个版本的init_array的偏移地址,
            # jumpto可以直接跳转到目标地址
            idc.jumpto(module.base + 0x2464)
            # 在init_array上下个断点
            idc.add_bpt(module.base + 0x2464, 1)
            # makecode更不用说了，相当于C
            idaapi.auto_make_code(module.base + 0x2464)


# 网鼎杯朱雀组 tree https://www.52pojie.cn/forum.php?mod=viewthread&tid=1181476
def wangding_tree():
    a = []
    lujing = []

    def traverse_leaf(pnode):
        if pnode != 0:
            if get_wide_dword(pnode + 12) == 0 and get_wide_dword(pnode + 16) == 0:
                print(chr(get_wide_byte(pnode)))
                print("".join(a))
                lujing.append([chr(get_wide_byte(pnode)), "".join(a)])
            a.append('0')
            traverse_leaf(get_wide_dword(pnode + 12))
            a.append('1')
            traverse_leaf(get_wide_dword(pnode + 16))
        if pnode != 0x00406530:
            a.pop()

    traverse_leaf(0x00406530)
    print(lujing)


def preorder():
    addr = 0x00601290

    def preorder_tree(addr):
        if addr:
            b = get_wide_byte(addr)
            print(chr(b))
            preorder_tree(get_dword(addr + 8))
            return preorder_tree(get_dword(addr + 16))

    preorder_tree(addr)


def export_asm():
    print("[-] 开始导出反汇编代码")
    import idautils
    ea = idc.ScreenEA()
    addrs = idautils.FuncItems(ea)
    text = ''
    for addr in addrs:
        # print idc.GetDisasm(addr)
        text += idc.GetDisasm(addr) + '\n'
    with open("D:\\disasm.txt", 'w') as f:
        f.write(text)
    print("[+] 成功将当前函数的反汇编代码写入d:\\disasm.txt")


def batch_bytes_selection_nop():
    from ida_bytes import *
    addr = 0x402219
    for i in range(224):
        a = addr + i
        patch_byte(a, get_byte(a) ^ 0x99)


def batch_bytes_xor_smcfix():
    from ida_bytes import *
    addr = 0x402219
    for i in range(224):
        a = addr + i
        patch_byte(a, get_byte(a) ^ 0x99)


def batch_bytes_undefined():
    import ida_bytes

    start_addr = 0x402219
    end_addr = 0x0402220

    for i in range(start_addr, end_addr):
        ida_bytes.del_items(i)


def print_current_addr():
    import idc
    ea = idc.get_screen_ea()
    print("Current cursor address: 0x{:X}".format(ea))

def jump_addr_next_func():
    import idc
    end = 0x0402220
    ea = idc.get_screen_ea()
    while idc.find_func_end(ea) < end:
        next_func = get_next_func(ea)
        print(hex(next_func))
        idc.jumpto(next_func)
        ea = idc.get_screen_ea()


def remake_main():
    # 先新建好所有函数, 再执行
    # -- 脚本将start~end所有函数 undefined, 在start处make function
    import ida_bytes

    start_addr = 0x0402126
    end_addr = 0x0402220

    for i in range(start_addr, end_addr):
        ida_bytes.del_items(i)

    idc.jumpto(start_addr)
    idc.add_func(start_addr)

    import ida_hexrays  # open pseudocode view
    ida_hexrays.open_pseudocode(0x0402126, ida_hexrays.OPF_NO_WAIT)


def ask():
    import ida_kernwin
    ID = ida_kernwin.ask_long(1, "Enemy skill No.?")
    print(ID)


from idc import get_reg_value


def get_register_value_rax():
    a = get_reg_value('rax')
    print(hex(a))

    # M2
    import idautils
    idautils.cpu.rbx = 123
    print(idautils.cpu.rbx)


import idaapi, datetime

def debug_methods():
	# ida_dbg.run_to()
    idc.run_to(0x600000)


def clear_output():
    form = idaapi.find_widget("Output window")
    idaapi.activate_widget(form, True)
    idaapi.process_ui_action("msglist:Clear")
    print('---------------IDA Python Running at {}---------------------'.format(datetime.datetime.now()))


clear_output()

# condition breakpoint
# zf == 1
from ida_bytes import get_byte, patch_byte
from idc import get_reg_value, get_qword


def condition_breakpoint():
    zf = get_reg_value('zf')
    return zf


from idc import savefile


def dump_data():
    address = 0x0400000
    file = "D:\\dump_mem.bin"
    size = 0x20
    savefile(file, 0, address, size)  # 0是pos, 表示前面添加多少个 00 填充


dump_data()


def dump_data2_slow():
    from ida_bytes import get_byte
    begin = 0x7FF6978E3040
    size = 0x34166
    file = "D:/a.so"
    lst = []
    for i in range(size):
        byte_tmp = get_byte(begin + i)
        lst.append(byte_tmp)
        if (i + 1) % 0x1000 == 0:
            print("All count:{}, collect current:{}, has finish {}".format(hex(size), hex(i + 1), (i + 1) / size))
    print('collect over')
    with open(file, 'wb') as fw:
        fw.write(bytearray(lst))
    print('write over')


dump_data()

# def dump_data_idc():
# 	auto fname      = "D:\\dump_mem.bin";
# 	auto address    = 0x0400000;
# 	auto size       = 0x0300000;
# 	auto file= fopen(fname, "wb");
#
# 	savefile(file, 0, address, size);
# 	fclose(file);


def my_get_all_refs():
    '''
      https://mp.weixin.qq.com/s/tQzJWaAyUT119lNIp_Az7g
      功能：获取一个函数的上层调用函数地址
      返回：函数的上层调用地址
    '''
    from idaapi import *

    def get_crefs(func):
        find_func = func
        addr = list(CodeRefsTo(find_func, 0))[0]
        up_call = get_func(addr).start_ea
        return up_call

    '''
      功能：获取godeep_tree.ApSzXJOjiFA到godeep_tree.VSWEwsr之间的所有函数上层调用
      返回：这两个函数之间的调用列表
    '''

    def get_all_refs():
        start_func = get_name_ea(0, 'godeep_tree.VSWEwsr')
        end_func = get_name_ea(0, 'godeep_tree.ApSzXJOjiFA')
        func_list = [start_func]
        while True:
            ret = get_crefs(start_func)
            func_list.append(ret)
            start_func = ret
            if ret == end_func:
                break
        return func_list

    refs = get_all_refs()
    print(refs)
    print(get_func_name(refs[0]))
    print(get_func_name(refs[-1]))


def segments():
    print([hex(x) for x in Segments()]) # segments 地址


def names():
    print([x for x in Names()]) # [ (5368714814, 'func9'), (5368714844, 'func10')], 地址+名字

def strings():
    print([str(x) for x in Strings()]) # Shift+F12相同

def getDataList():
    addr = 0x1400014B0
    count = 3
    print([hex(x) for x in GetDataList(addr, count)]) # 从地址读取数据 ['0x48', '0x83', '0xec']