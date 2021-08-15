# https://github.com/Ganapati/RsaCtfTool/
import os

rsa = '/home/kali/Downloads/RsaCtfTool/RsaCtfTool.py'

e = 65537
n = 1455925529734358105461406532259911790807347616464991065301847
c = 69380371057914246192606760686152233225659503366319332065009

os.system(f'{rsa} -n {N} -e {e} --private --dumpkey')

os.system(f'{rsa} -n {n} -e {e} --private --uncipher {c}')

os.system(f'{rsa} -n {n} -e {e} --private --uncipher {c} --attack cube_root')  # 低指数攻击

os.system(f'{rsa} --key pubkey.pem --uncipherfile ./flag.enc')

os.system(f'{rsa} --publickey public.key --private ')

os.system(f'{rsa} --publickey public.key --private --uncipherfile ./flag.enc')

os.system(f'{rsa} --dumpkey --key public.key')  # get n e,



### read n , e from key

from Crypto.PublicKey import RSA
from numpy.compat import long

public = RSA.importKey(open('public.key').read())
n = long(public.n)
e = long(public.e)
print(n)
print(e)
