# https://github.com/Ganapati/RsaCtfTool/
import os
import time
from threading import Thread

from Crypto.PublicKey import RSA

rsa = '/home/kali/Downloads/RsaCtfTool/RsaCtfTool.py'

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
### read n , e from key


print(n)
print(e)


def factor(N):
    cmd = f'yafu "factor({N})" > yafu_result.txt'
    # cmd2 = f'start cmd /k {cmd}'
    os.system(cmd)


def yafu(N):
    start = time.perf_counter()
    t1 = Thread(target=factor, args=(N,))
    t1.daemon = True
    t1.start()
    print('t1 start')
    t1.join(timeout=22)  # 超过 daemon时 超过 timeout时间 主线程退出后 其他线程退出
    end = time.perf_counter()
    print("总耗时:", end - start)
    os.system('pkill -9 yafu')


def get_key(key):
    pub = RSA.importKey(open('public.key').read())
    n = pub.n
    e = pub.e

    # n = long(pub.n)
    # e = long(pub.e)
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


if __name__ == '__main__':
    if n := globals().get('n', ""):
        factor(n)
