题目 N1CTF2022 Babyecc
```py
from Crypto.Util.number import *
from secret import flag

m = Integer(int.from_bytes(flag, 'big'))

for _ in range(7):
    p = getPrime(512)
    q = getPrime(512)
    n = p * q
    while 1:
        try:
            a = randint(0,n)
            b = randint(0,n)
            Ep = EllipticCurve(GF(p), [a,b])
            Gp = Ep.lift_x(m) * 2
            Eq = EllipticCurve(GF(q), [a,b])
            Gq = Eq.lift_x(m) * 2
            y = crt([int(Gp[1]),int(Gq[1])],[p,q])
            break
        except Exception as err:
            pass
    print(n, a, b, y)

# 有个7个数的txt
```

wp
```py
from Crypto.Util.number import *

lines = open("babyecc.txt","r").readlines()
fs = []
ns = []

def Function(n,a,b,y):
    P.<m> = PolynomialRing(Zmod(n))
    k = 4*(m^3+a*m+b)
    c = (3*m^2+a)^2
    f = k^3*y^2 - (c-2*m*k)^3 - a*(k^2*c-2*m*k^3) - b*k^3
    return f

for line in lines:
    n,a,b,y = [ZZ(i) for i in line.strip().split(" ")]
    f = Function(n,a,b,y).monic().change_ring(ZZ)
    fs.append(f)
    ns.append(n)

F = crt(fs,ns)
N = prod(ns)
FF = F.change_ring(Zmod(N))
roots = FF.small_roots(epsilon = 0.03)
print(roots)
print(long_to_bytes(int(roots[0])))
# n1ctf{7140f171-5fb5-484d-92f4-9f7ba02c33d0}
```