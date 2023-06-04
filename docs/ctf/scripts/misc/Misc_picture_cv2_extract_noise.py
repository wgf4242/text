import cv2
import numpy as np


def f(a):
    if (a == [0, 0, 0]).all() or (a == [255, 255, 255]).all():
        return np.array([0, 0, 0])
    return np.array([255, 255, 255])


img = cv2.imread("tHXcode.png")

res_img = np.apply_along_axis(f, 2, img)  # 三维最里面是axis=2 是 3位最里面,
cv2.imwrite('new.png', res_img)
