
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


## 羊城杯2021 赛博德国人-Enigama



### 小WIKI 传统密码 - ENIGMA 恩尼格玛密码机

```python
original_wheel = ['ZWAXJGDLUBVIQHKYPNTCRMOSFE',
                  'PBELNACZDTRXMJQOYHGVSFUWI',
                  'BDMAIZVRNSJUWFHTEQGYXPLOCK',
                  'RPLNDVHGFCUKTEBSXQYIZMJWAO',
                  'IHFRLABEUOTSGJVDKCPMNZQWXY',
                  'AMKGHIWPNYCJBFZDRUSLOQXVET',
                  'GWTHSPYBXIZULVKMRAFDCEONJQ',
                  'NOZUTWDCVRJLXKISEFAPMYGHBQ',
                  'XPLTDSRFHENYVUBMCQWAOIKZGJ',
                  'UDNAJFBOWTGVRSCZQKELMXYIHP',
                  'MNBVCXZQWERTPOIUYALSKDJFHG',
                  'LVNCMXZPQOWEIURYTASBKJDFHG',
                  'JZQAWSXCDERFVBGTYHNUMKILOP ']#所给初始状态的轮转机
shifted_wheel = []
key = [2,3,7,5,13,12,9,1,8,10,4,11,6] #所给密钥
ciphertext = 'NFQKSEVOQOFNP' #所给密文
 
#按照密钥顺序对轮排序
for i in key:
    shifted_wheel.append(original_wheel[i-1])
print('按照密钥重新排序后的轮转机：\n',shifted_wheel)
 
#按照密文顺序转动轮
for i in range(len(shifted_wheel)):
    index = shifted_wheel[i].index(ciphertext[i])
    shifted_wheel[i] = shifted_wheel[i][index:]+shifted_wheel[i][0:index]
print('按照密文重新排序后的轮转机：\n',shifted_wheel)
 
#读取所有恢复的明文
print('输出所有可能的明文：')
for i in range(1,len(shifted_wheel[0])):
    for j in range(len(shifted_wheel)):
        print(shifted_wheel[j][i],end='')
    print('')
```


## 2021陇剑杯 wifi
https://www.nctry.com/2449.html

filescan 搜 wifi.

volatility -f 'Windows 7-dde00fa9.vmem' --profile=Win7SP1x86_23418 dumpfiles -Q 0x000000003fdc38c8 --dump-dir=./

是个zip文件。打开提示密码是网卡GUID。

再搜interface, 找到guid解压，得到wifi essid和密码 。

解密流量。
`airdecap-ng 客户端.cap -e My_Wifi -p 233@114514_qwe`

再打开新的 dec.cap文件发现搜http, 发现流量传输还是加密的。

看服务器的流量。base64解码发现是哥斯拉木马。使用了xor_base64的加密器 。。异或加密再执行一次就能解密。。。去到前后16个混淆字符。。。然后得到 flag。
```php 
<?php
function encode($D,$K){
    for($i=0;$i<strlen($D);$i++){
        $c = $K[$i+1&15];
        $D[$i] = $D[$i]^$c;
    }
    return $D;
}
 
$pass='pass';
$payloadName='payload';
$key='3c6e0b8a9c15224a';
echo gzdecode(encode(base64_decode('需要解密的内容'),$key));
?>
```

14.根据上面的文章可以知道（对于PHP_XOR_BASE64加密方式来说，前后各附加了16位的混淆字符），所以我们拿到的流量要先删除前16位和后16位字符

原始返回包:72a9c691ccdaab98fL1tMGI4YTljMn75e3jOBS5/V31Qd1NxKQMCe3h4KwFQfVAEVworCi0FfgB+BlWZhjRlQuTIIB5jMTU=b4c4e1f6ddd2a488

真正内容：fL1tMGI4YTljMn75e3jOBS5/V31Qd1NxKQMCe3h4KwFQfVAEVworCi0FfgB+BlWZhjRlQuTIIB5jMTU=

# 文件取证

### 2021.10 dasctf 《魔法少女雪殇——光与暗的对决》——剧场版
参考资料-- http://www.snowywar.top/?p=2629
FTK_Imageer加载文件，提取出 魔法少女雪殇——光与暗的对决 所有内容。
存在pcm, pkl  -- 就是DCP影院放映格式
```
pcmXXXXX.mxf
pklXXXXX.xml
```
安装 DCP-o-matic 工具。运行 DCP-o-matic 2
添加工程，添加文件无法解析。

根据ASSETMAP的顺序，我们可以知道他的解析顺序是PKL,CPL,J2C,PCM

正常的文件
```
<AssetList>
    <Asset>
      <Id>urn:uuid:b930717c-2ebd-41ee-bf96-4f7eb552912b</Id>
      <AnnotationText>b930717c-2ebd-41ee-bf96-4f7eb552912b</AnnotationText>
      <Hash>NbJAmgRI82AB5Bhyzo/FpBmd0w4=</Hash>
      <Size>9233</Size>
      <Type>text/xml;asdcpKind=CPL</Type>
    </Asset>
    <Asset>
      <Id>urn:uuid:76c03e9e-89fa-476f-82c1-3830c08ec5a7</Id>
      <AnnotationText>76c03e9e-89fa-476f-82c1-3830c08ec5a7</AnnotationText>
      <Hash>5aGsAqrh48aUfuPSKtVMoAOaOoY=</Hash>
      <Size>2518301586</Size>
      <Type>application/x-smpte-mxf;asdcpKind=Picture</Type>
    </Asset>
    <Asset>
      <Id>urn:uuid:9b04a14b-2bfd-42d0-9788-bfd3e5d54ad6</Id>
      <AnnotationText>9b04a14b-2bfd-42d0-9788-bfd3e5d54ad6</AnnotationText>
      <Hash>7EH1FaDkSggILH7pC+isiipNODI=</Hash>
      <Size>118034594</Size>
      <Type>application/x-smpte-mxf;asdcpKind=Sound</Type>
    </Asset>
  </AssetList>
```
此题文件
```
  <Creator>DCP-o-matic 2.14.55 af98c4c415</Creator>
  <AssetList>
  </AssetList>
```

