# 仿射密码

仿射密码也是一个单表替换密码，字母表中的每个字母相应的值使用一个简单的数学函数映射到对应的数值，再把对应数值转换成字母。
仿射密码的加密函数是$e(x)=ax+b (mod \ m)$ ， 其中：

* a和m互质。
* m是字母的数目。

解密函数是$d(x)=a^{-1}(x-b）(mod \ m)$ ， 其中$a^{-1}$是a在集合Z上的逆元，
满足$a*a^{-1} \equiv 1 mod 26$求集合Z上某个数的逆元：

```python
gmpy2.invert(x, Z)
```

# 题目

## warmup（2021绿城杯）

```python
from Crypto.Util.number import *
from flag import flag
assert flag[:5]=='flag{'


str1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def encode(plain_text, a, b, m):
   cipher_text = ''
   for i in plain_text:
      if i in str1:
         addr = str1.find(i)
         cipher_text += str1[(a*addr+b) % m]
      else:
         cipher_text += i
   print(cipher_text)
encode(flag,37,23,52)
# cipher_text = 'aoxL{XaaHKP_tHgwpc_hN_ToXnnht}'
```

方式1: 正向爆破
```python
from string import printable
str1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encode(cipher_text, a, b, m):
    flag = ''
    for ch in cipher_text:
        if ch not in str1:
            flag += ch
        for p in printable:
            if p in str1:
                addr = str1.find(p)
                if str1[(a * addr + b) % m] == ch:
                    flag += p
                    continue
    print(flag)


cipher_text = 'aoxL{XaaHKP_tHgwpc_hN_ToXnnht}'
encode(cipher_text, 37, 23, 52)
```

方式2: 解密

```python
import gmpy2
str1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def decode(cipher_text, a, b, m):
    flag = ''
    for c in cipher_text:
        if c not in str1:
            flag += c
        addr = str1.find(c)
        a1 = gmpy2.invert(a, m)
        flag += str1[a1 * (addr - b) % m]
    print(flag)


cipher_text = 'aoxL{XaaHKP_tHgwpc_hN_ToXnnht}'
decode(cipher_text, 37, 23, 52)
```