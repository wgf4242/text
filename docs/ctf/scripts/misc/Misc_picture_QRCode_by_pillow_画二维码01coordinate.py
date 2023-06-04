"""
@description: 画二维码,
data format like
0 0
0 1
0 2
0 3
0 4
0 5
0 6
"""
from PIL import Image

coordinates = open('flag.txt', 'r').read()
coordinates = coordinates.strip('\n').split('\n')
d2_array = [x.split(' ') for x in coordinates]


def get_max(txt):
    import itertools
    chain = itertools.chain(*(map(int, xy) for xy in txt))
    return max(chain)


MAX = int(get_max(d2_array))
im = Image.new("RGB", (MAX + 1, MAX + 1), color=(255, 255, 255))  # 背景白色
black = (0, 0, 0)
for xy in coordinates:
    x, y = map(int, xy.split(' '))
    im.putpixel([x, y], black)
im.show()
exit(0)
