from threading import Thread
import os
from time import sleep

import gmpy2

yafu_path = r'F:\downloads\网络课程\@网络安全攻防相关\900.Tools\【渗透测试工具包AIO201811】\0x08CTF-AWD\RSA\RSA大整数分解\yafu-1.34\yafu-x64.exe'

# Get prime
# import libnum
# libnum.generate_prime(128)
# from Crypto.Util.number import getPrime
# getPrime()

def n_is_prime(n):
    if not all([n]):
        return
    if gmpy2.is_prime(n):
        print('n is prime, phi is n - 1')

def nc_are_prime(n, c):
    if not all([n, c]):
        return
    gcd = gmpy2.gcd(n, c)
    if gcd != 1:
        print('n, c not prime, gcd is ', gcd)


def ephi_not_prime(e, phi):
    if not all([e, phi]):
        return
    r = gmpy2.invert(e, phi)
    if r != 1:
        print('e, phi not prime')


def check_crt(m, n):
    if not all([n, m]):
        return
    if m > n:
        print('m > n, try crt')


def factor(N):
    if not N:
        return
    cmd = f"{yafu_path} factor({N})"
    cmd2 = f'start cmd /k {cmd}'
    os.system(cmd2)


def is_prime(x):
    if not x:
        return

    import inspect
    frame = inspect.currentframe()
    frame = inspect.getouterframes(frame)[1]
    string = inspect.getframeinfo(frame[0]).code_context[0].strip()
    args = string[string.find('(') + 1:-1].split(',')

    names = []
    for i in args:
        if i.find('=') != -1:
            names.append(i.split('=')[1].strip())

        else:
            names.append(i)

    print(names, 'is_prime=', gmpy2.is_prime(x))


def is_prime(x):
    if not x:
        return

    def get_varname():
        import inspect
        frame = inspect.currentframe()
        frame = inspect.getouterframes(frame)[2]
        string = inspect.getframeinfo(frame[0]).code_context[0].strip()
        args = string[string.find('(') + 1:-1].split(',')

        names = []
        for i in args:
            if i.find('=') != -1:
                names.append(i.split('=')[1].strip())

            else:
                names.append(i)
        return names

    names = get_varname()
    print(names, 'is_prime =', gmpy2.is_prime(x))



def isqrt(n):
  x = n
  y = (x + n // x) // 2
  while y < x:
    x = y
    y = (x + n // x) // 2
  return x

def fermat(n, verbose=True):
    a = isqrt(n) # int(ceil(n**0.5))
    b2 = a*a - n
    b = isqrt(n) # int(b2**0.5)
    count = 0
    while b*b != b2:
        # if verbose:
        #     print('Trying: a=%s b2=%s b=%s' % (a, b2, b))
        a = a + 1
        b2 = a*a - n
        b = isqrt(b2) # int(b2**0.5)
        count += 1
    p=a+b
    q=a-b
    assert n == p * q
    # print('a=',a)
    # print('b=',b)
    print('p=',p)
    print('q=',q)
    # print('pq=',p*q)
    return p, q


def fermat_run():
    t1 = Thread(target=fermat, args=(n,))
    t1.daemon = True
    t1.start()
    sleep(0.5)
    print('t1 start')
    t1.join(timeout=3)


if __name__ == '__main__':
    m = ""
    n = ""
    c = ""
    p = ""
    q = ""
    e = ""
    phi = ""
    n = 161670795418661108941395547760068053355832555077779027853700140442876298077926786030806243269042521234383793929910836023913994987010924339006536693866763078849189869497871752489277315727669547511079303136326388638480680630822677173084810848784554433394382029956739707395702556105138001868786944077871569844771

    # fermat(n)
    n_is_prime(n)
    nc_are_prime(n, c)
    check_crt(m, n)
    ephi_not_prime(e, phi)
    # factor(n)
    # factor(p)
    # factor(q)
    is_prime(p)
    is_prime(q)
    is_prime(e)
    is_prime(c)
    fermat_run()



