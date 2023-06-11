# http://www.fzwjscj.xyz/index.php/archives/30/#bincat2
# 没啥难的，脚本一把梭。。。图片替换长度减一半扫二维码后md5即可
from PIL import Image
from pyzbar.pyzbar import decode
import hashlib

p1 = Image.open('11.png').convert('RGB')
p2 = Image.open('12.png').convert('RGB')
a,b = p1.size
dif = []
for y in range(b):
    for x in range(a):
        if p1.getpixel((x,y))!=p2.getpixel((x,y)):
            dif.append((x,y))
mark = dif[0]

p = Image.open('res.png').convert('RGB')
aa,bb = p.size
data = []
for y in range(0,bb,50):
    for x in range(0,aa,100):
        if p.getpixel((x+mark[0],y+mark[1])) == p1.getpixel(mark):
            data.append('1')
        else:
            data.append('0')

B = Image.new('L',(10,10),255)
W = Image.new('L',(10,10),0)
np = Image.new('L',(290,290),0)
for y in range(29):
    for x in range(29):
        if data[x+29*y] == '0':
            np.paste(B,(10*x,10*y))
        else:
            np.paste(W,(10*x,10*y))
np.save('r.png')
pp = Image.open('r.png')
barcodes = decode(pp)
for barcode in barcodes:
    barcodeData = barcode.data.decode("utf-8")
    print(hashlib.md5(barcodeData.encode()).hexdigest())
