from pathlib import Path

import numpy as np
import cv2

r, g, b = [0, 1, 2]


def get_channel(filename, channel_col):
    """
    :param filename:
    :param channel_col: 通道索引, r-0,g-1,b-2
    :return:
    """
    include = [x for x in [r, g, b] if x != channel_col]

    img = cv2.imread(filename)
    img[:, :, include] = 255  # 除了col通道都置于白色
    # 255一共是8位, 和每一位做与运算为1放白色，否则放黑色
    # 对应的 stegsovle green channel 0, 如果√第1位则 0b00000010
    res_index = np.where(img[:, :, channel_col] & 1)  # 筛选g0位有数据的像素点,每点3个数据[255,15,255] 返回索引
    img[res_index] = 255
    res_index = np.where(~img[:, :, channel_col] & 1)  # 无数据的用 ~反选, 填充黑色
    img[res_index] = 0

    # cv2.imshow('G-RGB', img)
    # cv2.waitKey(0)
    file = Path(filename)
    cv2.imwrite(f'{file.stem}_{channel_col}{file.suffix}', img)
    # cv2.imwrite(filename + str(channel_col) + '.png', img)


get_channel('x.png', g)
get_channel('x.png', r)
get_channel('x.png', b)
