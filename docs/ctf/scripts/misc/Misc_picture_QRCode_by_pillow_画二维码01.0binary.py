from PIL import Image
import math

data = '111111000000'

MAX = int(math.sqrt(len(data)))
im = Image.new("RGB", (MAX, MAX), color='white')  # 背景白色

for x in range(MAX):
    for y in range(MAX):
        if data[x * MAX + y] == '1':
            im.putpixel([x, y], 0)
        else:
            im.putpixel([x, y], 0xffffff)
# im.show()
im.save('a.png')
