"""
点阵坐标转文字 2023年国家基地“楚慧杯”网络空间安全实践能力竞赛-Q组\Misc\gb2312-80
0,0,4080,3072,3072,3072,4032,3680,48,48,48,3120,1632,960,0,0
0,0,992,1584,3096,3096,3096,3096,3096,3096,3096,3096,1584,992,0,0
"""
f = open('cipher.txt', 'r', encoding='utf8')
txt = f.read().splitlines()
txt =txt[1:]

fp = open('out.txt', 'w', encoding='utf8')
for line in txt:
    x = eval(line)
    for e in x :
        dots = f"{e:016b}".replace('0', '. ').replace('1', '0 ') # 0看着清楚一些
        fp.write(dots+'\n')
    fp.write('\n')

print(txt)