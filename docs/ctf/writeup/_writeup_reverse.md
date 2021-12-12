
# C
## Thread/多线程

### Youngter-drive
https://github.com/hx1997/CTF-writeups/raw/master/anheng-july-re-youngter-drive/Youngter-drive.exe

程序创建了2个线程运行。交替运行。2个地方执行了x1d(29) 减1.
所以。由于从29开始计算，奇数执行线程1.偶数则字符不变。最后和key2比较。
线程1
```c
void __stdcall __noreturn StartAddress_0(int a1)
{
  while ( 1 )
  {
    WaitForSingleObject(hObject, 0xFFFFFFFF);
    if ( x1d > -1 )
    {
      sub_41112C((int)&Source, x1d);
      --x1d; //执行了-1
      Sleep(0x64u);
    }
    ReleaseMutex(hObject);
  }
}
```
线程2
```c
void __stdcall __noreturn sub_411B10(int a1)
{
  while ( 1 )
  {
    WaitForSingleObject(hObject, 0xFFFFFFFF);
    if ( x1d > -1 )
    {
      Sleep(0x64u);
      --x1d; //也执行了-1
    }
    ReleaseMutex(hObject);
  }
}
```

```c
char *__cdecl sub_41112C(int source, int x1d)
{
  char *result; // eax
  char v3; // [esp+D3h] [ebp-5h]

  v3 = *(_BYTE *)(x1d + source);
  if ( (v3 < 97 || v3 > 122) && (v3 < 65 || v3 > 90) )
    exit(0);
  if ( v3 < 'a' || v3 > 'z' )
  {                                             // upper
    result = pkey1[0];
    *(_BYTE *)(x1d + source) = pkey1[0][*(char *)(x1d + source) - 38];
  }
  else
  {
    result = pkey1[0];                          // lower
    *(_BYTE *)(x1d + source) = pkey1[0][*(char *)(x1d + source) - 96];
  }
  return result;
}
```
# Python
## pyc | DASCTF Oct X 吉林工师 欢迎来到魔法世界～ 魔法叠加

pyc文件
```
03 F3 0D 0A 00 00 00 00 54 93 6F 61 88 07 00 00
E3 00 00 00 00 00 00 00 00 00 00 00 00 5B 00 00
00 40 00 00 00 73 34 01 00 00 71 02 64 00 64 01
6C 00 5A 00 64 02 64 03 64 04 64 05 64 06 64 07
```

这个结构Magic Code是8byte。是python3的。具体哪个版本没看出来。用python3以上版本生成pyc。确认为3.7

结构分析
```
00 40 00 00 00 73 34 01 00 00 71 02 64 00 64 01
```
1. 这里 73是TYPECODE头, 34 01 00 00 是长度。 后面的7102多余删除掉。再把34长度-2 = 32，如下
```
00 40 00 00 00 73 32 01 00 00 64 00 64 01
```
2.将文件头的magic code改下。
```
42 0D 0D 0A 00 00 00 00 54 93 6F 61 88 07 00 00
```

反编译得脚本

```python
import struct
raw91maps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '#', '$', '%', '&', '(', ')', '*', '+', ',', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~', '"']

def encode(arg1):
    """"""
    a1 = 0
    a2 = 0
    res = ''
    for i in range(len(arg1)):
        c = arg1[i:i + 1]
        a1 |= struct.unpack('B', c)[0] << a2
        a2 += 8
        if a2 > 13:
            r2 = a1 & 8191
            if r2 > 88:
                a1 >>= 13
                a2 -= 13
            else:
                r2 = a1 & 16383
                a1 >>= 14
                a2 -= 14
            res += l2[(r2 % 91)] + l2[(r2 // 91)]

    if a2:
        res += l2[(a1 % 91)]
        if a2 > 7 or a1 > 90:
            res += l2[(a1 // 91)]
    return res


l2 = []
l3 = []
fp = input('plz input O0O0O0O0000O0O00O:\n')
for i in range(0, 52):
    l2 = raw91maps[i:] + raw91maps[0:i]
    fp = encode(fp.encode('utf-8'))

dic = open('./00.txt', 'a')
dic.write(fp)
dic.close
```

解码脚本
```python
# -*- coding:utf-8 -*-
import struct
rawb91Maps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '#', '$',
           '%', '&', '(', ')', '*', '+', ',', '.', '/', ':', ';', '<', '=',
           '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~', '"']
def decode(encoded_str:bytes):
    ''' Decode Base91 string to a bytearray '''
    v = -1
    b = 0
    n = 0
    out = b''
    for strletter in encoded_str.decode():
        if not strletter in b91Table:
            continue
        c = b91Table[strletter]
        if v < 0:
            v = c
        else:
            v += c * 91
            b |= v << n
            n += 13 if (v & 8191) > 88 else 14
            while True:
                out += struct.pack('B', b & 255)
                b >>= 8
                n -= 8
                if not n > 7:
                    break
            v = -1
    if v + 1:
        out += struct.pack('B', (b | v << n) & 255)
    return out
 
b91MapArr = []
for i in range(0, 52):
    b91MapArr.append(rawb91Maps[i:] + rawb91Maps[0:i])
b91MapArr.reverse()
with open("/home/kali/Desktop/00.txt", "rb") as f:
    strs = f.read()
 
for i in range(0, 52):
    b91Table = dict((v, k) for k, v in enumerate(b91MapArr[i]))
    strs = decode(strs).decode()
    print("round:", i)
 
print(strs)
```