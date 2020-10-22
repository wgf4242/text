WMCTF2020 Writeup



# Reverse

## 0x1 easy_re

x64dbg 打开文件，F8运行，在某个call提示输入结束了。

00000000004038CC | E8 0FDE0000              | call perl.4116E0                        |

4038CC这里，F7进入

0000000000411866 | E8 E5EEFFFF              | call perl.410750                        |

这个411866 call又结束了，F7跟进，F8单步走着走着有显示flag了。

`WMCTF{I_WAnt_dynam1c_F1ag}`

# Misc

## 0x1 Happy Birthday

daolnwod.zip 打不开，用010 editor看到最后是KP, 一看套路就是逆向数据

```python
filename = 'daolnwod.zip'

def reverse_file(filename):
    file = open(filename, 'rb')
    data =file.read()
    data_reversed = data[::-1]
    f = open(new_name(filename), 'wb')
    f.write(data_reversed)
    f.close()

def new_name(filename):
    f,ext = filename.split('.')
    return f[::-1] + '.' + ext


if __name__ == '__main__':
    reverse_file(filename)
```
解压出来flag `WMCTF{Happy_birthd4y_XMAN><}`


# other writeup
[WMCTF 部分pwn题解](https://mp.weixin.qq.com/s/POEBBiwuR3lP-u-85sA0KQ)
[WMCTF-WriteUp](https://mp.weixin.qq.com/s/SddIi7Om8BACyo_X1Skdfg)
[WMCTF2020 部分Writeup&招新帖](https://mp.weixin.qq.com/s/Njf67W2-H2EjV-_mZGC0eQ)
[【Android CTF】wmctf2020 reverse easy_apk](https://mp.weixin.qq.com/s/H-15XL4pWZOEsSzZM793EQ)

