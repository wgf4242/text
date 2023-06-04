p = process('./pwnme')
context.terminal = ['gnome-terminal', '-x', 'sh', '-c']
gdb.attach(p)

context.terminal = ['tmux', 'splitw', '-h']
context.terminal = ['tmux', 'splitw', '-v']
# 新版本中不再使用execute参数，改用gdbscript
gdb.attach(p, gdbscript='b *0x400620\nc\n')
gdb.attach(p, gdbscript=open('gdb.x'))