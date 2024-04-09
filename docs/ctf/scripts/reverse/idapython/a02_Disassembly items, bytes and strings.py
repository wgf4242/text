"""
# 控制台输入 ?idaapi.is_data
is_data(*args) -> 'bool'
    is_data(F) -> bool
    Does flag denote start of data?
    
    @param F: (C++: flags64_t)
"""
idaapi.msg_clear()
ea = idc.here()
ea_p1 = ea + 1
f = idaapi.get_flags(ea)
f_p1 = idaapi.get_flags(ea_p1)
# 菜单 View - Print internal flags

print("is_code:", idaapi.is_code(f))
print("is_unk:", idaapi.is_unknown(f))
print("is_data", idaapi.is_data(f))
print("has_name", idaapi.has_name(f))
print("is_head_ea", idaapi.is_head(f))
print("is_head_ea+1", idaapi.is_head(f_p1))
print("is_tail_ea", idaapi.is_tail(f))
print("is_tail_ea+1", idaapi.is_tail(f_p1))


idaapi.create_byte(here(),1)
idaapi.op_chr(here(),0)
idaapi.get_bytes(here(),10)
idaapi.get_bytes(here(),10).decode('utf-8')
?idaapi.get_strlit_contents    # ida控制台输入
idaapi.get_strlit_contents(idc.here(), -1, idaapi.STRTYPE_C)
b'GetModuleHandleW'
