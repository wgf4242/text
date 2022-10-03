# sha256碰撞,得出xxxx的值
import hashlib
import itertools
import re

from pwn import remote

hashcat_path = r"F:\downloads\@CTF\hashcat-6.2.3"
host = 'nc 180.184.96.131 30021'
pattern = '''sha256(("`match`"ssss== "`match`"'''  # `match`,  ssss: .+? dot star
ip, port = host.split(' ')[1:]

String = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz'
strlist = itertools.product(String, repeat=4)


def proof_of_work(prefix, sha256enc):
    for x in strlist:
        rinput = ''.join(x).encode()
        b = prefix + rinput
        sha = hashlib.sha256(b).hexdigest().encode()
        if sha == sha256enc:
            return rinput


def bf_hashcat(prefix, sha256enc):
    import os
    import subprocess

    cmd = f"""hashcat -m 1400 -O -a 3 {sha256enc} {prefix}?1?1?1?1  --custom-charset1=?l?u?d"""
    os.chdir(hashcat_path)

    print(subprocess.getoutput(cmd))
    out = subprocess.getoutput(cmd + ' --show')
    hash, pwd = out.split(':')
    print(pwd)
    return pwd.replace(prefix, '').encode()


sh = remote(ip, port)
msg = sh.recvuntil('equation:')
pattern2 = re.escape(pattern).replace('`match`', r'(.*?)')
pattern2 = pattern2.replace('ssss', '.*?')
r = re.search(pattern2.encode(), msg)
if not r:
    print('not found')
prefix, sha256enc = r.groups()
# res = proof_of_work(prefix, sha256enc)
res = bf_hashcat(prefix.decode(), sha256enc.decode())

print(msg)
sh.sendline(res)
sh.interactive()
