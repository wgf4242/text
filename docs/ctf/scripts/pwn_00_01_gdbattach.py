"""
gdb attach 的几种方式
https://pwntools-docs-zh.readthedocs.io/zh_CN/dev/gdb.html
$ tmux # 进入 tmux再 $python3 exp.py
"""


from pwn import *

is_debug = False
# is_debug = True

io = process('./pwnme')
io = process('./pwn1', env={"LD_PRELOAD": "./libc-2.23.so"}) # 自定义预加载libc.so
# io = gdb.debug('./test', 'b main\nc')  # type: process 可以断在 main 处. attach比较慢,运行时main已经执行断不下来

# libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
# libc = ELF('/lib/i386-linux-gnu/libc.so.6')

context(log_level='debug', arch='i386', os='linux' )
context(log_level='debug', arch='amd64', os='linux' )
context.arch = 'amd64'
context.terminal = ['gnome-terminal', '-x', 'sh', '-c']
context.terminal = ['tmux', 'splitw', '-h', '-F' '#{pane_pid}', '-P']
context.terminal = ["tmux", "splitw", "-h"]

success('0x123') # 以 [+] 开头输出内容


pid = print('id is ', proc.pidof(io)[0])

# attach 跟在 process 后, 不要放在最后面.
if is_debug:
    gdb.attach(io)
    gdb.attach(io, 'b *0x400620')
    gdb.attach(io, 'b *0x00400627\ncondition 1 $rdx>18\nc')  # 条件断点
    gdb.attach(io, gdbscript='b *0x400620\nc\n')
    gdb.attach(io, gdbscript='b *$rebase(0x933)\nc\n')
    gdb.attach(io, gdbscript=open('gdb.x'))
    gdb.attach(io, gdbscript='''
    b main
    b * 080486BA 
    ''')


shellcode_addr=conn.recvuntil('?',drop=True)
conn.sendlineafter('a', payload)

# exec('n=1', globals())

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