PKL出了问题。 PKL的格式为
```
<Asset>
    <ld>urn:uuid:(文件名那个uuid)</ld>
    <AnnotationText>(同上)</AnnotationText>
    <Hash>openssl sha1 -binary "文件名" | openssl base64</Hash>
    <Size>stat 文件就可以看</Size>
    <Type>类型</Type>
</Asset>
```

整理后
```
  <AssetList>
    <Asset>
        <Id>urn:uuid:b56bffec-4634-4484-b754-b5978645390d</Id>
        <AnnotationText>b56bffec-4634-4484-b754-b5978645390d</AnnotationText>
        <Hash>HBDdtFWZyW2WPVms3N3RqF5BK9U=</Hash>
        <Size>9375</Size>
         <Type>text/xml;asdcpKind=CPL</Type>
    </Asset>
    <Asset>
      <Id>urn:uuid:ec979cf7-811c-43e0-968c-015dfb201e77</Id>
      <AnnotationText>ec979cf7-811c-43e0-968c-015dfb201e77</AnnotationText>
      <Hash>2nspCospkqJM/pHLmH+vqhvzr/I=</Hash>
      <Size>108059598</Size>
      <Type>application/x-smpte-mxf;asdcpKind=Picture</Type>
    </Asset>
    <Asset>
      <Id>urn:uuid:db891f03-6b85-4627-9a1c-49750bf6ced4</Id>
      <AnnotationText>db891f03-6b85-4627-9a1c-49750bf6ced4</AnnotationText>
      <Hash>WZD30AEOA76Uk7cSKsrYQg0pGl8=</Hash>
      <Size>12106358</Size>
      <Type>application/x-smpte-mxf;asdcpKind=Sound</Type>
    </Asset>
  </AssetList>
```
KDM当作密钥就好。
KDM文件在删除的文件夹中，一起恢复一下。还有个exe，拉进ida是个加密。

```c
int encrypto()
{
  FILE *v1; // [esp+18h] [ebp-10h]
  FILE *Stream; // [esp+1Ch] [ebp-Ch]
  FILE *v3; // [esp+1Ch] [ebp-Ch]

  Stream = fopen("KDM.zip", "rb");
  if ( !Stream )
    return printf(&byte_40A076);
  for ( i = 0; i <= 9; ++i )
  {
    fread(&res[i], 2u, 1u, Stream);
    res[i] ^= 0xBF52u;
  }
  fseek(Stream, 0, 2);
  length = ftell(Stream);
  fclose(Stream);
  v1 = fopen("hack", "wb");
  v3 = fopen("KDM.zip", "rb");
  if ( !v1 )
    return printf(&byte_40A062);
  for ( i = 0; i <= 9; ++i )
    fwrite(&res[i], 2u, 1u, v1);
  fseek(v3, 20, 0);
  while ( length / 2 > i )
  {
    fread(&temp, 2u, 1u, v3);
    fwrite(&temp, 2u, 1u, v1);
    ++i;
  }
  fclose(v3);
  fclose(v1);
  return printf(&Format);
}
```

DCP-o-matic 新建工程，添加dcp。选中修复后的文件夹。

出现视频。提示需要KDM。右击左侧视频文件，添加KDM。

# 内存取证
## 2021 dasctf oct 卡比卡比卡比
题目里有2个文件，一个内存文件，一个 `!@#$unimportance` 奇怪文件。

volatility -f raw.raw --profile=Win7SP1x64 pslist

有cmd.exe和iexplore.exe

先看看iehistory一下看看历史记录

volatility -f raw.raw --profile=Win7SP1x64 pslist iehistory

python3 vol.py -f ../raw.raw windows.filescan>02filescan.txt

发现key.png. dump出来 

```vol3
python3 vol.py -f ../raw.raw windows.dumpfiles --physaddr 0x3e5e94c0
```

找开一看是文本，提示有个视频文件。过滤video。找到ohhhh。dump出来是 xzkbyyds!  不知道什么的key。

cmd进程，cmdscan一下，发现输入了5201314

```
volatility -f raw.raw --profile=Win7SP1x64 cmdscan
```

去 filescan搜一下。dump出来。是个zip。要密码。用xzkbyyds!解压不了。

再找管理员密码。

volatility -f raw.raw --profile=Win7SP1x64 mimikatz>password.txt

得到 MahouShoujoYyds 解压zip得到exp。和题目的 `!@#$unimportance` 有关系。

```py
import struct
key = 'xxxxxxxxx'
fp = open('!@#$importance', 'rb')
fs = open('!@#$unimportance', 'wb')
data = fp.read()
for i in range(0, len(data)):
    result = struct.pack('B', data[i] ^ ord(*key[i % len(key)]))
    fs.write(result)
fp.close()
fs.close()
```

key 前面收集到一个 `xzkbyyds!` 解一下。
```py
import struct
key = 'xzkbyyds!'
# fp = open('!@#$importance', 'rb')
fs = open('!@#$unimportance', 'rb')
fe = open('ex', 'wb')
data = fs.read()
for i in range(0, len(data)):
    result = struct.pack('B', data[i] ^ ord(*key[i % len(key)]))
    fe.write(result)
fe.close()
fs.close()
```
是个gif。里面有 flag。