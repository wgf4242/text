# 西湖论剑2021 YUSA的小秘密 https://le1a.gitee.io/posts/cab9d8c/
# ByteCTF的Hardcore Watermark 01 https://bytectf.feishu.cn/docs/doccnqzpGCWH1hkDf5ljGdjOJYg#
# 奇偶做二值化处理 YCrCb

from cv2 import *
import cv2 as cv
img=cv2.imread('211119619784cbdb9fb.png')
src_value=cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
Y, Cr, Cb = cv.split(src_value)   #使用cv.split分离通道
cv.imwrite('Y.png', (Y % 2) * 255)   #对三个通道中的数据分别根据奇偶做二值化处理，并分别保存为图片
cv.imwrite('Cr.png', (Cr % 2) * 255)
cv.imwrite('Cb.png', (Cb % 2) * 255)