# 2022年春秋杯春季赛Misc PINTU
from PIL import Image
import os
from tqdm import tqdm
pic = Image.new('RGB',(4000,4000),(255,255,255))
pt = os.listdir('./img')

for i in tqdm(range(len(pt))):
    f = open(f'./img/{pt[i]}','rb').read()
    w,h = f[6],f[8]
    img = Image.open(f'./img/{pt[i]}')
    pic.paste(img,(32*w,18*h))
pic.show()