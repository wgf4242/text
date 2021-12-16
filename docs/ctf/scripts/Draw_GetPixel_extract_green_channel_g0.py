from PIL import Image
import struct
pic = Image.open('x.png')
pic = pic.convert("RGB") # 转成RGB再像素对比

a, b = pic.size
img = Image.new("RGB", pic.size, color=(255, 255, 255))  # default black
black = (0,0,0)
white = (255,255,255)
for y in range(b):
    for x in range(a):
        g = pic.getpixel((x, y))[1]
        # 255一共是8位, 和每一位做与运算为1放白色，否则放黑色
        # 对应的 stegsovle green channel 0, 如果√第1位则 0b00000010
        if g & 0b000001: 
            img.putpixel((x, y), white)
        else:
            img.putpixel((x, y), black)

img.save('ff.png')
# img.show()
