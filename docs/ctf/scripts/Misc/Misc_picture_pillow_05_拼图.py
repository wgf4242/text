# 2023第七届HECTF信息安全挑战赛 咖啡宝贝
# 4行6列 每块大小 66x100 按修改日期排序拼图
from pathlib import Path
from PIL import Image

jpg_files = Path('.').rglob('**/*.jpg')
sorted_files = sorted(jpg_files, key=lambda f: f.stat().st_mtime)

w, h = (66, 100)
row, col = 4, 6
img = Image.new('RGB', (col * w, row * h))
for i, file in enumerate(sorted_files):
    irow = i // col
    icol = i % col

    tmp = Image.open(file)
    img.paste(tmp, box=(icol * w, irow * h))  # Coordinate

img.save('out.png')
