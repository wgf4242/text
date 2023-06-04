import numpy as np
import cv2
green_image = cv2.imread('x.png') # BGR
green_image[:,:,0] = 255 # B通道置于白色
green_image[:,:,2] = 255 # R通道置于白色
# G通道保留

# 255一共是8位, 和每一位做与运算为1放白色，否则放黑色
# 对应的 stegsovle green channel 0, 如果√第1位则 0b00000010
res_index = np.where(green_image[:,:,1] & 1)  # 筛选g0位有数据的像素点,每点3个数据[255,15,255] 返回索引
green_image[res_index] = 255
res_index = np.where(~green_image[:,:,1] & 1)
green_image[res_index] = 0

cv2.imshow('G-RGB', green_image)
cv2.waitKey(0)
cv2.imwrite('ffcv1.png', green_image)