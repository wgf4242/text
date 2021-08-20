from Crypto.Util.number import *
def CRT(r, d): # r -- alst, d -- mlst
    M = reduce(lambda x, y: x * y, d)
    x = 0
    for re, de in zip(r, d):
        md = M // de
        x = (x + gmpy2.invert(md, de) * md * re) % M
    return int(M + x % M) % M


def CRT2(mi, ai):
    # mi,ai分别表示模数和取模后的值,都为列表结构
    # Chinese Remainder Theorem
    # lcm=lambda x , y:x*y/gcd(x,y)
    # mul=lambda x , y:x*y
    # assert(reduce(mul,mi)==reduce(lcm,mi))
    # 以上可用于保证mi两两互质
    assert (isinstance(mi, list) and isinstance(ai, list))
    M = reduce(lambda x, y: x * y, mi)
    ai_ti_Mi = [a * (M / m) * gmpy2.invert(M / m, m) for (m, a) in zip(mi, ai)]
    return reduce(lambda x, y: x + y, ai_ti_Mi) % M

# 以上程序将mi当作两两互质处理,实际上有时会遇到其他情况，这时就需要逐一两两合并方程组。我参照下图实现了一个互质与不互质两种情况下都能工作良好的中国剩余定理（解同余方程组）的Python程序。

def GCRT(mi, ai):
    # mi,ai分别表示模数和取模后的值,都为列表结构
    assert (isinstance(mi, list) and isinstance(ai, list))
    curm, cura = mi[0], ai[0]
    for (m, a) in zip(mi[1:], ai[1:]):
        d = gmpy2.gcd(curm, m)
        c = a - cura
        assert (c % d == 0) #不成立则不存在解
        K = c / d * gmpy2.invert(curm / d, m / d)
        cura += curm * K
        curm = curm * m / d
    return (cura % curm, curm) #(解,最小公倍数)
