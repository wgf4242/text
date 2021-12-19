import numpy as np
import cv2

# rgb_image = cv2.imread('g00000001.png')
rgb_image = cv2.imread('mmm.png')
rgb_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2RGB)


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
    green_image = rgb_image.copy()  # Make a copy
    if rgb_order:
        green_image[:, :, [0, 1, 2]] = green_image[:, :, get_order(rgb_order)]

    # cv2.imwrite(f'rg.png', green_image)

    lst = []
    for channel, index in zip([r, g, b], [0, 1, 2]):
        if not channel:
            continue
        green_image[:, :, index] = green_image[:, :, index] & channel
        for i in range(8)[::-1]:
            if channel & 2 ** i:
                l = np.where(green_image[:, :, index] & 2 ** i > 0, 1, 0)
                lst.append(l)

    c = np.dstack(lst).flatten()

    f = bytearray([])
    for i in range(0, len(c), 8):
        tmp_bin = ''.join([str(x) for x in c[i: i + 8]])
        dec = int(tmp_bin, 2)
        f.append(dec)
    f = f.strip(b'\x00')
    print(f.hex().upper())
    open(get_name(r, g, b, rgb_order), 'wb').write(f)


if __name__ == '__main__':
    save_rgb_final(r=0b00000001)
    save_rgb_final(g=0b00000001)
    save_rgb_final(b=0b00000001)
    save_rgb_final(r=0b11111111)
    save_rgb_final(g=0b11111111)
    save_rgb_final(b=0b11111111)
    # save_rgb_final(r=0b00000001, g=0b0000001)
    # save_rgb_final(r=0b00000001, g=0b0000001)
    # save_rgb_final(r=0b00000001, g=0b00000001, b=0b00000001)
    save_rgb_final(r=0b00000001, g=0b00000001, b=0b00000001, rgb_order='rgb')
    save_rgb_final(r=0b00000001, g=0b00000001, b=0b00000001, rgb_order='grb')
    save_rgb_final(r=0b00000001, g=0b00000001, b=0b00000001, rgb_order='rbg')
    save_rgb_final(r=0b00000001, g=0b00000001, b=0b00000001, rgb_order='brg')
    save_rgb_final(r=0b00000001, g=0b00000001, b=0b00000001, rgb_order='gbr')
    save_rgb_final(r=0b00000001, g=0b00000001, b=0b00000001, rgb_order='bgr')
