# myscript.py

example = '''Allocated chunk | PREV_INUSE
Addr: 0x15ed000
Size: 0x91
'''
import re

txt = gdb.execute('heap', to_string=True)
print(txt)
match = re.search('Addr:.*?(0x[a-f0-9]+)', txt)
if match:
    addr = match.group(1)
ptr = '0x602120'
print(addr)
cmd = f'hexdump {addr} 2300'
gdb.execute(cmd)
# gdb.execute(f'hex {addr} 2300')
gdb.execute('tel %s' % ptr)
gdb.execute('parseheap')
