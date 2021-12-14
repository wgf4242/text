# [GWCTF 2019]xxor
# https://blog.csdn.net/weixin_47158947/article/details/107693058

from Crypto.Util.number import long_to_bytes
import numpy as np

np.seterr(over='ignore')

a = [3746099070, 550153460, 3774025685, 1548802262, 2652626477, 2230518816]
a2 = [2, 2, 3, 4]
for j in range(0, 5, 2):
    v3 = np.uint32(a[j])
    v4 = np.uint32(a[j + 1])
    v5 = np.int32(1166789954 * 0x40& 0xffffffff)

    for i in range(0x3f + 1):
        v4 -= np.uint32((v3 + v5 + 20) ^ ((v3 << 6) + a2[2]) ^ ((v3 >> 9) + a2[3]) ^ 0x10)
        v3 -= np.uint32((v4 + v5 + 11) ^ ((v4 << 6) + a2[0]) ^ ((v4 >> 9) + a2[1]) ^ 0x20)
        v5 -= np.int32(1166789954)
    a[j] = v3
    a[j + 1] = v4

for i in range(6):
    print(long_to_bytes(a[i]).decode())
