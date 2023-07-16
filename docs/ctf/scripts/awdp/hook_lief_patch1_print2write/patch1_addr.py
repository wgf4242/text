import lief
from pwn import *

def patch_call(file,srcaddr,dstaddr,arch = "amd64"):
	print( hex(dstaddr))
	length = p32((dstaddr - (srcaddr + 5 )) & 0xffffffff)
	order = b'\xe8'+length
	print( disasm(order,arch=arch))
	# file.patch_address(srcaddr,[ord(i) for i in order])
	file.patch_address(srcaddr,[i for i in order])

binary = lief.parse("./vulner")
hook = lief.parse('./hook')
# inject hook program to binary
segment_added  = binary.add(hook.segments[0])
hook_fun      = hook.get_symbol("myprintf")

dstaddr = segment_added.virtual_address + hook_fun.value
srcaddr = 0x040057E

patch_call(binary,srcaddr,dstaddr)

binary.write('vulner.patched')