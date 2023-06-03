from pwn import *

libc = ELF('./libc.so')
system = libc.sym["system"]
print(hex(libc.address))
print(hex(system))

bin_sh = libc.search(b'/bin/sh').__next__()
print(hex(bin_sh))
# bin_sh =  libc.address + 0x18ce57
# success(hex(bin_sh))