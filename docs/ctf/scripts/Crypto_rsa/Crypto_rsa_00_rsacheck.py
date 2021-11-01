import os

import gmpy2

yafu_path = r'F:\downloads\网络课程\@网络安全攻防相关\900.Tools\【渗透测试工具包AIO201811】\0x08CTF-AWD\RSA\RSA大整数分解\yafu-1.34\yafu-x64.exe'


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


if __name__ == '__main__':
    m = ""
    n = ""
    c = ""
    p = ""
    q = ""
    e = ""
    phi = ""
    n = 24981188020167643746074879674147956549430370314044132464039253351652835734440674909204189557556602865962429895374385855345228410925147709118740392159925942795088299679655602727568511595072696409696271371250102853677902616206682058248674337676916036346628088795691598346311821772518310067782592432491390315016938601034921878080792576848740835839533436309467949739957366439791446358471180018562594829965668319970676634275599934272794456322929434264075482862354958544593517741073415713467939034524174022554745424038830745700456334054077809280744596235294447559597633491714726093368901810800094506409706555205366712813489
    c = 18621596046506896357501494490427254488179638636182636310535680038609096612801678121484736598560358324455851721295385341142207429201113106822997090878471278518783809844775558184834964034587247425952074737623038780244691628409045326000650516141599732305641793044557982746856322994617259408879266356396616639748741726355064689072113192676869563527139209384310754130692810070548558914951576972545449143198975499766952417464247791425484288188124235662918342094367901287461654602032582020287215884903753469091244847129233355340585693462406329376871222071849218639774125831290704426337294409031337314523781596602940531607723
    e = 65537

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
