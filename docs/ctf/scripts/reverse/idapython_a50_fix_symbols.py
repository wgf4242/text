import idc
from idaapi import *

loadaddress = 0x10000  # 定义固件地址
eaStart = 0x301e64 + loadaddress
eaEnd = 0x3293a4 + loadaddress

ea = eaStart
eaEnd = eaEnd

while ea < eaEnd:
    offset = 0
    MakeStr(get_dword(ea - offset), BADADDR)
    sName = GetString(get_dword(ea - offset), -1, ASCSTR_C)
    print(sName)
    if sName:
        eaFunc = get_dword(ea - offset + 4)
        MakeName(eaFunc, sName)
        make_code(eaFunc)
        MakeFunction(eaFunc, BADADDR)
    ea = ea + 16
    # time.sleep(1)
print('ok')