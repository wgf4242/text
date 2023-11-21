from PIL import Image, ImageFile
import math

size = (200, 200)
img = Image.new("RGB", size)  # default black
img = Image.new("RGB", size, 'white')  # white
img = Image.new("RGB", size, 0xff)  # white
img = Image.new("RGB", size, 0x0000ff)  # red 低2位是红
img = Image.new("RGB", size, 0x00ff00)  # green
img = Image.new("RGB", size, 0xff0000)  # blue 高2位是蓝
img = Image.new("RGB", size, '#f00')  # red
img = Image.new("RGB", size, color='#00ff00')  # green
img = Image.new("RGB", size, color=(255, 255, 255))  # 255 255 255 白
img = Image.new("RGB", size, color='pink')

a = Image.open(a)  # type: Image.Image
a = a.convert("RGB")  # 转成RGB再像素对比

# 类型声明
a = Image.open('123.png')  # type: Image.Image
a.getpixel()
a.putpixel()
width, height = a.size

# 画图
draw.rectangle(((100, 100), (150, 150)), fill="red")  # left,top , right,bottom


# 放大
def multiply_image(image: Image.Image, n=20):
    w, h = image.size
    return image.resize((w * n, h * n), Image.ANTIALIAS)


# 解决 IOError：image file is truncated. 报错原因：图像文件被截断
ImageFile.LOAD_TRUNCATED_IMAGES = True

# 通道分离
red, green, blue, a = Image.open("flag.PNG").split()  # type: Image.Image


# Mode L
def mode_l_test():
    im = Image.new("L", (20, 20), color=0xff)  # 背景白色
    for i in range(20):
        for j in range(10):
            im.putpixel((i, j), 0)  # 填充黑色
    im.show()


def from_array():
    import numpy as np
    im = Image.open("hopper.jpg")
    a = np.asarray(im)
    im = Image.fromarray(a)
    im.show()


def cut_rect():
    from PIL import Image
    x, y = 0, 0  # 起始位置 (0, 0)
    width, height = 300, 400  # 宽度和高度
    cropped_img = img.crop((x, y, x + width, y + height))



def paste_rect():
    from PIL import Image
    result = Image.new("RGB", (400, 400), color=(255, 255, 255))
    red = Image.new("RGB", (20, 20), color=(255, 0, 0))
    result.paste(red, box=(0, 0))  # box: Coordinate
    result.show()


def mirror_image():
    img = Image.open('binodd.jpg')
    img_mirror = img.transpose(Image.FLIP_LEFT_RIGHT)
    img_mirror.save(r'binodd_mirror.png')


# by cv2
import cv2

## extract G channel
green_image = cv2.imread('x.png')
green_image[:, :, 0] = 0
green_image[:, :, 2] = 0
cv2.imshow('G-RGB', green_image)
cv2.waitKey(0)
cv2.imwrite('ff.png', green_image)
