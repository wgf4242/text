import numpy as np
import cv2

img = cv2.imread('misc_picture_cv2_rgb.png')  # Default BGR mode
# image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # M1: convert to RGB
# image_rgb = img[...,::-1] # M2: convert to RGB
# print(img)  # row1 ... rowN [[[B, G, R], [B, G, R], ...], ...]


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


reshape()

