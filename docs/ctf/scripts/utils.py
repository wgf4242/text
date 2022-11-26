import struct

import numpy as np
from Crypto.Util.number import long_to_bytes, bytes_to_long


def bytes_to_4lst(a: list) -> list:
    b = bytes(a)
    lst = []
    for i in range(0, len(b), 4):
        unpack = struct.unpack('<I', b[i: i + 4])[0]
        # print(i_)
        lst.append(unpack)
    return lst


def rotate_left(x, n):
    return int(f"{x:032b}"[n:] + f"{x:032b}"[:n], 2)


def rotate_right(x, n):
    return int(f"{x:032b}"[-n:] + f"{x:032b}"[:-n], 2)


def rotate_left_str(txt, n):
    return txt[n:] + txt[:n]


def rotate_right_str(txt, n):
    return txt[-n:] + txt[:-n]


rol = lambda val, r_bits, max_bits: \
    (val << r_bits % max_bits) & (2 ** max_bits - 1) | \
    ((val & (2 ** max_bits - 1)) >> (max_bits - (r_bits % max_bits)))

# Rotate right: 0b1001 --> 0b1100
ror = lambda val, r_bits, max_bits: \
    ((val & (2 ** max_bits - 1)) >> r_bits % max_bits) | \
    (val << (max_bits - (r_bits % max_bits)) & (2 ** max_bits - 1))


# rol int bytes
def rol_int(v: int):
    b = long_to_bytes(v).rjust(4, b'\0')
    # [0, 61, 51, 51] => [61, 51, 51, 0]
    rev = b[1:] + b[:1]
    return bytes_to_long(rev)


# generate_lorum(8)
# generate_lorum(32, 'b')
def generate_lorum(n: int, c='a'):
    round = n // 4
    for i in range(round):
        print(3 * c + str(i), end='')
    print()


def swap_l4_h4_todigit(file):
    # swap low 4 bit, high 4 bit
    ar = np.fromfile(file, dtype='uint8')
    b1 = (ar & 0xf0) >> 4
    b2 = (ar & 0xf)<< 4
    ar2 = b1 + b2
    ar2.tofile('out')

if __name__ == '__main__':
    a = [20, 105, 41, 173, 62, 178, 75, 159, 182, 170, 33, 91, 46, 230, 57, 64, 234, 134, 33, 151, 82, 198, 52, 227]
    o = bytes_to_4lst(a)
    print(o)
