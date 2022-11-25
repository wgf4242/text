import numpy as np
import cv2

img = cv2.imread('3.png')  # BGR 通道
img[:, :, :] &= 0b11  # b通道清空


def f(a):
    if any(a):
        return np.array([55, 55, 55])
    return np.array([255, 255, 255])


res_img = np.apply_along_axis(f, 2, img)  # 三维最里面是axis=2 是 3位最里面,
cv2.imwrite('final4.png', res_img)
