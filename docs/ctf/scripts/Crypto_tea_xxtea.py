# https://blog.csdn.net/A951860555/article/details/120120400
from ctypes import *


def MX(z, y, total, key, p, e):
    temp1 = (z.value >> 5 ^ y.value << 2) + (y.value >> 3 ^ z.value << 4)
    temp2 = (total.value ^ y.value) + (key[(p & 3) ^ e.value] ^ z.value)

    return c_uint32(temp1 ^ temp2)


def encrypt(n, v, key):
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


#  test
if __name__ == "__main__":
    # 该算法中每次可加密不只64bit的数据，并且加密的轮数由加密数据长度决定
    # 注意大小端, 方向错了没有
    delta = 0x9e3779b9
    v = [0x12345678, 0x78563412]
    k = [0x67616c66, 0, 0, 0]
    n = 6

    res = [0x40CEA5BC, 0xE7B2B2F4, 0x129D12A9, 0x5BC810AE, 0x1D06D73D, 0xDCF870DC]
    # print("Data is : ", hex(v[0]), hex(v[1]))
    # res = encrypt(n, v, k)
    # print("Encrypted data is : ", hex(res[0]), hex(res[1]))
    res = decrypt(n, res, k)
    print("Decrypted data is : ",)

    import struct
    for i in res:
        print(struct.pack("<I", i).decode(), end='')

    # for i in res:
        # print(i.to_bytes(4, 'little').decode(), end='')

    # from Crypto.Util.number import long_to_bytes
    # for i in res:
        # print(long_to_bytes(i).decode()[::-1],end='')


"""
Data is :  0x12345678 0x78563412
Encrypted data is :  0xef86c2bb 0x25f31b5e
Decrypted data is :  0x12345678 0x78563412
"""
