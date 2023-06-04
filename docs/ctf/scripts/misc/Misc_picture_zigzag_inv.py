# zigzag逆变换
from PIL import Image
import numpy as np
def Zmartix_inverse(m,n):
    result, count = [], 0
    result = np.zeros((m,n),int)
    i, j = 0, 0
    while count < m * n:
        up = True
        while up == True and i >= 0 and j < n:
            result[i][j]=count
            i -= 1
            j += 1
            count += 1

        if j <= n - 1:
            i += 1

        else:
            i += 2
            j -= 1
        up = False
        while up == False and i < m and j >= 0:
            result[i][j]=count
            i += 1
            j -= 1
            count += 1

        if i <= m - 1:
            j += 1

        else:
            j += 2
            i -= 1
    return result
original = Image.open('original.bmp')
final = Image.new("RGB",original.size)
temp = Zmartix_inverse(512,512)
for y in range(len(temp)):
    for x in range(len(temp[0])):
        final.putpixel((x,y),original.getpixel((int(temp[y][x]%512),int(temp[y][x]//512))))
final.save('flag.bmp')