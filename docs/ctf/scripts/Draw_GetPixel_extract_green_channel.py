# 每10像素读一次
from PIL import Image

pic = Image.open("cipher.bmp")  # type: Image.Image
pic = pic.convert('RGB')
width, height = pic.size
lst = []
lr, lg, lb = [], [], []
for y in range(0, height):
    for x in range(0, width):  # 放大图片看一格子是10x10像素
        pixel = pic.getpixel((x, y))
        print(pixel)
        #         if pixel == (255, 255, 255):
        #             continue
        r, g, b = pixel
        lr.append(r)
        lg.append(g)
        lb.append(b)
        lst.extend(pixel)
print(lst)
#         # print(pixel)
#         lst.extend(pixel)
from collections import Counter

#
# data = ''
# for i in lst:
#     if i == 0: continue
#     if i < 32 or i > 128:
#         continue
#     data += chr(i)
#
# print(data)
#
counter = Counter(lb)
print(counter.most_common())
c2 = Counter(lst)
print(c2.most_common())

import string

for k, count in Counter(lr).most_common():
    print(chr(k), end='')  # key就是前面的  theKEYis:#R@/&p~!
print('\n------\n')

for k, count in Counter(lg).most_common():
    print(chr(k), end='')  # key就是前面的  theKEYis:#R@/&p~!
print('\n------\n')

for k, count in Counter(lb).most_common():
    print(chr(k), end='')  # key就是前面的  theKEYis:#R@/&p~!
print('\n------\n')
