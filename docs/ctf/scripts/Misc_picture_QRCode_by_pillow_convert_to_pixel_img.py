# 大图转像素图, 读取每个格子中的中间像素 转为黑白像素图
# 如果存 PNG 用画图 或 FastStone看 不要用 ps 或其他看
# 保存为 BMP 用什么看都行
n = 12  # 12个格子
from PIL import Image

# Open image file
img = Image.open('pass.png')

# Convert image to black and white
img = img.convert('1')

# pixel cell is n*n
cell_width = img.width // n
img = img.resize((n * cell_width, n * cell_width))
img.save('pass_resize.png')

# Create new image
new_img = Image.new('1', (n, n))

# Loop through each cell and set the corresponding pixel in the new image to black or white
for x in range(0, img.width, cell_width):
    for y in range(0, img.height, cell_width):
        cell_color = img.getpixel((x + cell_width // 2, y + cell_width // 2))
        if cell_color == 0:
            new_img.putpixel((x // cell_width, y // cell_width), 0)
        else:
            new_img.putpixel((x // cell_width, y // cell_width), 255)

# Save the new image
new_img.save('new_pass.bmp')
print('用画图 或 FastStone看 不要用 ps 或其他看')
