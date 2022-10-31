"""
将伪加密 zip 恢复加密位
Usage:
    python secret.zip
"""

import sys

file = sys.argv[1]
f = open(file, 'rb').read()
f = bytearray(f)


def decrypt_all():
    add_flag('504b0304', 6) # record block
    add_flag('504b0102', 8) # dirty block
    open('output.zip', 'wb').write(f)


def add_flag(header, offset):
    pk_idx = -1
    while (pk_idx := f.find(bytes.fromhex(header), pk_idx + 1)) > -1:
        enc_flag_idx = pk_idx + offset
        f[enc_flag_idx] = 9


decrypt_all()
