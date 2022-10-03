# https://blog.csdn.net/A951860555/article/details/120120400

import struct
from ctypes import *


def MX(z, y, total, key, p, e):
    temp1 = (z.value >> 5 ^ y.value << 2) + (y.value >> 3 ^ z.value << 4)
    temp2 = (total.value ^ y.value) + (key[(p & 3) ^ e.value] ^ z.value)

    return c_uint32(temp1 ^ temp2)


def encrypt(n, v, key):
    delta = 0x9e3779b9
    rounds = 6 + 52 // n

    total = c_uint32(0)
    z = c_uint32(v[n - 1])
    e = c_uint32(0)

    while rounds > 0:
        total.value += delta
        e.value = (total.value >> 2) & 3
        for p in range(n - 1):
            y = c_uint32(v[p + 1])
            v[p] = c_uint32(v[p] + MX(z, y, total, key, p, e).value).value
            z.value = v[p]
        y = c_uint32(v[0])
        v[n - 1] = c_uint32(v[n - 1] + MX(z, y, total, key, n - 1, e).value).value
        z.value = v[n - 1]
        rounds -= 1

    return v


def decrypt(n, v, key):
    delta = 0x9e3779b9
    rounds = 6 + 52 // n

    total = c_uint32(rounds * delta)
    y = c_uint32(v[0])
    e = c_uint32(0)

    while rounds > 0:
        e.value = (total.value >> 2) & 3
        for p in range(n - 1, 0, -1):
            z = c_uint32(v[p - 1])
            v[p] = c_uint32((v[p] - MX(z, y, total, key, p, e).value)).value
            y.value = v[p]
        z = c_uint32(v[n - 1])
        v[0] = c_uint32(v[0] - MX(z, y, total, key, 0, e).value).value
        y.value = v[0]
        total.value -= delta
        rounds -= 1

    return v


def assert1():
    k = [0x0000001E, 0xFFFFFF87, 0x0000004A, 0xFFFFFFB1]
    v = list(b'ZCTF')
    n = 4

    res = encrypt(n, v, k)
    res_hex_little_endian = struct.pack('<' + "I" * len(res), *res).hex()

    assert res_hex_little_endian == '53912aff24b6429435996691abd6da5d'
    res = [0xff2a9153, 0x9442b624, 0x91669935, 0x5ddad6ab]  # little_endian就是上面
    res = decrypt(n, res, k)
    assert bytearray(res) == b'ZCTF'


#  test
if __name__ == "__main__":
    # 该算法中每次可加密不只64bit的数据，并且加密的轮数由加密数据长度决定
    v = [0x12345678, 0x78563412]
    k = [0x1, 0x2, 0x3, 0x4]
    n = 2


    print("Data is : ", hex(v[0]), hex(v[1]))
    res = encrypt(n, v, k)
    print(f"Encrypted data is : ", ','.join(hex(x) for x in res))
    res = decrypt(n, res, k)
    print(f"Decrypted data is : ", ','.join(hex(x) for x in res))
    # ---------------
    assert1()
"""
Data is :  0x12345678 0x78563412
Encrypted data is :  0xef86c2bb 0x25f31b5e
Decrypted data is :  0x12345678 0x78563412
"""
