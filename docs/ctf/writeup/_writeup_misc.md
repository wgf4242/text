
# 文字隐写
## TTL隐写 - [SWPU2019]Network（TTL隐写）

https://guokeya.github.io/post/swpu2019networkttl-yin-xie/

就给了一个TXT。里面就四种类型的数字。
63/127/191/255

将其各自转换为二进制
```
00111111
01111111
10111111
11111111
```

只有前两位是变化的。这就是TTL隐写。

```python
import binascii

f = open('attachment.txt', 'r')
s = ''

while i := f.readline().strip('\n'):
    if i == "63":
        a = '00'
    if i == "127":
        a = '01'
    if i == "191":
        a = '10'
    if i == "255":
        a = '11'
    s += a
data = ''
for i in range(0, len(s), 8):
    data += chr(int(s[i:i + 8], 2))
data = binascii.unhexlify(data)
open('fb.zip', 'wb').write(data)
```


## 羊城杯2021 misc520

循环解压, 并检测story文件有没有异常
```python
# 羊城杯2021 Misc520
import zipfile
from pathlib import Path

origin = open('story', 'r', encoding="utf-8").read()

def zips():  #处理压缩包
    while True:
        if not any(True for _ in Path('.').glob('*.zip')):
            return
        for file in Path('.').glob('*.zip'):
            txt = open('story', 'r', encoding="utf-8").read()
            if txt != origin:
                print(txt)
            zip_file = zipfile.ZipFile(file)
            zip_list = zip_file.namelist()  #获取压缩包中的文件
            for f in zip_list:
                zip_file.extract(f, '.')      #将压缩文件放入‘.’文件夹下
            zip_file.close()
            file.unlink()
zips()
```

得到
```
这都被你发现了？
我这故事不错吧，嘻嘻嘻
那就把flag给你吧
oh，不，还有一半藏在了pcap的心里，快去找找吧
左心房右心房，扑通扑通的心，咿呀咿呀的❤
72, 89, 75, 88, 128, 93, 58, 116, 76, 121, 120, 63, 108,
```
zsteg flag.png ， 检测到flag.pcap

```
imagedata           .. text: "\n\n\n\n\t\n\n\n\n"
b1,r,lsb,xy         .. file: raw G3 data, byte-padded
b1,bgr,lsb,xy       .. text: "flag.pcap"  #按这个选
```

两种方式
1. stegsovle 打开, 勾上r0g0b0，LSB first, 选bgr模式。 save bin得到PK开头的zip文件。 
2. 题目提示LSBSteg, 搜了到python文件。  `LSBsteg.py decode -i flag.png -o flag.zip`

暴力破解zip。

tshark 读取usb信息。

```
tshark -r flag.pcap -T fields -e usb.capdata > out.txt
```


```python
nums = []
keys = open('out.txt', 'r')
f = open('xy.txt', 'w')
posx = 0
posy = 0
for line in keys:
    if len(line) != 12:
        continue
    x = int(line[3:5], 16)
    y = int(line[6:8], 16)
    if x > 127:
        x -= 256
    if y > 127:
        y -= 256
    posx += x
    posy += y
    btn_flag = int(line[0:2], 16)  # 1 for left , 2 for right , 0 for nothing
    if btn_flag != 0:
        f.write(str(posx))
        f.write(' ')
        f.write(str(posy))
        f.write('\n')

f.close()
```
或者 
gnuplot
>plot xy.txt
注意 plot的图片需要翻转

得到组合下  72, 89, 75, 88, 128, 93, 58, 116, 76, 121, 120, 63, 108, 130, 63, 111, 94, 51, 134, 119, 146

```python
# 羊城杯是 GWHT, 71, 87, 72, 84
# 相差 1,2,3,4...
lst = [72, 89, 75, 88, 128, 93, 58, 116, 76, 121, 120, 63, 108, 130, 63, 111, 94, 51, 134, 119, 146]
for i, n in enumerate(lst):
    print(chr(n - i - 1), end='')

```