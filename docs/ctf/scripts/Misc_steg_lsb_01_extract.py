# 根据黑白组成01，列读取01,转bytes, 拼合图形

import cv2
import numpy as np

rgb_image = cv2.imread('mmm.png')
rgb_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2RGB)
img = rgb_image.copy() & 1
img_base = img[:, :, 0]
im_flatten = np.dstack(img_base).flatten()

img2 = im_flatten.reshape(-1, 8)
op = 2 ** np.arange(8, dtype=np.uint8)[::-1]  #  [0b10000000, 0b1000000, 0b100000, 0b10000, 0b1000, 0b100, 0b10, 0b1] 
data = img2.dot(op)
open('res.png', 'wb').write(data.tobytes())
