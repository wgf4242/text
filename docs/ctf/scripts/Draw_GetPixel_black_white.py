# 2021 dasctf 10 虚幻3
# 这题提取最低位像素，转化为黑白。但是组合顺序是grb。 本题长宽比为3:1, 进行了处理

from PIL import Image
pic = Image.open('cipher.bmp')
a, b = pic.size
r1 = []  # 储存r、g、b通道
g1 = []
b1 = []
r2 = []  # 一行一行临时储存
g2 = []
b2 = []
for y in range(b):
    for x in range(a):
        r2.append(pic.getpixel((x, y))[0] % 2)
        g2.append(pic.getpixel((x, y))[1] % 2)
        b2.append(pic.getpixel((x, y))[2] % 2)
    r1.append(r2)
    g1.append(g2)
    b1.append(b2)
    r2 = []
    g2 = []
    b2 = []
pic_1 = Image.new('L', (a, b*3), 255)
for y in range(0, len(r1)*3, 3):
    for x in range(len(r1[0])):
        pic_1.putpixel((x, y), g1[y//3][x] * 255)
        pic_1.putpixel((x, y+1), r1[y//3][x] * 255)
        pic_1.putpixel((x, y+2), b1[y//3][x] * 255)
pic_1.show()
# pic_1.save('flag.bmp')
