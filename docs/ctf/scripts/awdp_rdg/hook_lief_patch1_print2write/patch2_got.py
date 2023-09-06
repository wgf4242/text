import lief

binary = lief.parse("./vulner")
hook = lief.parse('./hook')
# inject hook program to binary
segment_added  = binary.add(hook.segments[0])

# hook got
my_printf      = hook.get_symbol("myprintf")
my_printf_addr = segment_added.virtual_address + my_printf.value

binary.patch_pltgot('printf', my_printf_addr)
binary.write('vulner.patched')