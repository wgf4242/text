import cv2
import matplotlib.pyplot as plt
# 读取图像
img = cv2.imread('misc_picture_cv2_rgb_big.png')

# 获取像素范围 (0,0) 到 (50,50)
crop_img = img[0:50, 0:50]
# 获取像素范围 (50,50) 到 (100,100)
# crop_img = img[50:100, 50:100]
# 获取像素范围 (50,100) 到 (100,150)
# crop_img = img[100:150, 50:100] # 取100-150间的所有行, 取行内 50-100 列

# 保存裁剪后的图像（可选）
cv2.imwrite('cropped_example.png', crop_img)

# 显示裁剪后的图像 Linux
# cv2.imshow('Cropped Image', crop_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 使用matplotlib显示裁剪后的图像
plt.imshow(cv2.cvtColor(crop_img, cv2.COLOR_BGR2RGB))
plt.title('Cropped')
plt.show()