第四届2021美团网络安全高校挑战赛 humburgerRSA题解
http://www.zbc53.top/archives/157/  Baby rsa,Crypto CTF rsa
https://blog.csdn.net/rickliuxiao/article/details/121882386


## 题目
```python
from Crypto.Util.number import *
 
flag = open('flag.txt').read()
nbit = 64
 
while True:
    p, q = getPrime(nbit), getPrime(nbit)
    PP = int(str(p) + str(p) + str(q) + str(q))
    QQ = int(str(q) + str(q) + str(p) + str(p))
    if isPrime(PP) and isPrime(QQ):
        break
 
n = PP * QQ
m = bytes_to_long(flag.encode())
c = pow(m, 65537, n)
print('n =', n)
print('c =', c)
```

## 解题

从n=172552610852624337784035949632908517355734035684070753814679795210135425973527923366032328492820431356488870897173177428620479155806759875055162439119840201 , p*q=172552610852624337765055162439119840201中，可以发现

str(N)[:19]==str(p*q)[:19]
str(N)[-19:]==str(p*q)[-19:]
且len(p*q)=39，为39位。
那么，已知前19位和后19位，总共位数是39，只需要爆破1位即可。


```python
from Crypto.Util.number import *

# 常规解题RSA
def decrypt_RSA(c, e, p, q):
    phi = (p-1) * (q-1)
    d = inverse(e, phi)
    m = pow(c, d, p*q)
    print(long_to_bytes(m))


N = 177269125756508652546242326065138402971542751112423326033880862868822164234452280738170245589798474033047460920552550018968571267978283756742722231922451193
c = 47718022601324543399078395957095083753201631332808949406927091589044837556469300807728484035581447960954603540348152501053100067139486887367207461593404096

low = str(N)[-19:]
high = str(N)[:18]
'''sage
for i in ['']+[str(i) for i in range(10)]:
    for j in ['']+[str(i) for i in range(10)]:
        n=int(high+i+j+low)
        f=factor(n)
        if len(f)==2:
            print(f)
'''
p = 9788542938580474429
q = 18109858317913867117
x, y = len(str(p)), len(str(q))

P = int(str(p) + str(p))
Q = int(str(q) + str(q))
PP = int(str(P) + str(Q))
QQ = int(str(Q) + str(P))
N = PP * QQ

decrypt_RSA(c, 65537, PP, QQ)
```