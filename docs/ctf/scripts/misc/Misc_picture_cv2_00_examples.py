# 西湖论剑2021 - misc-YUSA的小秘密
# 先读行再读列
import cv2
img =cv2.imread('yusa.png')
cv_color= cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
cv2.imwrite('flag.png',cv_color)

# img_rgb = cv2.cvtColor(crop_img, cv2.COLOR_BGR2RGB)
# crop_img = img[r1:r2, c1:c2] # 取 r1-r2间的所有行, c1:c2间的所有列