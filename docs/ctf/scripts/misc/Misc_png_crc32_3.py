# -*- coding: utf-8 -*-
import binascii
import struct

f = open('flag.png', 'rb').read()

crc_buffer = f[0x1d:0x21]
crc32key = struct.unpack('>I', crc_buffer)[0]

for i in range(0, 65535):
    height = struct.pack('>i', i)
    data = f[0xc:0x14] + height + b'\x08\x06\x00\x00\x00'
    crc32result = binascii.crc32(data) & 0xffffffff
    if crc32result == crc32key:
        print(''.join(map(lambda c: "%02X" % c, height)))
