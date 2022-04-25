import struct


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



if __name__ == '__main__':
    a = [20, 105, 41, 173, 62, 178, 75, 159, 182, 170, 33, 91, 46, 230, 57, 64, 234, 134, 33, 151, 82, 198, 52, 227]
    o = bytes_to_4lst(a)
    print(o)