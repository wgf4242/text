def willson(A, B):
    tmp = 1
    for i in range(B + 1, A - 1):
        tmp *= i
        tmp %= A
    factorial = gmpy2.invert(tmp, A)
    return factorial

