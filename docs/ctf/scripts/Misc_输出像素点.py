#!/usr/bin/env python
# -*- coding: utf-8 -*-
import zlib
import binascii

from PIL import Image
pic = Image.open("xs.png") #//要进行获取像素点的图片
strtxt = open('c.txt','a') #//存放输出结果的txt
width,height = pic.size
for y in range(height):
    for x in range(width):
        strtxt.write(str(pic.getpixel((x,y))))
strtxt.close()