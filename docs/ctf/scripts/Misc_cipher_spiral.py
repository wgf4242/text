# 螺旋加密 spiral - CISCN2022 babydisk
# http://www.snowywar.top/?p=3400
# 0-86是边界， 文件大小是7569 开平方得 87.
from struct import pack

file = open('spiral.zip', 'rb').read()
rotate = 0
match = ((0, 1), (1, 0), (0, -1), (-1, 0))
wall = [0, 86, 86 ,0]
sets = (1, -1, -1, 1)
matrix = []
for i in range(87):
    list = []
    for o in range(87):
        list.append(0)
    matrix.append(list)

x = 0
y = 0

for i in file:
    matrix[y][x] = i
    x += match[rotate][1]
    y += match[rotate][0]
    
    if x > wall[1] or x < wall[3] or y > wall[2] or y < wall[0]:
        x -= match[rotate][1]
        y -= match[rotate][0]
        wall[rotate] += sets[rotate]
        rotate = (rotate + 1) % 4
        x += match[rotate][1]
        y += match[rotate][0]



file3 = open('out.zip', 'wb')
for i in matrix:
    for o in i:
        file3.write(pack('B', o))
file3.close()