# CISCN2023 国粹 a.png k.png 题目.png
from PIL import Image

# 2279 x 146 = (53 x (73 x 2)) * 42  -- 53 x 73 图片2行 每行 42张图片
# 题目中保存了 42 x 2 张图片，每张图片大小为 53 * 73,
ew, eh = 53, 73
table_pic = Image.open('题目.png')
ti_w, ti_h = table_pic.size
color = [0] * 42

for i in range(1, 43):
    pic = []
    for y in range(eh):
        for x in range(ew):
            pic.append(table_pic.getpixel((53 * i + x, y))[0])
    color[i - 1] = pic

k_pic = Image.open('k.png')
k_w, k_h = k_pic.size
flag_ind = []
for i in range(k_w // 53):
    pic = []
    for y in range(eh):
        for x in range(ew):
            pic.append(k_pic.getpixel((53 * i + x, y))[0])
    ind = color.index(pic)
    flag_ind.append(ind)

a_pic = Image.open('a.png')
a_w, a_h = a_pic.size
a_ind = []
for i in range(a_w // 53):
    pic = []
    for y in range(eh):
        for x in range(ew):
            pic.append(a_pic.getpixel((53 * i + x, y))[0])
    ind = color.index(pic)
    a_ind.append(ind)

new_pic = Image.new('L', (42, 42), 255)
for i in range(len(a_ind)):
    new_pic.putpixel((flag_ind[i], a_ind[i]), 0)
new_pic.show()
