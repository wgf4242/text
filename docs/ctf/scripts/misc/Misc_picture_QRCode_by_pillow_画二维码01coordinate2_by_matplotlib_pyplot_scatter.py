"""
@description: 画二维码,
data format like
0 0
0 1
0 2
0 3
0 4
0 5
0 6
"""

import matplotlib.pyplot as plt

f = open("xy.txt", "r").readlines()

x_li = []
y_li = []
for i in range(len(f)):
    x_li.append(int(f[i].strip().split()[0]))
    y_li.append(int(f[i].strip().split()[1]))

plt.scatter(x_li, y_li, s=10)  # 调整 s 参数来设置点的大小
plt.savefig("flag.png")
plt.show()