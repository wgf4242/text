"""
xy.txt
-629 -93
-638 -84
"""

from PIL import Image
import math


def draw(img: Image.Image, x, y):
    for i in range(10):
        for j in range(10):
            img.putpixel((x + i, y + j), (0, 0, 0))


img = Image.new("RGB", (2048, 2048), color=(255, 255, 255))  # 255 255 255 白
lst = open("xy.txt", 'r').read().split('\n')
for line in lst:
    if not line:
        continue
    x, y = line.split(' ')
    x, y = int(x), int(y)
    x, y = x + 1000, y + 1000
    draw(img, x, y)
    # img.putpixel((x, y), (0, 0, 0))

img.save('gogo.png')
