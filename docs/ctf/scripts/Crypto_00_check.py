from base64 import b64decode


def dec(func):
    def inner(*args, **kwargs):
        try:
            txt, *lst = list(args)
            if type(txt) != bytes:
                txt = txt.encode()
            func(txt, **kwargs)
        except:
            print(f'{func.__name__} failed')

    return inner


@dec
def utf7(txt):
    print('utf7 is \t\t', txt.decode('utf7'))

@dec
def base64(txt):
    print('base64 is \t\t', b64decode(txt))


if __name__ == "__main__":
    txt = 'MTIzNA=='
    utf7(txt)
    base64(txt)
