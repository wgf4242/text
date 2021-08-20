https://www.jianshu.com/p/a0aa94ef8ab2
https://blog.csdn.net/anscor/article/details/80878285
http://meta.math.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference
https://mirrors.tuna.tsinghua.edu.cn/CTAN/info/lshort/chinese/lshort-zh-cn.pdf

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
x=p^3modn -- p= \sqrt[3]{x+kn}
\end{align}
$$

欧拉定理: 正整数a和n互质，则：

$$
a ^{\phi (n)} \equiv 1(mod \ n) \\
{\phi (a*b)} = \phi (a) * \phi(b) \\
$$

费马小定理: 假设正整数a与质数p互质，因为质数p的$\phi (n)$等于p-1, 则欧拉定理可以写成

$$
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
& c1=m^{e} \ \% n = (m^{14})^{e/14} \ \% n \\
& gcd为14, e/14和 \phi (n) 互素
\end{aligned}
\end{multline}
$$

另一种做法


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



###  Coppersmith相关攻击
https://www.cnblogs.com/coming1890/p/13506057.html

明文高位泄露
因子低位泄露：
明文低位泄露
因子低位泄露
