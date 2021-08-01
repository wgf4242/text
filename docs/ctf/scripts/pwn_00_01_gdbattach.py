"""
gdb attach 的几种方式
"""


from pwn import *
p = process('./pwnme')
context(log_level='debug', arch='i386', os='linux' )
context.terminal = ['gnome-terminal', '-x', 'sh', '-c']

# attach 跟在 process 后, 不要放在最后面.
gdb.attach(p)
gdb.attach(p, gdbscript='b *0x400620\nc\n')
gdb.attach(p, gdbscript=open('gdb.x'))
gdb.attach(p,'''
b * 080486BA 
''')
