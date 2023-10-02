"""2文件是 1 0 组合
11111111
00010110
"""
import numpy as np
import cv2, re

f = open('2', 'r', encoding='utf8')
raw = f.read()
buffer = re.sub(r'[\r\n]+', '', raw)
lines = raw.strip('\n').splitlines()
row = len(lines)
col = len(lines[0])

print(row)
print(col)

r = np.frombuffer(buffer.encode(), dtype=np.uint8).copy()
r = r.reshape((row, col))
r[r == 49] = 0  # 将颜色值为49的像素映射为黑色（0）
r[r == 48] = 255  # 将颜色值为48的像素映射为白色（255）

cv2.imwrite('output.png', r)
