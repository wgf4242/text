https://www.jianshu.com/p/a0aa94ef8ab2
https://blog.csdn.net/anscor/article/details/80878285
http://meta.math.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference
https://mirrors.tuna.tsinghua.edu.cn/CTAN/info/lshort/chinese/lshort-zh-cn.pdf



<h1 style="color:blue;text-align:center;">This is a header</h1>
<font size=4, color='red'><b>chosen font</b></font>


$$
\sum_{n=1}^{100}{a_n}
$$

$\sum_{i=0}^N\int_{a}^{b}g(t,i)\text{d}t$

$\frac{1}{2}$

1. 使用\ 表示空格

1|2|3|4
--|--|--|--
quad空格 |   a \qquad b | $a \qquad b$| 两个m的宽度
quad空格 |   a \quad b  | $a \quad b $| 一个m的宽度
大空格 |  a\ b          | $a\ b      $|        1/3m宽度
中等空格 |     a\;b     | $ a\;b     $|   2/7m宽度
小空格 |  a\,b          | $a\,b      $|        1/6m宽度
没有空格 |     ab       | $ab\,$
紧贴 |   a\!b           | $a\!b      $|         缩进1/6m宽度

## 字母 

显示|命令|显示|命令
--|--|--|--
α|\alpha|  β|   \beta
γ|\gamma|  δ|   \delta
ε|\epsilon|    ζ|   \zeta
η|\eta|    θ|   \theta
ι|\iota|   κ|   \kappa
λ|\lambda| μ|   \mu
ν|\nu| ξ|   \xi
π|\pi| ρ|   \rho
σ|\sigma|  τ|   \tau
υ|\upsilon|    φ|   \phi
χ|\chi|    ψ|   \psi
ω|\omega||

上标：^
下标：_
矢量: 
$$
\vec a , 
\overrightarrow{xy}
$$

\oplus 异或 $\oplus$ 
## 字体
Typewriter: \mathtt{A}

* $ \mathtt{A} $

Blackboard bold: \mathbb{A}

* $ \mathbb{A} $

Sans Serif: \mathsf{A}

* $ \mathsf{A} $

## 括号  符号

$$
(),
[],
\langle \rangle,
$$

\left或\right 使符号 大小与邻近的公式相适用

换行
$$
\begin{equation}
\begin{split}
y=a^2\\
  +i^2
\end{split}
\end{equation}
$$

开方 $\sqrt[4]{x}$

