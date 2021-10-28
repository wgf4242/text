# 当e约去公约数后与phi互素
def decrypt(p, q, e, c):
    n = p * q
    phi = (p - 1) * (q - 1)
    t = gmpy2.gcd(e, phi)
    d = gmpy2.invert(e // t, phi)
    m = pow(c, d, n)
    print(m)
    msg = gmpy2.iroot(m, t)
    print(msg)
    if msg[1]:
        print(long_to_bytes(msg[0]))
decrypt(p, q, e, c) 作者：风二西 https://www.bilibili.com/read/cv13702478?spm_id_from=333.999.0.0 出处：bilibili