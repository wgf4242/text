
# xref from
import idautils
idaapi.msg_clear()
ea = idaapi.get_screen_ea()
print(f"Address {ea:x} leads to:")
for xb in idautils.XrefsFrom(ea):
    print(f"   ---> {xb.to:x}")




# xref to
import idautils
idaapi.msg_clear()
ea = idaapi.get_name_ea(idaapi.BADADDR, "f6")
print(f"Address {ea:x} accessed by:")
for xb in idautils.XrefsTo(ea):
    if not xb.iscode: continue
    print(f"   ---> {xb.frm:x}")




# busy func: 函数使用次烽
import idautils
idaapi.msg_clear()
tally = {}
for func_ea in idautils.Functions():
    c = 0
    for xb in idautils.XrefsTo(func_ea):
        if xb.iscode: c += 1
    if c > 0:
        tally[func_ea] = c
sorted_tally = sorted(tally.items(), key=lambda x:x[1])
sorted_tally = reversed(sorted_tally)
for rank, (func_ea, called_count) in enumerate(sorted_tally, start=1):
    print(f"#{rank} {func_ea:16x} {idaapi.get_name(func_ea)} --> {called_count}")