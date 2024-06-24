"""
能源网络安全大赛2024-个人赛 损坏的图片
data加载后类似 [[(42, 'X'), (43, 'X'), (44, 'X')], [(6, 'X'), (7, 'X'), (41, 'X'), (42, 'X')] ...]
"""
import pickle
import matplotlib.pyplot as plt

file_path = '2.data'
with open(file_path, 'rb') as file:
    data = pickle.load(file)

# 提取数据中的所有点
points = [(x, i) for i, sublist in enumerate(data) for x, _ in sublist]
# 调整Y轴的⽐例，翻转图像
x_vals, y_vals = zip(*points)
adjusted_y_vals = [-y for y in y_vals]
# 绘制这些点
plt.figure(figsize=(10, 10))
plt.scatter(x_vals, adjusted_y_vals, marker='X')
plt.show()
