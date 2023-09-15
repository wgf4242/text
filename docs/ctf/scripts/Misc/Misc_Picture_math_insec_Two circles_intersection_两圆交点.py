"""三裂偏移
data.txt 每行3个点+半径, 可以确定3个圆,通过3个圆确定交点
(661, 103)-655.3388436526558;(665, 218)-640.7261505510759;(230, 231)-206.81392603013947;
(548, 320)-524.7856705360771;(975, 198)-951.433129547211;(1179, 250)-1153.1110094002224;
"""
import math
import re


def insec(p1, r1, p2, r2):
    x = p1[0]
    y = p1[1]
    R = r1
    a = p2[0]
    b = p2[1]
    S = r2
    d = math.sqrt((abs(a - x)) ** 2 + (abs(b - y)) ** 2)
    if d > (R + S) or d < (abs(R - S)):
        print("Two circles have no intersection")
        return
    elif d == 0 and R == S:
        print("Two circles have same center!")
        return
    else:
        A = (R ** 2 - S ** 2 + d ** 2) / (2 * d)
        h = math.sqrt(R ** 2 - A ** 2)
        x2 = x + A * (a - x) / d
        y2 = y + A * (b - y) / d
        x3 = round(x2 - h * (b - y) / d, 2)
        y3 = round(y2 + h * (a - x) / d, 2)
        x4 = round(x2 + h * (b - y) / d, 2)
        y4 = round(y2 - h * (a - x) / d, 2)
        s0 = {(x3, y3), (x4, y4)}
        return s0


def go():
    lst = []
    f = open('data.txt', 'r', encoding='utf8')
    txt = f.read()
    for line in txt.splitlines():
        res = line.strip(';').split(";")
        a1, a2, a3 = res

        "'(661, 103)-655.3388436526558'"
        p1, r1 = get_param(a1)
        p2, r2 = get_param(a2)
        p3, r3 = get_param(a3)
        rs = insec(p1, r1, p2, r2)
        rs2 = insec(p3, r3, p2, r2)
        point = rs & rs2
        lst.append(point)

    f1 = open('point.txt', 'w', encoding='utf8')
    for line in lst:
        x,y = line.pop()
        f1.write(f"{x} {y}\n")
    f1.close()


def get_param(a1):
    m = re.search(r"\((\d+), (\d+)\)(.*)", a1).groups()
    p1 = float(m[0]), float(m[1])
    r1 = float(m[2][1:])
    return p1, r1


go()
