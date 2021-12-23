import binascii

f = open('out.txt', 'r')

r = ''
for l in f.read().splitlines():
    b = f'{int(l):08b}'
    r += b[:2]

n = int(r, 2)
print(binascii.unhexlify('%x' % n))
