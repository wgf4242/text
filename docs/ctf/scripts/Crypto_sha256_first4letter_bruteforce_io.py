# sha256碰撞,得出xxxx的值
import hashlib
import itertools
import re

from pwn import remote

hashcat_path = r"F:\downloads\@CTF\hashcat-6.2.3"
host = 'nc 120.79.18.34 20561'
# 示例值 sha256(XXXX+3foGpAabJ3MB4Tv1) == 28a9892c535a2c7a954fd8ad37ddcb068826fedbbd78d139900530a8c9d40e73
# 把垃圾换成 ssss, 匹配换成 `match`
pattern = '''sha256(ssss+`match`) == `match`'''  # `match`,  ssss: .+? dot star
rev_msg = b'tell me XXXX:'

ip, port = host.split(' ')[1:]

String = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz'
strlist = itertools.product(String, repeat=4)


def get_match(pattern, txt):
    pattern = re.escape(pattern)
    pattern = pattern.replace('`match`', r'(.+?\b)')
    pattern = pattern.replace('ssss', r'.+?')
    matches = re.findall(pattern, txt)
    if matches:
        return matches[0]
    raise Exception('not found')


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

    cmd = f"""hashcat -m 1400 -O -a 3 {sha256enc} ?1?1?1?1{prefix}  --custom-charset1=?l?u?d"""
    os.chdir(hashcat_path)

    print(subprocess.getoutput(cmd))
    out = subprocess.getoutput(cmd + ' --show')
    hash, pwd = out.split(':')
    print(pwd)
    return pwd.replace(prefix, '')


sh = remote(ip, port)
msg = sh.recvuntil(rev_msg).decode()

res = get_match(pattern, msg)
prefix, sha256enc = res
res = bf_hashcat(prefix, sha256enc)

print(msg)
sh.sendline(res)
sh.interactive()
