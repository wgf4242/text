# a=0e开头字符串 , 
# php弱等于0e开头 a == sha1(md5(a))
import hashlib

from Crypto.Util.number import long_to_bytes
import string

s = 'DD01903921EA24941C26A48F2CEC24E0BB0E8CC7'


for a in string.digits:
    for b in string.digits:
        for c in string.digits:
            for d in string.digits:
                m = (a+b+c+d).encode()
                # r1 = hashlib.md5(a).digest()
                r2 = hashlib.sha1(m).hexdigest()
                if r2.upper() == s:
                    print(m)
                    exit(0)
