"""
# https://xz.aliyun.com/t/4630
# 2018 CISCN 初赛 oldstreamgame
flag = "flag{xxxxxxxxxxxxxxxx}"
assert flag.startswith("flag{")
assert flag.endswith("}")
assert len(flag)==14

def lfsr(R,mask):
    output = (R << 1) & 0xffffffff #将R左移一位然后保留低32位，赋值给output
    i=(R&mask)&0xffffffff #R和mask做与运算，然后保留低32位赋值给i
    lastbit=0
    while i!=0:
        lastbit^=(i&1)
        i=i>>1 #让lastbit依次和i的每一位异或，然后赋值给lastbit
    output^=lastbit
    return (output,lastbit)

R=int(flag[5:-1],16)
mask = 0b10100100000010000000100010010100

f=open("key","w")
for i in range(100):
    tmp=0
    for j in range(8):
        (R,out)=lfsr(R,mask)
        tmp=(tmp << 1)^out
    f.write(chr(tmp))
f.close()
"""


def solve1():
    mask = 0b10100100000010000000100010010100
    N = 32
    # b = open('key', 'rb').read()
    b = bytes.fromhex('20FDEEF8A4C9F4083F331DA8238AE5ED083DF0CB0E7A83355696345DF44D7C186C1F459BCE135F1DB6C76775D5DCBAB7A783E48A203C19CA25C22F60AE62B37DE8E40578E3A7787EB429730D95C9E1944288EB3E2E747D8216A4785507A137B413CD690C')
    key = ''
    for i in range(N // 8):
        t = b[i]
        for j in range(7, -1, -1):
            key += str(t >> j & 1)
    idx = 0
    ans = ""
    key = key[31] + key[:32]
    while idx < 32:
        tmp = 0
        for i in range(32):
            if mask >> i & 1:
                tmp ^= int(key[31 - i])
        ans = str(tmp) + ans
        idx += 1
        key = key[31] + str(tmp) + key[1:31]
    num = int(ans, 2)
    print(hex(num))

def solve2():
    mask = 0b10100100000010000000100010010100

    N = 32
    F = GF(2)

    b = bytes.fromhex('20FDEEF8A4C9F4083F331DA8238AE5ED083DF0CB0E7A83355696345DF44D7C186C1F459BCE135F1DB6C76775D5DCBAB7A783E48A203C19CA25C22F60AE62B37DE8E40578E3A7787EB429730D95C9E1944288EB3E2E747D8216A4785507A137B413CD690C')

    R = [vector(F, N) for i in range(N)]
    for i in range(N):
        R[i][N - 1] = mask >> (31 - i) & 1
    for i in range(N - 1):
        R[i + 1][i] = 1
    M = Matrix(F, R)
    M = M ^ N

    vec = vector(F, N)
    row = 0
    for i in range(N / 8):
        t = b[i]
        for j in range(7, -1, -1):
            vec[row] = t >> j & 1
            row += 1
    print(rank(M))
    num = int(''.join(map(str, list(M.solve_left(vec)))), 2)
    print(hex(num))

if __name__ == '__main__':
    solve1()
