"""
三维数组: 2*2*2数组
ar = np.array([
    [[0, 1], [2, 3]],
    [[4, 5], [6, 7]]
])

# ar[1:], 第1维第2个  array([[[4, 5], [6, 7]]])
# ar[1,1] === ar[1][1] === array([6,7])
# ar[:,1] 1维所有, 2维[1]   array([[2, 3],[6, 7]])
# ar & 1 所有值和1做与运算   array([[[0, 1], [0, 1]], [[0, 1], [0, 1]]], dtype=int32)

# ar.flatten()                          # [0, 1, 2, 3, 4, 5, 6, 7]
# np.dstack(ar).flatten()               # [0, 4, 1, 5, 2, 6, 3, 7])  将列表中的数组沿深度方向进行拼接。
# 2**np.arange(8,dtype=np.uint8)[::-1]  # [0b10000000, 0b1000000, 0b100000, 0b10000, 0b1000, 0b100, 0b10, 0b1]
# setdtype:ar.astype(np.uint8)

# dot()返回的是两个数组的点积(dot product)
# ar.reshape(-1, 8)                  # 不知道size, numpy自动找出
"""

import numpy as np
import cv2


img = cv2.imread('misc_picture_cv2_rgb.png')  # Default BGR mode
# image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # M1: convert to RGB
# image_rgb = img[...,::-1] # M2: convert to RGB
# print(img)  # row1 ... rowN [[[B, G, R], [B, G, R], ...], ...]


c1,c2,c3 = img.shape # 1维 2维 3维 数量 == 从里向外

def reshape():
    image_bgr = img
    image_bgr = image_bgr.reshape(3, 2, 3)  # 3行 2列 每行3个元素为RGB
    cv2.imwrite('ffcv1.png', image_bgr)


def reshape_delete():
    image_bgr = img
    # image_bgr = image_bgr.reshape(3, 2, 3)  # 3行 2列 每行3个元素为RGB
    xx = image_bgr[:, :100]  # 删除100列之后，只保留之前的
    xx2 = xx.reshape(200,200,3)
    cv2.imwrite('ffcv1.png', xx2)

def fill_green():
    img[:, :, 0] = 0  # b通道清空
    img[:, :, 1] = 255  # g通道填充
    img[:, :, 2] = 0  # r通道清空


