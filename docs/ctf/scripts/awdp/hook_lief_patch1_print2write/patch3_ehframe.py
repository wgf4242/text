import lief
from pwn import *

def patch_call(file,srcaddr,dstaddr,arch = "amd64"):
	print(hex(dstaddr))
	length = p32((dstaddr - (srcaddr + 5 )) & 0xffffffff)
	order = b'\xe8'+length
	print(disasm(order,arch=arch))
	# file.patch_address(srcaddr,[ord(i) for i in order])
	file.patch_address(srcaddr,[i for i in order])

binary = lief.parse("./vulner")
hook = lief.parse('./hook')

# write hook's .text content to binary's .eh_frame content 
sec_ehrame = binary.get_section('.eh_frame')
print(sec_ehrame.content)
sec_text = hook.get_section('.text')
print(sec_text.content)
sec_ehrame.content = sec_text.content
print(binary.get_section('.eh_frame').content)

# hook target call
dstaddr = sec_ehrame.virtual_address
srcaddr = 0x040057E

patch_call(binary,srcaddr,dstaddr)

binary.write('vulner.patched')