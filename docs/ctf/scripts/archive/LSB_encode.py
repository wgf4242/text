# Stegsolve 读取时 √LSB √R0,G0,B0通道
# https://wenku.baidu.com/view/ff590e9d5f0e7cd1842536d7.html
from PIL import Image


def get_key(filename):
    # 获取要隐藏的文件内容
    f = open(filename, "rb")
    txt = ""
    s = f.read()
    for c in s:
        txt = txt + f'{c:0>8b}'  # 将c用2进制表示, 用0左侧填充至8位
    f.close()
    return txt


def mod(x, y):
    return x % y


# str1为载体图片路径,str2为隐写文件,str3为加密图片保存的路径
def func(input_image, txt_file, enc_image):
    im = Image.open(input_image)
    # 获取图片的宽和高
    width = im.size[0]
    print("width:" + str(width))
    height = im.size[1]
    print("height:" + str(height))
    count = 0
    # 获取需要隐藏的信息
    key = get_key(txt_file)
    keylen = len(key)
    for h in range(0, height):
        for w in range(0, width):
            pixel = im.getpixel((w, h))
            a = pixel[0]
            b = pixel[1]
            c = pixel[2]
            if count == keylen:
                break
            # 下面的操作是将信息隐藏进去
            # 分别将每个像素点的RGB值余2,这样可以去掉最低位的值
            # 出再从需更A式的信息中服H一位,协为感利
            # 两值相加,就把信息隐藏起来
            a = a - mod(a, 2) + int(key[count])
            count += 1
            if count == keylen:
                im.putpixel((w, h), (a, b, c))
                break
            b = b - mod(b, 2) + int(key[count])
            count += 1
            if count == keylen:
                im.putpixel((w, h), (a, b, c))
                break
            c = c - mod(c, 2) + int(key[count])
            count += 1
            if count == keylen:
                im.putpixel((w, h), (a, b, c))
                break
            if count % 3 == 0:
                im.putpixel((w, h), (a, b, c))
    im.save(enc_image)


# 原图
old = "tu.png"
new = "tu_LSB1.png"
enc = 'flag.txt'

func(old, enc, new)
# get_key(enc)
