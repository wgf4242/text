# 羊城杯2023 babyobfu
import re

SET_PTN = [
    r'byte ptr \[rbp-([0-9A-F]{1,3})h?]', # state
    r'([0-9A-F]{1,3})h?',
    r'offset (?:dword|unk)_([0-9A-F]{6})',
    r'\[rbp-([0-9A-F]{1,3})h?]', # data
    r'([0-9A-F]{1,9})h?'
]
DEC_PTN = [
    r'ds:(?:qword|off)_([0-9A-F]{6})',
    r'ds:qword_([0-9A-F]{6})',
    r'\[rbp-([0-9A-F]{1,3})h?]' # data
]
memset_searchDict = {
    "di": (r'\[rbp-([0-9A-F]{1,3})h?]', 0),
    "si": (r'(.*)', 1),
    "dx": (r'([0-9A-F]{1,3})h?', 2)
}
encrypt_searchDict = {
    "di": (r'\[rbp-([0-9A-F]{1,3})h?]', 0),
    "si": (r'\[rbp-([0-9A-F]{1,3})h?]', 1),
    "dx": (r'\[rbp-([0-9A-F]{1,3})h?]', 2)
}
NOP_TYPE = ["MEMSET", "KEY", "DEC", "ENC"]
g_func_addrs = [(0x4022B0, 0x4035BF), (0x401980, 0x4022B0), (0x401580, 0x401980), (0x4011B0, 0x401580)]
g_nop_addrs = []

def smc_keyset(state, size, idx_arr, data_arr, key):
    if state == 0:
        for i in range(size):
            idx = get_wide_dword(idx_arr + i*4)
            data_arr[idx] ^= key
    return

def smc_decrypt(code_addr, size, key):
    s = key.to_bytes(4, 'little')
    for i in range(size):
        code = get_wide_byte(code_addr+i)
        smc_key = ((i-50)&0xff) ^ s[i%4]
        patch_byte(code_addr+i, code ^ smc_key)
        del_items(code_addr+i)
    create_insn_with_check(code_addr)
    print("* Patch at", hex(code_addr), "for", size, "bytes with key", hex(key))
    return

def create_insn_with_check(ea):
    off = 1
    while create_insn(ea) == 0:
        del_items(ea, 0, off)
        off += 1
    return

def search_up_for_args(ea, searchDict, nop):
    global g_nop_addrs
    tl = []
    sDict = searchDict.copy()
    while bool(sDict):
        ea = prev_head(ea)
        opn0 = print_operand(ea, 0)[-2:]
        opn1 = print_operand(ea, 1)
        if opn0 in sDict.keys():
            g_nop_addrs.append((ea, ea+get_item_size(ea), nop))
            matchobj = re.match(sDict[opn0][0], opn1)
            if matchobj is not None:
                try:
                    tl.append((int(matchobj.groups()[0], 16), sDict[opn0][1]))
                except ValueError:
                    tl.append(("NONE", sDict[opn0][1]))
            else:
                sDict.update({opn1[-2:]: sDict[opn0]})
            del sDict[opn0]
    tl.sort(key=lambda t:t[1])
    return tl

def dobf_func(func_addr_t):
    arr_addrs = [] # [state_addr, state_size], [data_addr, data_size]
    ea = func_addr_t[0]
    print("START at", hex(ea))
    while ea < func_addr_t[1]:
        try:
            create_insn_with_check(ea)
        except:
            print("FUNC END at", hex(ea))
            break
        opcode = print_insn_mnem(ea)
        operand = print_operand(ea, 0)
        if operand == "smc_keyset":
            assert len(arr_addrs) == 2
            addr = ea
            args = []
            for i in range(5)[::-1]:
                addr = prev_head(addr)
                opn = print_operand(addr, 1)
                matchobj = re.match(SET_PTN[i], opn)
                if matchobj is None:
                    matchobj = re.match(r'([0-9A-F]{1,9})h?', opn)
                assert matchobj is not None
                args.append(int(matchobj.groups()[0], 16))
            g_nop_addrs.append((addr, ea+get_item_size(ea), NOP_TYPE.index("KEY")))
            args = args[::-1]
            args[0] = state_arr[arr_addrs[0][0] - args[0]]
            args[3] = data_arr
            print("* smc_keyset addr:", hex(ea))
            smc_keyset(*args)
        elif operand == "smc_decrypt":
            assert len(arr_addrs) == 2
            addr = ea
            args = []
            for i in range(10):
                addr = prev_head(addr)
                op = print_insn_mnem(addr)
                opn0 = print_operand(addr, 0)
                opn1 = print_operand(addr, 1)
                if op == "mov" and opn1 == "1":
                    matchobj = re.match(SET_PTN[0], opn0)
                    state_addr = int(matchobj.groups()[0], 16)
                    assert matchobj is not None
                    state_arr[(arr_addrs[0][0]-state_addr)] = 1
                    break
            g_nop_addrs.append((addr, ea+get_item_size(ea), NOP_TYPE.index("DEC")))
            for i in range(3):
                addr = next_head(addr)
                opn = print_operand(addr, 1)
                matchobj = re.match(DEC_PTN[i], opn)
                assert matchobj is not None
                args.append(int(matchobj.groups()[0], 16))
            assert (arr_addrs[1][0] - args[2]) % 4 == 0
            args[0] = get_qword(args[0])
            args[1] = get_qword(args[1])
            args[2] = data_arr[(arr_addrs[1][0]-args[2])//4]
            print("* smc_decrypt addr:", hex(ea))
            smc_decrypt(*args)
        elif operand == "smc_encrypt":
            search_up_for_args(ea, encrypt_searchDict, NOP_TYPE.index("ENC"))
            g_nop_addrs.append((ea, ea+get_item_size(ea), NOP_TYPE.index("ENC")))
        elif len(arr_addrs) != 2 and operand == "_memset":
            addr = ea
            g_nop_addrs.append((ea, ea+get_item_size(ea), NOP_TYPE.index("MEMSET")))
            for i in range(5): # two _memset funcs apart <= 5 bytes
                addr += get_item_size(addr)
                create_insn_with_check(addr)
                if print_operand(addr, 0) == "_memset":
                    g_nop_addrs.append((addr, addr+get_item_size(addr), NOP_TYPE.index("MEMSET")))
                    for x in [ea, addr]:
                        memset_args = search_up_for_args(x, memset_searchDict, NOP_TYPE.index("MEMSET"))
                        memset_args = memset_args[:1] + memset_args[2:]
                        arr_addrs.append([t[0] for t in memset_args])
                    state_arr = [0] * arr_addrs[0][1]
                    data_arr = [0] * arr_addrs[1][1]
                    break
            print("INFO: init ", arr_addrs)
        ea += get_item_size(ea)

def main():
    for i in range(len(g_func_addrs)):
        dobf_func(g_func_addrs[i])
    for t in g_nop_addrs:
        for i in range(t[0], t[1]):
            patch_byte(i, 0x90)
            create_insn(i)
        add_hidden_range(t[0], t[1], NOP_TYPE[t[2]], '', '', 0xFFFFFF)
    for t in g_func_addrs:
        ea = t[0]
        while ea < t[1]:
            create_insn(ea)
            del_func(ea)
            ea += get_item_size(ea)
        add_func(t[0], t[1])

if __name__ == '__main__':
    print("\n-=-=-= start deobf =-=-=-")
    main()
