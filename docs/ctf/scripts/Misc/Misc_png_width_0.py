# -*- coding: utf-8 -*-
import binascii
import struct

f = open('flag.png', 'rb').read()

crc_buffer = f[0x1d:0x21]
crc32key = struct.unpack('>I', crc_buffer)[0]

for i in range(0, 20000):
    height = struct.pack('>i', i)
    data = f[0xc:0x14] + height + f[0x18:0x18+5]
    crc32result = binascii.crc32(data) & 0xffffffff
    if crc32result == crc32key:
        bdata = f[:0x14] + height + f[0x18:]
        out = open('fix_flag.png', 'wb')
        out.write(bdata)
        out.close()
        print('end')
        # print(''.join(map(lambda c: "%02X" % c, height)))
        exit(0)
