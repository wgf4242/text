"""
(255, 255, 255)
(255, 255, 255)
(255, 255, 255)
(255, 255, 255)
(255, 255, 255)
"""
import math

import numpy as np
from PIL import Image

array = np.zeros([100, 200, 3], dtype=np.uint8)  # [x100, y100, z3]
f = open('qr.txt', 'r')
length = len(f.readlines())

f = open('qr.txt', 'r')
xy_len = int(math.sqrt(length))

lst = '[' + f.read().replace('\n', ',') + ']'
c = np.array(eval(lst), dtype=np.uint8)
d = np.resize(c, [200,200,3])

g = Image.fromarray(d)
g.save('test.png')
