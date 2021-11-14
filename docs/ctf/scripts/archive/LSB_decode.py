# -*- coding:utf-8 -*-
from PIL import Image


def mod(x, y):
    return x % y


def toasc(strr):
    return int(strr, 2)


# le为所要提取的信息的长度,str1为加密载体图片的路径,str2为提取文件的保存路径
def func(le, str1, str2):
    a = ''
    b = ''
    im = Image.open(str1)
    lenth = le * 8
    width = im.size[0]
    height = im.size[1]
    count = 0
    for h in range(0, height):
        for w in range(0, width):
            # 获得(w,h)点像素的值
            pixel = im.getpixel((w, h))
            # 此处余3,依次从R、G、B三个颜色通道获得最低位的除
            if count % 3 == 0:
                count += 1
                b = b + str((mod(int(pixel[0]), 2)))
                if count == lenth:
                    break
            if count % 3 == 1:
                count += 1
                b = b + str((mod(int(pixel[1]), 2)))
                if count == lenth:
                    break
            if count % 3 == 2:
                count += 1
                b = b + str((mod(int(pixel[2]), 2)))
                if count == lenth:
                    break
        if count == lenth:
            break
    with open(str2, "wb") as f:
        for i in range(0, len(b), 8):
            # 以每8位为一组二进制,转换为十进制
            stra = toasc(b[i:i + 8])
            # 将转换后的十注制数视为ascii码:再转换为字符中写入到文件中
            f.write(chr(stra).encode())
            stra = ''
        f.close()


# 文件长度
le = 30
# 含有隐藏信息的图片
new = r"tu_LSB1.png"
# 信息提取出后所存放的文件
tiqu = r"get_flag.txt"
func(le, new, tiqu)
