p = 319576316814478949870590164193048041239
q = 275127860351348928173285174381581152299
N = 0xC2636AE5C3D8E43FFB97AB09028F1AAC6C0BF6CD3D70EBCA281BFFE97FBE30DD
e = 65537
# d = 67595638816573989554792254030140009889606004728909368108258780298415699743563

import gmpy2
# radin 加密 , e=2

with open('flag.enc', 'rb') as f:
    cipher = f.read().hex()
    cipher = int(cipher, 16)
    print(cipher)

yp = gmpy2.invert(p, q)
yq = gmpy2.invert(q, p)

# 计算mp和mq
mp = pow(cipher, (p + 1) // 4, p)
mq = pow(cipher, (q + 1) // 4, q)

# 计算a,b,c,d
a = (yp * p * mq + yq * q * mp) % N
b = N - int(a)
c = (yp * p * mq - yq * q * mp) % N
d = N - int(c)

for i in (a, b, c, d):
    s = '%x' % i
    if len(s) % 2 != 0:
        s = '0' + s
    print (s)
    print(bytearray.fromhex(s).decode('Latin1'))
    # print(codecs.decode(s, "hex"))
    # print (bytearray.fromhex(s).decode())