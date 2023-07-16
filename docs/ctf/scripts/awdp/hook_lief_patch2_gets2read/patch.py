import lief
from pwn import *

def patch_call(file,srcaddr,dstaddr,arch = "i386"):
	print(hex(dstaddr))
	length = p32((dstaddr - (srcaddr + 5 )) & 0xffffffff)
	order = '\xe8'+length
	print(disasm(order,arch=arch))
	# file.patch_address(srcaddr,[ord(i) for i in order])
	file.patch_address(srcaddr,[i for i in order])

binary = lief.parse("./ret2text")
hook = lief.parse('./hook_gets')

# write hook's .text content to binary's .eh_frame content 
sec_ehrame = binary.get_section('.eh_frame')
print(sec_ehrame.content)
sec_text = hook.get_section('.text')
print(sec_text.content)
sec_ehrame.content = sec_text.content
print(binary.get_section('.eh_frame').content)

# hook target call
dstaddr = sec_ehrame.virtual_address
srcaddr = 0x080486AE
print("dstaddr ==>", hex(dstaddr))
patch_call(binary,srcaddr,dstaddr)

binary.write('ret2text-patched')
# patch为 sys_read(0, 3, 0x20u);