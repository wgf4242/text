# [柏鹭杯 2021]蜜雪冰城? 修复条形码
from PIL import Image

pic = Image.open('密码.PNG')
width, height = pic.size
f = Image.new('RGB', (width, height), color=(255, 255, 255))  # type: Image

white = (255, 255, 255)
black = (0, 0, 0)


def check_black(file: Image, xy):
    x, _ = xy
    lst = [32, 83, 225, 106, 117, 38] # 处于黑色坐标的y轴位置
    for y in lst:
        r1, g1, b1, a1 = file.getpixel((x, y))
        if (r1, g1, b1) == black:
            return True
    return False


for y in range(height):
    for x in range(width):
        p = pic.getpixel((x, y))
        r, g, b, a0 = p
        if (r, g, b) == white or y < 29 or y > 230:
            f.putpixel((x, y), p)
            continue

        is_black = check_black(pic, (x, y))
        if is_black:
            f.putpixel((x, y), black)
        else:
            f.putpixel((x, y), p)

f.save('a.png')
f.show()
