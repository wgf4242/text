import os
import binascii
import struct


misc = open("flag.png","rb").read()

for i in range(1024):
    data = misc[12:16] + struct.pack('>i',i)+ misc[20:29]
    crc_block = misc[29:33]
    crc32 = struct.unpack('>I', crc_block)[0]
    if binascii.crc32(data) & 0xffffffff == crc32:
        print( i)