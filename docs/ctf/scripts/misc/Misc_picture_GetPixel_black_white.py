# 2021 dasctf 10 虚幻3
# 这题提取最低位像素，转化为黑白。但是组合顺序是grb。 本题长宽比为3:1, 进行了处理

from PIL import Image

pic = Image.open('cipher.bmp')
a, b = pic.size
pic_flag = Image.new('L', (a, b * 3), 255)
list_r = []
list_g = []
list_b = []
for y in range(b):
    for x in range(a):
        list_r.append(pic.getpixel((x, y))[0] % 2)
        list_g.append(pic.getpixel((x, y))[1] % 2)
        list_b.append(pic.getpixel((x, y))[2] % 2)
i = 0
for y in range(0, 3 * b, 3):
    for x in range(a):
        pic_flag.putpixel((x, y), list_g[i] * 255)
        pic_flag.putpixel((x, y + 1), list_r[i] * 255)
        pic_flag.putpixel((x, y + 2), list_b[i] * 255)
        i += 1
pic_flag.show()
pic_flag.save('flag.bmp')
