import gmpy2, string
enc = 'welcylk'
k1 = 11
k2 = 6
mod = 26
flag = ''

for i in enc:
    if i in string.ascii_lowercase:
        a = ord(i) - 97
        inv = gmpy2.invert(k1, mod)
        flag += chr(((a-k2)*inv) % mod + 97)
        print(flag)
    else:
        flag += i
        print(flag)