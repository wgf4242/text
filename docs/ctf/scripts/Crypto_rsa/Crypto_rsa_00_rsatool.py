# https://github.com/Ganapati/RsaCtfTool/
# yafu-x64 "factor(@)" -batchfile pcat.txt
# yafu.bat: yafu-x64.exe factor(%1)
import os

rsa = '/home/kali/Downloads/RsaCtfTool/RsaCtfTool.py'
yafu_path = r'E:\Software\CTF\【渗透测试工具包AIO201811】\0x08CTF-AWD\RSA\RSA大整数分解\yafu-1.34\yafu-x64.exe'
# yafu_path = r'c:\wgf\CTF\Crypto_yafu-1.34\yafu-x64.exe'

e = 65537
n = 1455925529734358105461406532259911790807347616464991065301847
c = 69380371057914246192606760686152233225659503366319332065009

os.system(f'{rsa} -n {n} -e {e} --private --dumpkey')

os.system(f'{rsa} -n {n} -e {e} --private --uncipher {c}')

os.system(f'{rsa} -n {n} -e {e} --private --uncipher {c} --attack cube_root')  # 低指数攻击

os.system(f'{rsa} --key pubkey.pem --uncipherfile ./flag.enc')

os.system(f'openssl rsa -pubin -text -modulus -in warmup -in public.key')

os.system(f'{rsa} --publickey public.key --private ')

os.system(f'{rsa} --publickey public.key --private --uncipherfile ./flag.enc')

os.system(f'{rsa} --dumpkey --key public.key')  # get n e,

os.system(f'echo 手动 yafu_path n')  # get n e,

### read n , e from key

from Crypto.PublicKey import RSA
from numpy.compat import long

public = RSA.importKey(open('public.key').read())
n = long(public.n)
e = long(public.e)
print(n)
print(e)


def factor(N):
    cmd = f"{yafu_path} factor({N})"
    cmd2 = f'start cmd /k {cmd}'
    os.system(cmd2)

def get_key(key):
    f = open('public.key', 'rb').read()
    pub = RSA.importKey(f)
    n = pub.n
    e = pub.e
    print(n, '\n', e)

def decrypt(n, e, d, p, q):
    from Crypto.Cipher import PKCS1_OAEP
    from base64 import b64decode
    key_info = RSA.construct((n, e, d, p, q))
    key = RSA.importKey(key_info.exportKey())
    key = PKCS1_OAEP.new(key)
    f = open('flag.enc', 'r').read()
    c = b64decode(f)
    flag = key.decrypt(c)
    print(flag)