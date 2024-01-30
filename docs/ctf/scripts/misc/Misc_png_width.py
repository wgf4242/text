# CRC给的值有错误时，可能要宽度爆破。有时要宽高一起爆
import binascii
import os
import struct

from Cryptodome.Util.number import long_to_bytes

p = open('flag.png', 'rb').read()
# print(p[0x14:0x17]+chr(0xaf).encode()[-1:])
count = 0
height, = struct.unpack('>I', p[0x14:0x18])
folder = 'te2/'
if not os.path.exists(folder):
    os.mkdir(folder)

for width in range(1, 300):
    data = p[:0x10] + width.to_bytes(4, 'big') + height.to_bytes(4, 'big') + p[0x18:0x1d]
    p2 = data + long_to_bytes(binascii.crc32(data[0xc:0x1d]) & 0xffffffff) + p[0x21:]
    p1 = open(folder + str(count) + '.png', 'wb')
    count += 1
    p1.write(p2)
    p1.close()
