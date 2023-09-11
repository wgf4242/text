```
from Crypto.Util.number import *
from secret import flag, p, q, a, b, e1, e2, e3

assert isPrime(p) and isPrime(q)
assert flag.startswith("DASCTF{") and flag.endswith("}")

class ECC():
    def __init__(self, a, b, p, q, e):
        self.p, self.q = p, q
        self.a, self.b = a, b
        self.N         = p * q
        self.e         = e
        self.Kbits     = 8
        self.Ep        = EllipticCurve(IntegerModRing(p), [a, b])
        self.Eq        = EllipticCurve(IntegerModRing(q), [a, b])

        N1 = self.Ep.order()
        N2 = 2 * p + 2 - N1
        N3 = self.Eq.order()
        N4 = 2 * q + 2 - N3

        self.d = {
            ( 1,  1): inverse_mod(e, lcm(N1, N3)),
            ( 1, -1): inverse_mod(e, lcm(N1, N4)),
            (-1,  1): inverse_mod(e, lcm(N2, N3)),
            (-1, -1): inverse_mod(e, lcm(N2, N4))
        }

        self.E = EllipticCurve(IntegerModRing(self.N), [a, b])

    def enc(self, plaintext):
        msg_point = self.msg_to_point(plaintext, True)
        mp = self.Ep(msg_point)
        mq = self.Eq(msg_point)
        cp = (self.e * mp).xy()
        cq = (self.e * mq).xy()
        cp = (int(cp[0]), int(cp[1]))
        cq = (int(cq[0]), int(cq[1]))
        c  = (int(crt([cp[0], cq[0]], [self.p, self.q])), \
              int(crt([cp[1], cq[1]], [self.p, self.q])))
        c = self.E(c)
        return c.xy()

    def dec(self, ciphertext):
        x = ciphertext
        w = x^3 + self.a*x + self.b % self.N

        P.<Yp> = PolynomialRing(Zmod(self.p))
        fp = x^3 + self.a*x + self.b -Yp^2
        yp = fp.roots()[0][0]

        P.<Yq> = PolynomialRing(Zmod(self.q))
        fq = x^3 + self.a*x + self.b -Yq^2
        yq = fq.roots()[0][0]

        y = crt([int(yp), int(yq)], [self.p, self.q])

        cp, cq = self.Ep((x, y)), self.Eq((x, y))
        legendre_symbol_p = legendre_symbol(w, self.p)
        legendre_symbol_q = legendre_symbol(w, self.q)

        mp = (self.d[(legendre_symbol_p, legendre_symbol_q)] * cp).xy()
        mq = (self.d[(legendre_symbol_p, legendre_symbol_q)] * cq).xy()

        return crt([int(mp[0]), int(mq[0])], [self.p, self.q]) >> self.Kbits

    def msg_to_point(self, x, shift=False):
        if shift:
            x <<= self.Kbits
        res_point = None
        for _ in range(2 << self.Kbits):
            P.<Yp> = PolynomialRing(Zmod(self.p))
            fp = x^3 + self.a*x + self.b - Yp^2
            P.<Yq> = PolynomialRing(Zmod(self.q))
            fq = x^3 + self.a*x + self.b - Yq^2
            try:
                yp, yq = int(fp.roots()[0][0]), int(fq.roots()[0][0])
                y = crt([yp, yq], [self.p, self.q])
                E = EllipticCurve(IntegerModRing(self.p*self.q), [self.a, self.b])
                res_point = E.point((x, y))
                return res_point
            except:
                x += 1
        return res_point


ecc1 = ECC(a, b, p, q, e1)
ecc2 = ECC(a, b, p, q, e2)
ecc3 = ECC(a, b ,p, q, e3)
gift = p * q * getPrime(1000)

secret = bytes_to_long(flag[7:-1].encode())
ciphertext1 = ecc1.enc(secret)
ciphertext2 = ecc2.enc(secret)
ciphertext3 = ecc3.enc(secret)

with open("output.txt", "w") as f:
    
    f.write(f"e1 = {e1}\n")
    f.write(f"e2 = {e2}\n")
    f.write(f"e3 = {e3}\n")
    f.write(f"gift = {gift}\n")
    f.write(f"C1 = {ciphertext1}\n")
    f.write(f"C2 = {ciphertext2}\n")
    f.write(f"C3 = {ciphertext3}\n")

```





题解:

1、由于已知三个密文C1，C2，C3，三个密文都在椭圆曲线上，因此可利用椭圆曲线表达式 $y^2=x^3+ax+b$ 在模kn(gift)下建立三个方程，，利用Groebner基进行化简很容易求出a和b，并且n也可以被规约出来。 

2、得到a，b，n就可以恢复等效的椭圆曲线$y^2=x^3+x+bmod \ n$。不难发现enc就是ECC上的群构成的RSA加密，即将明文映射为ecc上的点m，然后有 $c=c \cdot m $，这个数乘运算是在ecc上点的运算。现有同一个m用三组不同e加密得到的c，这可以类比rsa的共模攻击，具体地，利用拓展欧几里得算法，容易求得，经测试 $g_2$等于1，那么 ，而$s_1,t_1,s_2,t_2$都已知了，全部带入即可。



```
from sage.all import *

e1 = 516257683822598401
e2 = 391427904712695553
e3 = 431785901506020973
gift = 10954621221812651197619957228527372749810730943802288293715079353550311138677754821746522832935330138708418986232770630995550582619687239759917418738050269898943719822278514605075330569827210725314869039623167495140328454254640051293396463956732280673238182897228775094614386379902845973838934549168736103799539422716766688822243954145073458283746306858717624769112552867126607212724068484647333634548047278790589999183913
C1 = (1206929895217993244310816423179846824808172528120308055773133254871707902120929022352908110998765937447485028662679732041, 652060368795242052052268674691241294013033011634464089331399905627588366001436638328894634036437584845563026979258880828)
C2 = (1819289899794579183151870678118089723240127083264590266958711858768481876209114055565064148870164568925012329554392844153, 1110245535005295568283994217305072930348872582935452177061131445872842458573911993488746144360725164302010081437373324551)
C3 = (1112175463080774353628562547288706975571507012326470665917118873336738873653792420189391867408691423887642725415133046354, 1820636035485820691083758790204536675748006232767111209985774382700260408550258280489088658228739971137550264759084468620)
# 根据椭圆曲线表达式构造 groebner_basis() 
P.<a,b>=PolynomialRing(Zmod(gift))
F=[]
f1 = C1[0]^3 + a*C1[0] + b - C1[1]^2 
f2 = C2[0]^3 + a*C2[0] + b - C2[1]^2
f3 = C3[0]^3 + a*C3[0] + b - C3[1]^2
F.append(f1)
F.append(f2)
F.append(f3)

Ideal = Ideal(F)
I = Ideal.groebner_basis()
print(I)
# 求解参数a b n
res=[x.constant_coefficient() for x in I]
n = res[2]
a = -res[0]%n
b = -res[1]%n
      
E=EllipticCurve(Zmod(n),[a,b])
P1=E(C1)
P2=E(C2)
P3=E(C3)
# 三个e的ECRSA共模攻击
g1,s1,t1=xgcd(e1,e2)
g2,s2,t2=xgcd(g1,e3)
assert g2 == 1
M=s2*s1*P1 + s2*t1*P2 + t2*P3
from Crypto.Util.number import *
print(long_to_bytes(int(M[0])))
```