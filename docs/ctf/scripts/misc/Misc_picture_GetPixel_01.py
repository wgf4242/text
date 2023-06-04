from PIL import Image

img = Image.open('out.bmp')
img = img.convert('RGB')
str = ''
x, y = img.size

for i in range(x):
    for j in range(y):
        rgb = img.getpixel((i, j))
        m = (rgb[0] << 16) + (rgb[1] << 8) + rgb[2]
        str += chr(m)

print(str)
