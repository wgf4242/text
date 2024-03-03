# 如果超过8字节 2个一组处理
def encrypt(v, k):
    v0, v1 = v
    x = 0
    delta = 0x9E3779B9
    k0, k1, k2, k3 = k
    for i in range(32):
        x += delta
        x = x & 0xFFFFFFFF
        v0 += ((v1 << 4) + k0) ^ (v1 + x) ^ ((v1 >> 5) + k1)
        v0 = v0 & 0xFFFFFFFF
        v1 += ((v0 << 4) + k2) ^ (v0 + x) ^ ((v0 >> 5) + k3)
        v1 = v1 & 0xFFFFFFFF
    return [v0, v1]


def decrypt(v, k):
    v0, v1 = v
    delta = 0x9E3779B9
    # x = sum(delta for _ in range(32)) & 0xFFFFFFFF
    x = delta * 32 & 0xffffffff
    k0, k1, k2, k3 = k
    for i in range(32):
        v1 -= ((v0 << 4) + k2) ^ (v0 + x) ^ ((v0 >> 5) + k3)
        v1 = v1 & 0xFFFFFFFF
        v0 -= ((v1 << 4) + k0) ^ (v1 + x) ^ ((v1 >> 5) + k1)
        v0 = v0 & 0xFFFFFFFF
        x -= delta
        x = x & 0xFFFFFFFF
    return [v0, v1]


if __name__ == '__main__':
    key = [17477, 16708, 16965, 17734]
    v = [0x3e8947cb, 0xcc944639]
    v = decrypt(v, key)
    assert v == [1480750694, 1631937617]  # [b'XBvf', b'aEdQ']
    r = encrypt(v, key)
    assert r == [0x3e8947cb, 0xcc944639]
