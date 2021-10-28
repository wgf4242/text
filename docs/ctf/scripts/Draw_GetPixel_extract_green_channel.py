# 每10像素读一次
from PIL import Image
import struct
pic = Image.open('C:\\Users\\34603\\Desktop\\flag2.bmp')
a, b = pic.size
fp = open('C:\\Users\\34603\\Desktop\\flag.zip', 'wb')
for y in range(b):
    for x in range(a):
        g = pic.getpixel((x, y))[1]
        data = struct.pack('B', g & 0xff)
        # print(data)
        fp.write(data)
fp.close()
