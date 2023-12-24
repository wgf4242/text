import os

file="mmm.png"
# MSBFirst，是从高位开始读取，LSBFirst是从低位开始读取
# zsteg：只能从高位开始读，比如-b 0x81，在读取不同通道数据时，都是先读取一个字节的高位，再读取该字节的低位。对应到Stegsolve就是MSBFirst的选项。
# zsteg -b 0x02 -c r  {file} -n 0 -v > r00000010_ROW_MSB_RGB

# zsteg 不能0b10000000 这种提取 只能 0b11111111 的提取
# zsteg -e b1,rgb,lsb {file}    > r00000001g00000001b00000001.png
# zsteg -e b1,rgb,bgr,xy {file} > r0g0b0_bgr.png
## zsteg {file} -c r,g,b -b 8 -o xy   
# zsteg -e b8,g,lsb,xy {file} > g0-g7.png
## zsteg {file} -c r8 -b 00001110 -o xy -v
## zsteg {file} -c r1 -b 1 -o xy -v  --- r1,lsb,xy --- r1.png

os.system(f'exiftool {file} >> info.txt')
os.system(fr"zsteg {file} | sed -z 's/[\r\n]\+/\r\n/g' | sed '/\.\. \r/d' > 00_basic")
os.system(f'zsteg -e b1,r,lsb,xY     {file} > 01_r00000001_ROW_LSB_RGB')
os.system(f'zsteg -e b1,g,lsb,xY     {file} > 01_g00000001_ROW_LSB_RGB')
os.system(f'zsteg -e b1,b,lsb,xY     {file} > 01_b00000001_ROW_LSB_RGB')

os.system(f'zsteg -e b1,r,lsb,yx     {file} > 02_r00000001_COLUMN_LSB_RGB')
os.system(f'zsteg -e b1,g,lsb,yx     {file} > 02_g00000001_COLUMN_LSB_RGB')
os.system(f'zsteg -e b1,b,lsb,yx     {file} > 02_b00000001_COLUMN_LSB_RGB')

os.system(f'zsteg -e b1,bgr,lsb,xy   {file} > 03_r00000001g000000001b000000001_ROW_BGR')
os.system(f'zsteg -e b1,rgb,lsb,xy   {file} > 03_r00000001g000000001b000000001_ROW_RGB')
# os.system(f'zsteg -e b2,bgr,lsb,xy   {file} > 03_r2g2b2_ROW_BGR')
# os.system(f'zsteg -e b2,rgb,lsb,xy   {file} > 03_r2g2b2_ROW_RGB')
# os.system(f'zsteg -e b3,bgr,lsb,xy   {file} > 03_r3g3b3_ROW_BGR')
# os.system(f'zsteg -e b3,rgb,lsb,xy   {file} > 03_r3g3b3_ROW_RGB')
# os.system(f'zsteg -e b4,bgr,lsb,xy   {file} > 03_r4g4b4_ROW_BGR')
# os.system(f'zsteg -e b4,bgr,lsb,xy   {file} > 03_r4g4b4_ROW_BGR')
# os.system(f'zsteg -e b5,bgr,lsb,xy   {file} > 03_r5g5b5_ROW_BGR')
# os.system(f'zsteg -e b5,bgr,lsb,xy   {file} > 03_r5g5b5_ROW_BGR')
# os.system(f'zsteg -e b6,bgr,lsb,xy   {file} > 03_r6g6b6_ROW_BGR')
# os.system(f'zsteg -e b6,bgr,lsb,xy   {file} > 03_r6g6b6_ROW_BGR')
# os.system(f'zsteg -e b7,bgr,lsb,xy   {file} > 03_r7g7b7_ROW_BGR')
# os.system(f'zsteg -e b7,bgr,lsb,xy   {file} > 03_r7g7b7_ROW_BGR')
# os.system(f'zsteg -e b8,bgr,lsb,xy   {file} > 03_r8g8b8_ROW_BGR')
# os.system(f'zsteg -e b8,bgr,lsb,xy   {file} > 03_r8g8b8_ROW_BGR')

os.system(f'zsteg -e b8,r,lsb,xy     {file} > 04_r11111111_ROW_MSB_RGB')
os.system(f'zsteg -e b8,g,lsb,xy     {file} > 04_g11111111_ROW_MSB_RGB') # 搬山的魔法少女
os.system(f'zsteg -e b8,b,lsb,xy     {file} > 04_b11111111_ROW_MSB_RGB')

