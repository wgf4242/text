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
