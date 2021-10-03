

## easymath/TSG CTF 2020 Beginner's Crypto
https://ctftime.org/writeup/22374

```python

assert(len(open('flag.txt', 'rb').read()) < 50)
assert(str(int.from_bytes(open('flag.txt', 'rb').read(), byteorder='big') << 10000).endswith(
    '1862790884563160582365888530869690397667546628710795031544304378154769559410473276482265448754388655981091313419549689169381115573539422545933044902527020209259938095466283008'))
```

$$
c = flag * 2^{10000} mod \ 10^{175}
$$
At first you may try taking the inverse of $2^{10000}$ over $F_{10^{175}}$, but that should be impossible because they are not coprime.

The correct way is, first think of

$$
c = flag * 2^{10000} mod \ 5^{175}
$$

and, using Euler’s theorem, calculate:

$$
(2^{10000})^{-1} mod \ 5^{175}=(2^{10000})^{\phi(5^{175})-1}\&=(2^{10000})^{5^{175}-5^{174}-1}
$$

and get the flag by:

$$
flag=c*(2^{10000})^{-1}mod \ 5^{175}
$$

Since $256^{50}$<$5^{175}$, this is the only value that can satisfy the equation.

```python
c = 1002773875431658367671665822006771085816631054109509173556585546508965236428620487083647585179992085437922318783218149808537210712780660412301729655917441546549321914516504576
mod = 5 ** 175
phi = 5 ** 175 - 5 ** 174
inv = pow(pow(2, 10000, mod), phi - 1, mod)
print(((c * inv) % mod).to_bytes(50, byteorder='big'))
```


## 2021.09 DASCTF 签到 - 离散对数 n = 2 ** 512
同[网鼎杯2020青龙组] you_raise_me_up
https://www.bilibili.com/video/av668155150/
```python
import  gmpy2
import sympy
flag=sympy.discrete_log(n,c,m)
import binascii
print(binascii.unhexlify(hex(flag)[2:]))
```
```python
# sage
m = xx
c = yy
n = 2 ** 512

m = Mod(m,n)
c = Mod(c,n)
discrete_log(c,m)

```