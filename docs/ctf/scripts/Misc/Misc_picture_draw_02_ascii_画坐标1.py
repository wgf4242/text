"""
010 editor 默认用 Droid Sans Mono 看
MS Gothic
楷体 看得比较清楚

题目: 我爱Linux

pickle 文件头80 04，ascii码是 €
"""
import pickle

data = open("data", "rb+")
points = pickle.load(data)

lst = []
for row in points:
    if not row:
        continue
    v_max = row[-1][0] + 1
    tmp_row = [' '] * v_max
    for x, v in row:
        tmp_row[x] = v
    lst.append(tmp_row)

for row in lst:
    print(''.join(row))
