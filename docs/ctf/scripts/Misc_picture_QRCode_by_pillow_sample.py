from PIL import Image
import math

img = Image.new("RGB", size)  # default black
img = Image.new("RGB", size, color=(255, 255, 255))  # 255 255 255 白

a = Image.open(a)  # type: Image.Image
b = Image.open(b)  # type: Image.Image
a = a.convert("RGB") # 转成RGB再像素对比


from PIL import ImageFile


# 类型声明
a = Image.open('123.png')  # type: Image.Image
a.getpixel()
a.putpixel()
width, height = a.size

# 画图
draw.rectangle(((100, 100), (150, 150)), fill="red") # left,top , right,bottom

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
            im.putpixel((i, j), 0)
    im.show()


# by cv2
import cv2

## extract G channel
green_image = cv2.imread('x.png')
green_image[:,:,0] = 0
green_image[:,:,2] = 0
cv2.imshow('G-RGB', green_image)
cv2.waitKey(0)
cv2.imwrite('ff.png', green_image)