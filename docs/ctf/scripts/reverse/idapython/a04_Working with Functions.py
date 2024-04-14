# check function
def main():
    ea = idc.here()
    f = idaapi.get_func(ea)
    if not f:
        print(f"Not inside a function @ {ea:x}!")
        return False
    print(f"func_start: {f.start_ea:x} {f.end_ea:x}")
    print(f"function flags: {f.flags:x}")
    if f.flags & idaapi.FUNC_LIB != 0:
        print("It's a library function!")
    return True

idaapi.msg_clear()
main()


# show function
idaapi.msg_clear()
ea = idaapi.get_screen_ea()
f = idaapi.get_func(ea)
print(f"func name is {get_name(f.start_ea)}")

# Enumerating with idautils.Functions
import idautils

for func_ea in idautils.Functions():
    f = idaapi.get_func(func_ea)
    name = idaapi.get_name(func_ea)
    print(f"{f.start_ea:08x}-{f.end_ea:08x} {name}")

# qty
idaapi.msg_clear()
qty = idaapi.get_func_qty()
print(f"We have {qty}")
lib_funcs = 0
dnr_funcs = 0
for i in range(qty):
    f = idaapi.getn_func(i)
    if not f.does_return():
        dnr_funcs += 1
    if f.flags & idaapi.FUNC_LIB != 0:
        lib_funcs += 1
print(f"{lib_funcs} library function(s) and {dnr_funcs} do not return function(s)")

# 输出地址和汇编代码
f = idaapi.get_func(idc.here())
end_ea = f.end_ea
ea = f.start_ea
while ea < f.end_ea:
    inst = idautils.DecodeInstruction(ea)
    if not inst:
        print(f"Could not decode at {ea:x}")
        break
    print(f"{ea:08x} {idc.GetDisasm(ea)}")
    ea += inst.size