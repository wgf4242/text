"""
gdb attach 的几种方式
https://pwntools-docs-zh.readthedocs.io/zh_CN/dev/gdb.html
"""


from pwn import *

is_debug = False
# is_debug = True

io = process('./pwnme')
context(log_level='debug', arch='i386', os='linux' )
context(log_level='debug', arch='amd64', os='linux' )
context.arch = 'amd64'
context.terminal = ['gnome-terminal', '-x', 'sh', '-c']
context.terminal = ['tmux', 'splitw', '-h', '-F' '#{pane_pid}', '-P']
context.terminal = ["tmux", "splitw", "-h"]

pid = print('id is ', proc.pidof(io)[0])

# attach 跟在 process 后, 不要放在最后面.
if is_debug:
    gdb.attach(io)
    gdb.attach(io, 'b *0x400620')
    gdb.attach(io, gdbscript='b *0x400620\nc\n')
    gdb.attach(io, gdbscript=open('gdb.x'))
    gdb.attach(io, '''
    b main
    b * 080486BA 
    ''')


shellcode_addr=conn.recvuntil('?',drop=True)
conn.sendlineafter('a', payload)

# drop=True
# Message is : "hi?"
conn.recvuntil('?',drop=True) # hi
conn.recvuntil('?')           # hi?

# ELF
e=ELF("./level2")
next(e.search(b"/bin/sh"))


# cyclic leak
g = cyclic_gen() # Create a generator
c = g.get(240)
leak =g.find('acaa')[0]
print('leak is ' ,leak)
