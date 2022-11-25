# 西湖论剑2021 - misc-YUSA的小秘密
import cv2
img =cv2.imread('yusa.png')
cv_color= cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
cv2.imwrite('flag.png',cv_color)