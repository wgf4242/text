# RSA求d值
# 扩展欧几里得算法
# 快速幂模算法

def extendedGCD(a, b):
    #a*xi + b*yi = ri
    if b == 0:         
        return 1, 0, a     
    else:         
        x, y, q = extendedGCD(b, a % b) 
        # q = gcd(a, b) = gcd(b, a%b)         
        x, y = y, (x - (a // b) * y)         
        return x, y, q

 
def computeD(fn, e):
    (x, y, r) = extendedGCD(fn, e)
    #y maybe < 0, so convert it
    if y < 0:
        return fn + y
    return y


def fastExpMod(b,e,c):
    result = 1
    while e != 0:
        if (e & 1) == 1:
            result = (result * b) % c
        e >>= 1
        b = (b * b ) % c
    return result