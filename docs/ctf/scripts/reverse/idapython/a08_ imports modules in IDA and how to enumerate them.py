idaapi.msg_clear()

def print_name(ea, name, o):
    print(f" {ea:x}/#{o} {name}")
    return 0

qty = idaapi.get_import_module_qty()
print(f"We have {qty} imported module(s)")

for idx in range(qty):
    modname = idaapi.get_import_module_name(idx)
    print(f"module name is: {modname}")
    idaapi.enum_import_names(idx, print_name)



ea = idaapi.get_name_ea(idaapi.BADADDR, "GetLastError")
print(f"{ea:x}")