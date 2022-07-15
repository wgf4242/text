import hashlib
import string
from itertools import product

from bitstring import BitArray

e = b'3ia2UuuQ'
table = string.printable


def go(n=1):
    for i in product(table, repeat=n):
        #     m = e + bytes([i])
        key = ''.join(i)
        m = e + key.encode()
        sha = hashlib.sha256(m)
        r2 = sha.hexdigest()
        bits = BitArray(hex=r2)
        if bits.bin.endswith('000000000000000000'):
            print(key)
            exit()
    go(n + 1)


go()
