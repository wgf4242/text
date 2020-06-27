# 栅栏 W型加密 rail fence
def fence(lst, numrails):
    fence = [[None] * len(lst) for n in range(numrails)]
    rails = [*range(numrails - 1), *range(numrails - 1, 0, -1)]
    for n, x in enumerate(lst):
        fence[rails[n % len(rails)]][n] = x

    if 0:  # debug
        for rail in fence:
            print(''.join('.' if c is None else str(c) for c in rail))

    return [c for rail in fence for c in rail if c is not None]


def encode(text, n):
    return ''.join(fence(text, n))


def decode(text, n):
    rng = range(len(text))
    pos = fence(rng, n)
    return ''.join(text[pos.index(n)] for n in rng)


z = encode('ATTACK.AT.DAWN', 3)
print(z)  # ACTWTAKA.ANT.D
# y = decode(z, 3)
# print(y)  # ATTACK.AT.DAWN
for i in range(2, 10):
    print(decode(z, i))
