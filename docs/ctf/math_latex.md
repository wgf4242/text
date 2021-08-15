https://www.jianshu.com/p/a0aa94ef8ab2
https://blog.csdn.net/anscor/article/details/80878285
http://meta.math.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference
https://mirrors.tuna.tsinghua.edu.cn/CTAN/info/lshort/chinese/lshort-zh-cn.pdf

$$
\sum_{n=1}^{100}{a_n}
$$

$\sum_{i=0}^N\int_{a}^{b}g(t,i)\text{d}t$

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
a ^{\phi (n)} \equiv 1(mod \ n)
$$

费马小定理: 假设正整数a与质数p互质，因为质数p的$\phi (n)$等于p-1, 则欧拉定理可以写成

$$
a ^ {p-1} \equiv 1(mod \ p)
$$

### 模反元素

a和n互质，那么一定可以找到整数b，使得 ab-1 被n整除，或者说ab被n除的余数是1。b就叫做a的"模反元素"。

$$
ab \equiv 1(mod \ n)
$$

b+kn 都是a的模反元素。 欧拉定理可证
$$
a ^ {\phi (n)} = a * a ^ {\phi (n) -1} \equiv 1(mod \ n)
$$

$\delta$

### 中国剩余定理
(Chinese Remainder Theorem, CRT


### 常见题型

#### pq相近

yafu分解。比如
```
p = getPrime(1024)
q = gmpy2.next_prime(p)
```
