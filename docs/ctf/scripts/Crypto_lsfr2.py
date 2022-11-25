"""
# https://blog.csdn.net/m0_62506844/article/details/124378089
#  2018 强网杯 streamgame1
from flag import flag
assert flag.startswith("flag{")
assert flag.endswith("}")
assert len(flag)==25

def lfsr(R,mask):
    output = (R << 1) & 0xffffff
    i=(R&mask)&0xffffff
    lastbit=0
    while i!=0:
        lastbit^=(i&1)
        i=i>>1
    output^=lastbit
    return (output,lastbit)



R=int(flag[5:-1],2)
mask    =   0b1010011000100011100

f=open("key","ab")
for i in range(12):
    tmp=0
    for j in range(8):
        (R,out)=lfsr(R,mask)
        tmp=(tmp << 1)^out
    f.write(chr(tmp))
f.close()
"""


def solve1():
    global tmp
    mask = 0b1010011000100011100

    def lfsr(R, mask):
        output = (R << 1) & 0xffffff
        i = (R & mask) & 0xffffff
        lastbit = 0
        while i != 0:
            lastbit ^= (i & 1)
            i = i >> 1
        output ^= lastbit
        return (output, lastbit)

    key = [85, 56, 247, 66, 193, 13, 178, 199, 237, 224, 36, 58]
    for R in range(2 ** 19):
        judge = 0
        for i in range(12):
            tmp = 0
            for j in range(8):
                (R, out) = lfsr(R, mask)
                tmp = (tmp << 1) ^ out
            if key[i] != tmp:
                judge = 1
                break
        if judge == 0:
            print(bin(R)[2:])
            break


def solve2():
    mask = '1010011000100011100'  # 顺序 c_n,c_n-1,。。。,c_1
    key = '0101010100111000111'
    R = ''
    for i in range(19):
        output = 'x' + key[:18]  # 我们就是要求这个x
        out = int(key[-1]) ^ int(output[-3]) ^ int(output[-4]) ^ int(output[-5]) ^ int(output[-9]) ^ int(output[-13]) ^ int(output[-14]) ^ int(output[-17])
        R += str(out)
        key = str(out) + key[:18]
    print('flag{' + R[::-1] + '}')


if __name__ == '__main__':
    # solve1()
    solve2()
