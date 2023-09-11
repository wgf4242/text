

题目 ecc_stream

```
from Crypto.Util.number import *
import random, hashlib
from secret import flag

f = open("output.txt","w")

p = getPrime(256)
a = random.randint(2, p-1)
b = random.randint(2, p-1)
x = random.randint(2, p-1)
E = EllipticCurve(GF(p),[a,b])
F = []
G = E.random_element()

enc = bytes([i^^j for (i,j) in zip(flag, hashlib.sha384(long_to_bytes(x)).digest())])

for i in range(256):
    F.append(G[x%2])
    x //= 2
    G = 2*G
    
f.write("enc = " + enc.hex() + "\n")
f.write("F = " + str(F) + "\n")
```

out.txt

```
enc = ba1e3092e2baba2ed9d70b5d847bb74d8a7b59461d16240c0017ed79c5e4052149129bc5d3c1112ad22e
F = [165...,140..., 730..., 145..., 262..., 113..., ...... 166..., 470..., 169..., 145...]
```



本题的关键在于恢复p，总共有256组，猜测大概率有连续为0的4组，即在数组中均为点x的值，由点的递推关系可得3个同余方程组，将a^2和a视为两个不同变量，分别解出，再根据`a^2-(a)^2==k*p`得到kp，发现不止一组，求gcd得到p。后续都非常顺理成章了。

```
res = []
for i in range(253):
    var('aa a b')
    eq = []
    for j in range(3):
        c0 = -2 * (F[i+j]^2)-4*F[i+j]*F[i+j+1]
        c1 = -4 * F[i+j+1]-8*F[i+j]
        c2 = F[i+j]^4 -4 * F[i+j+1] *(F[i+j]^3)
        eq.append(aa+c0*a+c1*b+c2==0)
    t0 = solve(eq, aa, a, b)[0][0].rhs()
    t1 = solve(eq, aa, a, b)[0][1].rhs()
    t1 = t1 ^ 2
    le = t0.numerator() * t1.denominator()
    rh = t0.denominator() * t1.numerator()
    res.append(abs(le - rh))
for i in range(253):
    for j in range(i + 1, 253):
        ans = gcd(res[i], res[j])
        if ans > 2 ^ 200:
            print(ans)
            print(i, j)
```

解得a,b

```
zp = Zmod(p)
for i in range(253):
    var('aa a b')
    eq = []
    for j in range(3):
        c0 = -2 * (F[i+j]^2)-4*F[i+j]*F[i+j+1]
        c1 = -4 * F[i+j+1]-8*F[i+j]
        c2 = F[i+j]^4 -4 * F[i+j+1] *(F[i+j]^3)
        eq.append(aa+c0*a+c1*b+c2==0)
    t0 = solve(eq, aa, a, b)[0][1].rhs()
    t1 = solve(eq, aa, a, b)[0][2].rhs()
    if i == 0:
        print(zp(t0.numerator())*zp(t0.denominator())^(-1))
        print(zp(t1.numerator())*zp(t1.denominator())^(-1))
```

还原x

```
p = 17820136898270565003583154860416743796390790040178335664072441472386305480761
a = 9350908279444197743025002468741904275718898737006581492427705992219827176952
b = 13500852895882965574928430100049589390809744881726797117323415176748623881582
E = EllipticCurve(GF(p),[a,b])
G = E(16581946065268567237817415232739386442228092328655083118189304246170597434332, 6572297618785458302447485568200876595775007972363489568076029901524495685352)
print(G)
print(G.xy()[0])
ans = 0
for i in range(256):
    try:
        x, y = G.xy()
        if F[i] == x:
            ans += 0
        else:
            ans += 2^i
        G = 2 * G
    except:
        print(G.xy())
print(ans)
```

异或得到flag

```
import random, hashlib
from Crypto.Util.number import *
enc = 'ba1e3092e2baba2ed9d70b5d847bb74d8a7b59461d16240c0017ed79c5e4052149129bc5d3c1112ad22e'
a = 4009442033181566772244087448152745364151945732097529946674447227730338811104
x = hashlib.sha384(long_to_bytes(a)).digest()
flag = bytes([i^j for (i,j) in zip(bytes.fromhex(enc), x)])
print(flag)
```