os.system(f'zsteg -b 0x80 -c r -o yx {file} -n 0 -v > zsteg_r10000000_COLUMN_LSB_RGB')
os.system(f'zsteg -b 0x80 -c g -o yx {file} -n 0 -v > zsteg_g10000000_COLUMN_LSB_RGB')
os.system(f'zsteg -b 0x80 -c b -o yx {file} -n 0 -v > zsteg_b10000000_COLUMN_LSB_RGB')
# os.system('zsteg -e b1,r,lsb,xy   {file} > r00000001_ROW_MSB_RGB')
# os.system('zsteg -e b2,r,lsb,xy   {file} > r00000011_ROW_MSB_RGB')

import numpy as np
import cv2

# rgb_image = cv2.imread('g00000001.png')
rgb_image = cv2.imread(f'{file}')


# a = cv2.imread('ggggg.png')

def get_order(g='bgr'):
    return ['rgb'.index(x) for x in g]


def get_name(r=None, g=None, b=None, rgb_order=None):
    if not rgb_order:
        rgb_order = ''
    name = ''.join(x + f'{y:08b}' for x, y in zip('rgb', [r, g, b]) if y)
    return name + rgb_order


def save_rgb_final(r=None, g=None, b=None, rgb_order=None):
    """
    :param rgb_order: 'rgb', 'bgr' 等等模式
    :return:
    """
    image = rgb_image.copy()  # Make a copy
    if rgb_order:
        image[:, :, [0, 1, 2]] = image[:, :, get_order(rgb_order)]

    # cv2.imwrite(f'rg.png', image)

    rgb_lsb_lst = []  # rgb_lsb_lst
    for channel, index in zip([r, g, b], [0, 1, 2]):
        if not channel:
            continue
        image[:, :, index] = image[:, :, index] & channel
        for i in range(8)[::-1]:  # [7, 6, 5, 4, 3, 2, 1, 0]
            if channel & 2 ** i:  # [10000000,01000000,00100000,00010000,00001000,00000100,00000010,00000001]
                l = np.where(image[:, :, index] & 2 ** i > 0, 1, 0)
                rgb_lsb_lst.append(l)

    if len(rgb_lsb_lst) == 1:
        arr = rgb_lsb_lst[0]
        flat = np.stack(arr, axis=1).flatten()
    else:
        flat = np.dstack(rgb_lsb_lst).flatten()
    flat = flat.reshape(-1, 8)
    flat = flat.dot(2 ** np.arange(8, dtype=np.uint8)[::-1])
    result = np.array(flat, dtype=np.uint8)

    open(get_name(r, g, b, rgb_order), 'wb').write(result.tobytes())


def save_img(channel):
    image = rgb_image.copy()  # Make a copy
    img = image.copy()

    dic = {'r': 0, 'g': 1, 'b': 2}
    mode = dic[channel]  # BGR中保留的通道
    for k, v in dic.items():
        if k == channel:
            continue
        img[:, :, v] = 255
    res_index = np.where(img[:, :, mode] & 1)  # 筛选0位有数据的像素点,每点3个数据[255,15,255] 返回索引
    img[res_index] = 255
    res_index = np.where(~img[:, :, mode] & 1)
    img[res_index] = 0
    cv2.imwrite(f'{channel}.png', img)


if __name__ == '__main__':
    save_img('b')
    save_img('r')
    save_img('g')

    save_rgb_final(r=0b00000001)
    save_rgb_final(g=0b00000001)
    save_rgb_final(b=0b00000001)
    save_rgb_final(r=0b10000000)
    save_rgb_final(g=0b10000000)
    save_rgb_final(b=0b10000000)
    # 其他都有问题
    # save_rgb_final(r=0b11111111)
    # save_rgb_final(g=0b11111111)
    # save_rgb_final(b=0b11111111)
    # # save_rgb_final(r=0b00000001, g=0b0000001)
    # # save_rgb_final(r=0b00000001, g=0b0000001)
    # # save_rgb_final(r=0b00000001, g=0b00000001, b=0b00000001)
    # save_rgb_final(r=0b00000001, g=0b00000001, b=0b00000001, rgb_order='rgb')
    # save_rgb_final(r=0b00000001, g=0b00000001, b=0b00000001, rgb_order='grb')
    # save_rgb_final(r=0b00000001, g=0b00000001, b=0b00000001, rgb_order='rbg')
    # save_rgb_final(r=0b00000001, g=0b00000001, b=0b00000001, rgb_order='brg')
    # save_rgb_final(r=0b00000001, g=0b00000001, b=0b00000001, rgb_order='gbr')
    # save_rgb_final(r=0b00000001, g=0b00000001, b=0b00000001, rgb_order='bgr')
