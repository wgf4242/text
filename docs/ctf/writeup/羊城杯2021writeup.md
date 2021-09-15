# 羊城杯2021 writeup



## 赛博德国人

得到 cookbook.pdf，搜一下walzenlage，发现是enigma密码。

[模拟器](http://enigmamuseum.com/EnigmaSim.zip)

![Snipaste_2021-09-15_14-54-53](羊城杯2021writeup.assets/Snipaste_2021-09-15_14-54-53-16316889112961.png)

```
#encrypted.txt
0911 = 1tle = 1tl = 350 = RZS NAJ=
nkfgp roqad boprv yrdhy zwamf qsrhb owqvt jzotr ffcjq snpqh kpwzm fprru gufez xsuws aohyw xbreu pifbz kagxj blbha jzixj zrasn zxkay lpaza ejwou itcip dfdgp rbjnv xuqzq qhtya xwwik wyybx kdgrc slrkj pgjay aidwa jeszp pbqat njojg jrplb kkhot joqpg vwecj soabm aupsr fenug ybxmr jloch kmjgc tznxl tnrqx pbeph fwymn gpoor pjkkb plkwb kxzeq quorp ipuvs utyae qyzgp mqnai iysse gzsht tsrmv crrkr opuxj tqshv ypdrw rvnzt cstlj 

0911 猜测为接受到信息的日期  
1tle 总共1部分
1tl 第1部分
350 为密文长度为350位
RZS NAJ 为加密转子起始位置解密信号
nkfgp 是2位随机加后3位标志位，去密码表里找到是 TAG为10的密码行
```

![Snipaste_2021-09-15_14-55-58](羊城杯2021writeup.assets/Snipaste_2021-09-15_14-55-58.png)

### 方式1 - 模拟器解码

1. 打开盖子，设置为B型机器 。
   ![Snipaste_2021-09-15_14-57-07](羊城杯2021writeup.assets/Snipaste_2021-09-15_14-57-07.png)

1. 使用2，3，1号转轮，分别调整到05 21 25

通过红色位置点击更换转轮，通过蓝色位置点击切换轮盘号码。
 ![Snipaste_2021-09-15_15-00-18](羊城杯2021writeup.assets/Snipaste_2021-09-15_15-00-18.png)

3.盖上盖。调到RZS输入 NAJ。输出为PKS

![image-20210915150901502](羊城杯2021writeup.assets/image-20210915150901502.png)

4.把PKS作为轮子起始值，进行解密。输入密文。并去掉前五位。即

```
roqad boprv yrdhy zwamf qsrhb owqvt jzotr ffcjq snpqh kpwzm fprru gufez xsuws aohyw xbreu pifbz kagxj blbha jzixj zrasn zxkay lpaza ejwou itcip dfdgp rbjnv xuqzq qhtya xwwik wyybx kdgrc slrkj pgjay aidwa jeszp pbqat njojg jrplb kkhot joqpg vwecj soabm aupsr fenug ybxmr jloch kmjgc tznxl tnrqx pbeph fwymn gpoor pjkkb plkwb kxzeq quorp ipuvs utyae qyzgp mqnai iysse gzsht tsrmv crrkr opuxj tqshv ypdrw rvnzt cstlj 
```

得到

```
VIERSIEBENFUENFSIEBENVIERACHTFUENFVIERSIEBENBERTADREISECHSSECHSZWEIDREINEUNDREISECHSDREISIEBENDREIZWEIDREINULLDREIFUENFSECHSSECHSSECHSFUENFDREISIEBENDREIFUENFDREISIEBENDREINEUNDREIFUENFSECHSSECHSDREIEINSDREINULLDREIVIERDREIACHTDREIFUENFDREISIEBENDREIEINSSECHSDREISECHSSECHSDREIVIERSECHSDREISECHSSECHSSECHSZWEIDREISIEBENDREINULLDREIDREISIEBENDORA
```

都是德文字母。解码一下



```python
from binascii import unhexlify

words = [
    ("0","NULL"),
    ("1","EINS"),
    ("2","ZWEI"),
    ("3","DREI"),
    ("4","VIER"),
    ("5","FÜNF"),
    ("6","SECHS"),
    ("7","SIEBEN"),
    ("8","ACHT"),
    ("9","NEUN"),
    ('A',"ZEHN"),
    ('B',"ELF"),
    ('C',"ZWÖLF"),
    ('E',"VIERZEHN"),
    ('F',"FÜNFZEHN"),
    ("D","DORA"),
    ("5","FUENF"),
    ("B","BERTA"),
]
enc = """VIERSIEBENFUENFSIEBENVIERACHTFUENFVIERSIEBENBERTADREISECHSSECHSZWEIDREINEUNDREISECHSDREISIEBENDREIZWEIDREINULLDREIFUENFSECHSSECHSSECHSFUENFDREISIEBENDREIFUENFDREISIEBENDREINEUNDREIFUENFSECHSSECHSDREIEINSDREINULLDREIVIERDREIACHTDREIFUENFDREISIEBENDREIEINSSECHSDREISECHSSECHSDREIVIERSECHSDREISECHSSECHSSECHSZWEIDREISIEBENDREINULLDREIDREISIEBENDORA"""

for k,v in words:
    enc = enc.replace(v, str(k))
print(enc)
print(unhexlify(enc))
```



### 方式2 - pycipher

全部使用python解码。



```python
from pycipher import Enigma

from string import ascii_uppercase as letter

a, b, c = letter[5 - 1], letter[21 - 1], letter[25 - 1]
enigma = Enigma(settings=('R', 'Z', 'S'), rotors=(2, 3, 1), reflector='B', ringstellung=(a, b, c), steckers=[('A', 'T'), ('B', 'V'), ('C', 'F'), ('E', 'N'), ('G', 'Y'), ('H', 'O'), ('I', 'W'), ('L', 'U'), ('M', 'Z'), ('Q', 'X')])
walzenlage = enigma.decipher('NAJ')
print(walzenlage)

enigma.settings = list(walzenlage)
print(enigma.decipher('roqadboprvyrdhyzwamfqsrhbowqvtjzotrffcjqsnpqhkpwzmfprrugufezxsuwsaohywxbreupifbzkagxjblbhajzixjzrasnzxkaylpazaejwouitcipdfdgprbjnvxuqzqqhtyaxwwikwyybxkdgrcslrkjpgjayaidwajeszppbqatnjojgjrplbkkhotjoqpgvwecjsoabmaupsrfenugybxmrjlochkmjgctznxltnrqxpbephfwymngpoorpjkkbplkwbkxzeqquorpipuvsutyaeqyzgpmqnaiiyssegzshttsrmvcrrkropuxjtqshvypdrwrvnztcstlj'))

```

