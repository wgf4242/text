'''
# aes_pell_佩尔_连分数_assert x**2 - D * y**2 == 1_114514 # hgame2024 ezMath

from Crypto.Util.number import *
from Crypto.Cipher import AES
import random,string
from secret import flag,y,x
def pad(x):
    return x+b'\x00'*(16-len(x)%16)
def encrypt(KEY):
    cipher= AES.new(KEY,AES.MODE_ECB)
    encrypted =cipher.encrypt(flag)
    return encrypted
D = 114514
assert x**2 - D * y**2 == 1
flag=pad(flag)
key=pad(long_to_bytes(y))[:16]
enc=encrypt(key)
print(f'enc={enc}')
#enc=b"\xce\xf1\x94\x84\xe9m\x88\x04\xcb\x9ad\x9e\x08b\xbf\x8b\xd3\r\xe2\x81\x17g\x9c\xd7\x10\x19\x1a\xa6\xc3\x9d\xde\xe7\xe0h\xed/\x00\x95tz)1\\\t8:\xb1,U\xfe\xdec\xf2h\xab`\xe5'\x93\xf8\xde\xb2\x9a\x9a"
'''

from Crypto.Util.number import *
from Crypto.Cipher import AES

enc = b"\xce\xf1\x94\x84\xe9m\x88\x04\xcb\x9ad\x9e\x08b\xbf\x8b\xd3\r\xe2\x81\x17g\x9c\xd7\x10\x19\x1a\xa6\xc3\x9d\xde\xe7\xe0h\xed/\x00\x95tz)1\\\t8:\xb1,U\xfe\xdec\xf2h\xab`\xe5'\x93\xf8\xde\xb2\x9a\x9a"


def solve_pell(N, num=100):
    c = continued_fraction(sqrt(N))
    for i in range(num):
        y = c.denominator(i)
        x = c.numerator(i)
        if x ^ 2 - N * y ^ 2 == 1:
            return x, y
    return None, None


def pad(x):
    return x + b'\x00' * ((16 - len(x)) % 16)


def decrypt(KEY):
    cipher = AES.new(KEY, AES.MODE_ECB)
    flag = cipher.decrypt(enc)
    return flag


N = 114514
numTry = 1500
x, y = solve_pell(N, numTry)
print(x, y)

y = pad(long_to_bytes(y))[:16]
flag = decrypt(y)
print(flag)
