def test_bin_search():
    ea = 0x0000000140001000
    end_ea = ea + 0x100
    signs = ida_bytes.BIN_SEARCH_FORWARD | ida_bytes.BIN_SEARCH_NOBREAK | ida_bytes.BIN_SEARCH_NOSHOW
    ea = ida_bytes.bin_search(ea, end_ea, b"\xe8", b"\xe8", 1, signs)
    ea = ida_bytes.bin_search(ea, end_ea, b"\xe8", None, 1, signs)

def test_bin_search_idc():
    from idc import *
    ea = 0x0000000140001000
    end_ea = ea + 0x100
    ea = find_binary(ea, SEARCH_DOWN, 'E8 00 00 00 00')
    print(hex(ea))

def remove_junk_call_dollar():
    # call $+5 去除垃圾指令
    import idaapi
    from idc import *

    ea = 0x0000000140001000
    end_ea = ea + 0x100
    while ea < end_ea:
        ea = find_binary(ea, SEARCH_DOWN, 'E8 00 00 00 00')
        if ea == idaapi.BADADDR or ea > end_ea:
            break
        [patch_byte(ea, 0x90) for i in range(5 + 4)]
        create_insn(ea)  # makecode
