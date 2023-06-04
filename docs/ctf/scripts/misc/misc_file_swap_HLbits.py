import numpy as np

# 每个byte 低4 高4位 提取交换
ar = np.fromfile('m', 'uint8')
b1 = (ar & 0xf0) >> 4
b2 = (ar & 0xf) << 4
c = b1 + b2
c.tofile('rev')
