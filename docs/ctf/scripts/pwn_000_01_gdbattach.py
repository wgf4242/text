"""
gdb attach 的几种方式
"""


from pwn import *
p = process('./pwnme')
context.terminal = ['gnome-terminal', '-x', 'sh', '-c']


gdb.attach(p)
gdb.attach(p, gdbscript='b *0x400620\nc\n')
gdb.attach(p, gdbscript=open('gdb.x'))
gdb.attach(p,'''
b * 080486BA 
''')
