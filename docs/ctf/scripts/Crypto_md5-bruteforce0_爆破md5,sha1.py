# a=0e开头字符串 , 
# php弱等于0e开头 a == sha1(md5(a))
import hashlib

from Crypto.Util.number import long_to_bytes

for i in range(10**5):
    a = b'0e'+long_to_bytes(i)
    r1 = hashlib.md5(a).digest()
    r2 = hashlib.sha1(r1).hexdigest()
    if r2.startswith('0e'):
        print(a)
