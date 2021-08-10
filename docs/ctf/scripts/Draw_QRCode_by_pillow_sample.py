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


# 解决 IOError：image file is truncated. 报错原因：图像文件被截断
ImageFile.LOAD_TRUNCATED_IMAGES = True
