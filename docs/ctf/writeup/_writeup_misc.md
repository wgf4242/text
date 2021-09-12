
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