## RSA
[相关攻击](https://ohmygodlin.github.io/ctf/crypto/2018/09/26/RSA%E5%B8%B8%E8%A7%81%E6%94%BB%E5%87%BB%E6%96%B9%E6%B3%95/)
https://www.icode9.com/content-4-807230.html
https://lazzzaro.github.io/2020/05/06/crypto-RSA/index.html

欧拉函数: $x\le n$有多少$x$ ？ 计算这个值的方法就叫做欧拉函数，以$\phi (n)$表示

如果n质数, 就有n-1个x., $n = p * q$ 那么 $\phi (n) = \phi (pq)= \phi (p) * \phi (q)$

欧拉定理, pq是互质, phin是pq一共有多少
$$
\phi(n)=(p-1)(q-1)
$$


$$
\begin{align} 

n & = pq\\
\phi(n) & = (p-1)(q-1) -- \mathsf{求多少个数不能被n分解}\\
gcd&(e, \phi(n)) = 1\\
ed & \ mod \phi(n) = 1, 即 & c & \equiv \texttt{m}^e mod \ n\\
ed & = k\phi(n)+1, k\ge1 & m & \equiv c^d mod \  n\\
dp & = dmod(p-1) \\
x=p^3modn -- p= \sqrt[3]{x+kn} \\

(a*b)^e \% n = ((a^e \% n) * (b^e \% n)) \% n
\end{align}
$$

欧拉定理: 正整数a和n互质，则：

$$
a ^{\phi (n)} \equiv 1(mod \ n) \\
{\phi (a*b)} = \phi (a) * \phi(b) \\
$$

费马小定理: 假设正整数a与质数p互质，因为质数p的$\phi (n)$等于p-1, 则欧拉定理可以写成

$$
p为质数时 \phi(p) = p - 1 \\
a ^ {p-1} \equiv 1(mod \ p)
$$

### 模反元素/模逆元

a和n互质，那么一定可以找到整数b，使得 ab-1 被n整除，或者说ab被n除的余数是1。b就叫做a的"模反元素"。

$$
ab \equiv 1(mod \ n) \\
b = a^{-1} (mod \ n)
$$

b+kn 都是a的模反元素。 欧拉定理可证
$$
a ^ {\phi (n)} = a * a ^ {\phi (n) -1} \equiv 1(mod \ n)
$$

$\delta$

### 中国剩余定理
[(Chinese Remainder Theorem, CRT)](https://baike.baidu.com/item/%E5%AD%99%E5%AD%90%E5%AE%9A%E7%90%86/2841597)
[不懂看视频](https://www.bilibili.com/video/BV1AX4y137hi?from=search&seid=14799670217776478290)

https://code.felinae98.cn/CTF/Crypto/RSA%E5%A4%A7%E7%A4%BC%E5%8C%85%EF%BC%88%E4%B8%89%EF%BC%89%E4%BD%8E%E8%A7%A3%E5%AF%86%E6%8C%87%E6%95%B0%E6%94%BB%E5%87%BB%E3%80%81%E5%85%B1%E6%A8%A1%E6%94%BB%E5%87%BB%E3%80%81%E4%BD%8E%E8%A7%A3%E5%AF%86%E6%8C%87%E6%95%B0%E5%B9%BF%E6%92%AD%E6%94%BB%E5%87%BB/

[脚本 ](https://blog.csdn.net/xuqi7/article/details/75578414)

$$
\left\{
\begin{array}{c}

x \equiv a_1(mod3) \\
x \equiv a_2(mod5) \\
x \equiv a_3(mod7) \\
\end{array}
\right. \\
通解为 x = 70a_1 + 21a_2 + 15a_3(mod \ 105)
$$

$$
\begin{equation}
(S)
:
\left\{
\begin{array}{c}
    x\equiv a_1(mod \ m_1) \\
    x\equiv a_2(mod \ m_2) \\
    \vdots \\
    x\equiv a_n(mod \ m_n)
\end{array}
\right.
\end{equation}
$$

$$
\begin{equation*}
x = \sum_{i=1}^Ka_i \frac{M}{mi} (\frac{M}{m_i})^{-1}(mod \ m_i) (mod \ M)
\end{equation*}
$$

$a_i$是第i项的余数
$M^{-1}$是$M_i$的逆元 , $M_iM^{-1}_i \equiv 1(mod \ mi) \\$
$M = m_1*m_2*...*m_n$
$M_i = m_1*m_2*...*m_n / m_i$

---

$$
m \equiv C^d(mod \ pq) \\
中国剩余定理解法： \\
C^d \equiv m_1(mod \ p) => m_1 \equiv C^{d(mod \ p-1)}(mod \ p) \\
C^d \equiv m_2(mod \ q) => m_2 \equiv C^{d(mod \ q-1)}(mod \ q) \\
m = m_1qp^{-1}(modq) + m_2pq^{-1}(modp)(mod \ pq)
$$
注意有时会遇到转化，注意 $gcd(e, \phi n) !=1 $时记得转化
$$
m^{14} = c_1 mod \ q_1 \\
m^{14} = c_2 mod \ q_2 \\
转化为 m^{14} = c_3 mod \ (q_1*q_2) \\
这里 14和 \phi (q_1q_2) gcd为2, 所以 \\
m^{(2)7}= c_3 mod \ (q_1*q_2)
$$


### 阶乘取模 -- 威尔逊定理

RoarCTF2019 babyRSA

https://www.cnblogs.com/lipu123/p/13961694.html

p为质数
$(p-1)! \equiv -1(mod \ p)$

Q P, P是输入的素数，Q为小于P的第一个素数
$$
\begin{multline}
\shoveleft
\begin{aligned}
    & (Q-1)!mod \ P = -1 ==> [(P-1)! mod \ P] == P-1 \\
    & Q!*(Q+1)*(Q+2)...(P-1) == (P-1)! \\ 
    & Q!(mod \ P) == (P-1)! / [(Q+1)*(Q+2)*(Q+3)...(P-1)](mod \ P) \\
    & Q!(mod \ P) == (P-1) / (Q+1)*(Q+2)*(Q+3)...(P-1)(mod \ P)
\end{aligned}
\end{multline}
$$

### e和Φ(n)有公因数、即不互素时
https://blog.csdn.net/chenzzhenguo/article/details/94339659

$$
\begin{multline}
\shoveleft
\begin{aligned}
& gcd(e,\phi(n))=b \\
& ed \equiv 1mod \phi(n)  \\
& e = a*b \\ 
& abd \equiv 1mod \phi(n) \\
& c \equiv  m^e \ mod \ n => \ \ m^{ab} \equiv c\ mod \ n \\
& c^{bd} \equiv m^{abbd} \equiv m^b mod \ n \\
& bd = gmpy2.invert(a,\phi (n)) \\
& m^b = gmpy2.invert(c^{bd},\phi (n))
\end{aligned}
\end{multline}
$$

另一种做法

$$
\begin{multline}
\shoveleft
\begin{aligned}
& gcd(e, \phi (n) )=14 \\
& c1=m^{e} \ \% n = (m^{14})^{\frac e{14}} \ \% n \\
& gcd为14, e/14和 \phi (n) 互素
\end{aligned}
\end{multline}
$$




### 常见题型

#### pq相近

yafu分解。比如
```
p = getPrime(1024)
q = gmpy2.next_prime(p)
```


$$
\begin{multline}
\shoveleft
\begin{aligned}
& n1 = p * q1 \\
& m^{14} ☰c1^{d1}mod \ n1 \\
& m^{14} ☰c1^{d1}mod \ (p * q1) \\
\end{aligned}
\end{multline}
$$


### ecc

$$
\begin{multline}
\shoveleft
\begin{aligned}
& y^2 \equiv x^3 + a*x + b mod \  ecc\_prime \\
& 这里p对应x, q对应y \\
& q^2 \equiv p^3 + a*p + b \ mod \ ecc\_prime \\ 
& p^2 * q^2 \equiv (p^3+a*p+b) * p^2 \  mod \ ecc\_prime \\
& n^2 \equiv (p^3 + a*p + b) *p^2 \  mod \ ecc\_prime \\
& 0  \equiv (p^3 + a*p + b) *p^2 - n^2 \  mod \ ecc\_prime \\
\end{aligned}
\end{multline}
$$

### 连分数
[羊城杯 2020]RRRRRRRSA

$$
\huge \frac {1473}{50} = 29 + \frac {1}{ 2 + \frac 1 {5  + \frac 1 {1 + \frac 1 3}}}
$$

当p,q很大时,phi和n是接近的,1/(dphi)很小,说明e/phi 和k/d 很接近,这里phi可以近似看成n.
于是e/n 和k/d 很接近.
当e很大时,通过对e/n进行连分数展开,然后对每一项求其渐进分数,通过遍历渐进分数k/d很有可能就被e/n的众多项渐进分数中的一项所覆盖,假设覆盖它的是k1/d1,那么k1=k ; d1=d.这里可能会有疑问,如果gcd(k,d)!=1 那么对于最简的k1/d1来说是否应该存在t使得tk1=k td1=d 呢? 但其实这里 gcd(k,d)一定为1即k,d一定互质.

### 离散对数

[网鼎杯2020青龙组] you_raise_me_up

$ c= m^{bytes\_to\_long(flag)} mod \ n$



### 有限域 - 二次剩余

https://zhuanlan.zhihu.com/p/262542340
https://www.bilibili.com/read/cv2922069/
有限域通常称为伽罗瓦域(Galois Fields)，记为GF(pⁿ)。密码学中，最常用的域是GF(2ⁿ)。

二次剩余
https://www.youtube.com/watch?v=MEGSCV5PJAc

$X^2 \equiv d \ (mod \ p)$ 
有解，则 <font color='red'>d</font> 是模 p的二次剩余

欧拉准则
$d^{\frac {p-1}2} \equiv 1 (mod \ p)$ 当且仅当d是模p的二次剩余

###  Coppersmith相关攻击
https://www.cnblogs.com/coming1890/p/13506057.html

明文高位泄露
因子低位泄露：
明文低位泄露
因子低位泄露



$$
计算 \(x^{{2006}} \pmod {{x^3 + 7}}\) 在里面 \(GF(97)[x]\) ，我们创建商环 \(GF(97)[x]/(x^3+7)\) ，然后计算 \(x^{{2006}}\) 在里面。作为一个Sage的标记，我们必须区分 \(x\) 在里面 \(GF(97)[x]\) 以及相应的元素（我们用 \(a\) )在商环中 \(GF(97)[x]/(x^3+7)\) .$
$$
### Franklin-Reiter attack, 同n同e, m和m+r
### boneh_durfee d<N^0.270



### 其他

#### [TSG CTF 2020：Beginner‘s Crypto](https://github.com/tsg-ut/tsgctf2020/tree/master/crypto/beginners_crypto) 

```python
assert(len(open('flag.txt', 'rb').read()) <= 50)
assert(str(int.from_bytes(open('flag.txt', 'rb').read(), byteorder='big') << 10000).endswith('1002773875431658367671665822006771085816631054109509173556585546508965236428620487083647585179992085437922318783218149808537210712780660412301729655917441546549321914516504576'))
```

https://zhuanlan.zhihu.com/p/363648238

https://blog.csdn.net/song_lee/article/details/107498149

1.明文 $m < 2^{8 * 50}$​

2.$m * 2^{100000} $ , 10进制的后175位为c,  -- endwith后为10进制的175长度

$ m \ mod \ 2^k $ 不行，gcd(10, 2)不为1 ，分析$m \ mod \ 5^k$

$ m \equiv 2^{-10000}c(mod5^{175}) $

又范围限制 $ m < 2^{400}< 5^{175} $
所以 $ m = 2^{-10000} c mod \ 5^{175}$


```python
s_shift = 1002773875431658367671665822006771085816631054109509173556585546508965236428620487083647585179992085437922318783218149808537210712780660412301729655917441546549321914516504576
len_s = 175
five_power = 5 ** len_s

from Crypto.Util.number import *
import gmpy2

s = s_shift * gmpy2.powmod(2, -10000, five_power) % five_power

print(s)
print(long_to_bytes(s))
print(2**400 - 5**175)
```

#### 同n同e,多组m和c, 可求n

$$
\left\{
\begin{array}{rcl}
m_1^e\%(p*q)  = c_1 \\
m_2^e\%(p*q)  = c_2 \\
\end{array}
\right. \\

=>
\left\{
\begin{array}{c}
m_1^e-c_1=k_1*p*q \\
m_2^e-c_2=k_2*p*q \\
\end{array}
\right. \\

=> gcd(m_1^e-c_1,m_2^e-c_2) = p * q = n \\
$$

#### 同p同e,多组m和c, 可求p


$$
\left\{
\begin{array}{rcl}
m_1^e\%(p*q_1)  = c_1 \\
m_2^e\%(p*q_2)  = c_2 \\
\end{array}
\right. \\

=>
\left\{
\begin{array}{c}
m_1^e-c_1=k_1*p*q_1 \\
m_2^e-c_2=k_2*p*q_2 \\
\end{array}
\right. \\

=> gcd(m_1^e-c_1,m_2^e-c_2) = p \\
$$

## sage

```
F.<x> = Zmod(ep)[]  # 定义一个商环, ep是模。
```

将一个多项式分解成两个变量。
```py
sage: R.<x,y> = QQ[]
sage: F = factor(x^99 + y^99)
sage: F
(x + y) * (x^2 - x*y + y^2) * (x^6 - x^3*y^3 + y^6) *
(x^10 - x^9*y + x^8*y^2 - x^7*y^3 + x^6*y^4 - x^5*y^5 +
 x^4*y^6 - x^3*y^7 + x^2*y^8 - x*y^9 + y^10) *
(x^20 + x^19*y - x^17*y^3 - x^16*y^4 + x^14*y^6 + x^13*y^7 -
 x^11*y^9 - x^10*y^10 - x^9*y^11 + x^7*y^13 + x^6*y^14 -
 x^4*y^16 - x^3*y^17 + x*y^19 + y^20) * (x^60 + x^57*y^3 -
 x^51*y^9 - x^48*y^12 + x^42*y^18 + x^39*y^21 - x^33*y^27 -
 x^30*y^30 - x^27*y^33 + x^21*y^39 + x^18*y^42 - x^12*y^48 -
 x^9*y^51 + x^3*y^57 + y^60)
sage: F.expand()
x^99 + y^99
```



