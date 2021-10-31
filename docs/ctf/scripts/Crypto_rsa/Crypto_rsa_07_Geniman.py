# 已知很大的 C 和 N，无法用常规方法分解，由开局的提示”孪生素数“或题目”Gemini_Man“，猜测 q=p+2。
# 代入 pq=N，解一元二次方程得到正确 p,q 值。
# 题目未给 e ，猜测为常见的 e=65537 ，常规脚本放到Kali环境跑出明文 m。
# （未知原因Windows环境下 pow(C,d,N) 死活跑不出）

from gmpy2 import *
n='*******'
c='*******'
p = iroot(n,2)[0]
q=p+2
print(p*q == n)
phi = (p-1)*(q-1)
e = 65537

print("d.....")
d = invert(e,phi)
print("m.....")

m = int(powmod(c,d,n))
print("flag....")
flag = bytes.fromhex(hex(m).strip("0xL"))
print(flag)
# b'Nep{e540b1fd7d4459619eecd244c12ae5c4}'