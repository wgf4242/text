import base64


def dec(func):
    def inner(*args, **kwargs):
        try:
            txt, *lst = list(args)
            if type(txt) != bytes:
                txt = txt.encode()
            res = func(txt, **kwargs)
            if isinstance(res, bytes):
                return res.decode('utf8')
            return res
        except:
            r = f'{func.__name__} failed'
            print(r)
            return r

    return inner


@dec
def utf7_d(txt):
    r = txt.decode('utf7')
    print('utf7 is \t\t' + r.decode('utf8'))
    return r


@dec
def base64_d(txt):
    r = base64.b64decode(txt)
    print('base64 is \t\t' + r.decode('utf8'))
    return r


@dec
def base85_d(txt):
    return base64.b85decode(txt)


@dec
def base58_d(txt):
    import base58
    return base58.b58decode(txt)


@dec
def base32_d(txt):
    return base64.b32decode(txt)


@dec
def base16_d(txt):
    return base64.b16decode(txt)


@dec
def rot13_d(txt):
    import codecs
    return codecs.encode(txt.decode(), 'rot_13')


@dec
def rot47_d(txt):
    s = txt.decode()
    x = []
    for i in range(len(s)):
        j = ord(s[i])
        if j >= 33 and j <= 126:
            x.append(chr(33 + ((j + 14) % 94)))
        else:
            x.append(s[i])
    return ''.join(x)


@dec
def rot18_d(txt):
    ROT18 = str.maketrans(
        "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz0123456789",
        "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm5678901234",
    )
    return txt.decode().translate(ROT18)


@dec
def base62_d(txt):
    import os
    stdout = os.popen(f"node Crypto_base62.js {txt.decode()}").read()  # 执行并输出命令的执行结果
    return stdout.strip('\n')


if __name__ == "__main__":
    txt = 'MTIzNA=='
    # utf7(txt)
    # base64(txt)
