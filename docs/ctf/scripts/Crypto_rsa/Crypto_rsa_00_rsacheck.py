
import gmpy2
def nc_are_prime(n ,c):
    if not n:
        return
    gcd = gmpy2.gcd(n,c)
    if gcd != 1:
        print('n, c not prime, gcd is ', gcd)

def check_crt(m, n):
    if not n:
        return
    if m > n:
        print('m > n, try crt')

if __name__ == '__main__':
    m = ''
    n = ''
    c = ''

    nc_are_prime(n,c)
    check_crt(m, n)