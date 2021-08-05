"""
gdb attach 的几种方式
https://pwntools-docs-zh.readthedocs.io/zh_CN/dev/gdb.html
"""


from pwn import *

is_debug = False
# is_debug = True

p = process('./pwnme')
context(log_level='debug', arch='i386', os='linux' )
context.terminal = ['gnome-terminal', '-x', 'sh', '-c']
context.terminal = ['tmux', 'splitw', '-h', '-F' '#{pane_pid}', '-P']
context.terminal = ["tmux", "splitw", "-h"]

pid = print('id is ', proc.pidof(p)[0])

# attach 跟在 process 后, 不要放在最后面.
if is_debug:
    gdb.attach(p)
    gdb.attach(p, gdbscript='b *0x400620\nc\n')
    gdb.attach(p, gdbscript=open('gdb.x'))
    gdb.attach(p, '''
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
