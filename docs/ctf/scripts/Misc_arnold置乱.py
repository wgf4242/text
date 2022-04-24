import numpy as np
import cv2

r = 800
a = 121
b = 144
img = cv2.imread("flag.png", 1)
p = np.zeros([r, r, 3], np.uint8)
def dearnold(img):
    for x in range(0, r):
        for y in range(0, r):
            xx = -((a * b + 1) * x - b * y) % r
            yy = -(-a * x + y) % r
            p[xx][yy] = img[x][y]
    return p

for i in range(0, 33):
    p = dearnold(img)
    img = p
    cv2.imwrite(str(i) + ".png",p)