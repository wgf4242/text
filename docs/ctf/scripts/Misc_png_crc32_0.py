import binascii
import struct

with open("flag.png",'rb') as f:
    data = f.read()
    f.close()

crc32key, = struct.unpack(">I",data[29:33]) # struct.pack('>I',w), 将w转成4字节的bytes, >表示大端模式
# > 大端， 数据的高字节，保存在内存的低地址中。 0x1234大端表示为0x34 0x12 小端为 0x12 0x34

for w in range(16,1024):
    for h in range(16,1024):
        
        ihdr = b'IHDR' + struct.pack('>I',w) + struct.pack('>I',h) + data[24:29]
        
        if crc32key == binascii.crc32(ihdr):
            data = data[:12]+ihdr+data[29:]
        # if crc32key == (binascii.crc32(ihdr) & 0xffffffff): # 全平台
            # data = data[:12]+ihdr+data[29:]

with open("out2.png","wb") as f:
    f.write(data)
    f.close()