# 方法不对再研究下
# 0b0000011 隐写时
# 每个像素 lst.append(r & 0b00000001) 然后 lst.append(r & 0b00000010) 见 Misc_steg_lsb_extract.0b00000011

from PIL import Image

pic = Image.open("mmm.png")  # type: Image.Image
pic = pic.convert('RGB')
width, height = pic.size
lst = []
f = ''
res = ''
for x in range(width):
    for y in range(height): # 先扫描行, 行在内层
        pixel = pic.getpixel((x, y))
        r,g,b = pixel
        if r & 0b00000001:
            f += '1'
        else :
            f += '0'
        if r & 0b00000010:
            f += '1'
        else :
            f += '0'
        if len(f) == 8:
            res += chr(int(f, 2))
            f = ''
        lst.extend(pixel)
# print(res)
open("0b00000011", 'wb').write(res.encode())