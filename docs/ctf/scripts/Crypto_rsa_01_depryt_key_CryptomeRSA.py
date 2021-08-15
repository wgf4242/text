from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5, PKCS1_OAEP
# from numpy.compat import long
import gmpy2

public = RSA.importKey(open('pub.key').read())
# n = long(public.n)
n = public.n  # yafu 分解 pq
e = public.e
p = 304008741604601924494328155975272418463
q = 285960468890451637935629440372639283459
d = int(gmpy2.invert(e, (p - 1) * (q - 1)))

enc = open('flag.enc', 'rb').read()

private_key = RSA.construct((n, e, d, p, q))  # 根据已知参数，计算私钥
cipher = Cipher_PKCS1_v1_5.new(private_key)
m = cipher.decrypt(enc, None).decode()
print(m)
