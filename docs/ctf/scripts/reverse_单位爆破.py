#  [ACTF新生赛2020]SoulLike
from pwn import *
import re

flag = "actf{"
# context.log_level="debug"

k = 0
while True:
    for i in range(33,127):
        p = process('./SoulLike')
        _flag = flag + chr(i)
        print _flag
        p.sendline(_flag)
        s = p.recvline()
        r = re.findall("on #(.*?)\n", s)[0]
        r = int(r)
        if r == k:
            print 'no'
            print k
        elif r == k + 1:
            print s
            flag += chr(i)
            k += 1
            p.close()
        p.close()
    if k > 11:
        break
print (flag)