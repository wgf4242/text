# 每10像素读一次
from PIL import Image

pic = Image.open("aaaaa.png")  # type: Image.Image
width, height = pic.size
lst = []
for x in range(0, width, 10):  # 放大图片看一格子是10x10像素
    for y in range(0, pic.height, 10):
        pixel = pic.getpixel((x, y))
        if pixel == (255, 255, 255):
            continue
        r, g, b = pixel
        # print(pixel)
        lst.extend(pixel)
from collections import Counter

data = ''
for i in lst:
    if i == 0: continue
    if i < 32 or i > 128:
        continue
    data += chr(i)

print(data)

counter = Counter(data)
for k, count in counter.most_common():
    print(k, end='')  # key就是前面的  theKEYis:#R@/&p~!
