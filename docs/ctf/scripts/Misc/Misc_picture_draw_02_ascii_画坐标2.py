"""
010 editor 默认用 Droid Sans Mono 看
MS Gothic
楷体 看得比较清楚

题目: 我爱Linux
"""
import pickle
import re

fp = open("data", "rb+")
''' 打开序列化文件 '''
fw = open('pickle.txt', 'w')
''' 打开保存文件 '''
a = pickle.load(fp)
''' 反序列化文件编译 '''
pickle = str(a)
''' 转换成字符串要不然不能保存 '''
fw.write(pickle)
''' 写入文件 '''
fw.close()
''' 关闭文件 '''
fp.close()
''' 关闭文件 '''

file = "output2.txt"
f = open(file, "w")

fw = open("pickle.txt", "r")
text = fw.read()
i = 0
a = 0

while i < len(text):
    if (text[i] == ']'):
        print('\n', file=f)
        a = 0
    elif (text[i] == '('):
        if (text[i + 2] == ','):
            b = text[i + 1]
            d = text[i + 1]
            b = int(b) - int(a)
            c = 1
            while c < b:
                print(" ", end="", file=f)
                c += 1
            print(text[i + 5], end="", file=f)
            a = int(d)
        else:
            b = text[i + 1] + text[i + 2]
            d = text[i + 1] + text[i + 2]
            b = int(b) - int(a)
            c = 1
            while c < b:
                print(" ", end="", file=f)
                c += 1
            print(text[i + 6], end="", file=f)
            a = int(d)
    i += 1

# f.close()

f.close()
txt = open(file, "r").read()
txt = re.sub("\n+", "\n", txt)

f = open('output3.txt', 'w')
f.write(txt)
f.close()
