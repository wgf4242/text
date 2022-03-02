z3条件要 a-b == result

在一些程序语言，比如C，C++，C#，Java，有符号整数和无符号整数在位向量的层面上没有任何区别。然而，z3为有符号数与无符号数提供了不同的运算操作版本。在z3py中，运算符<, <=, >, >=, /, %和>>用于有符号数，而无符号数对应的操作符是ULT, ULE, UGT, UGE, UDiv, URem 和 LShR。

z3类型
```python
from z3 import *
a = Int('a')    # 声明变量为整数类型。
b = Real('b')   # 声明变量为实数类型。
c = Bool('c')   # 声明变量为bool类型。
d = IntVector('d', 3)   # 声明变量为int类型数组。
# << >> 移位运算要转为乘法和除法
```

```python
# Create to bit-vectors of size 32
from z3 import *
x, y = BitVecs('x y', 32)
# x, y = BitVecs('x y', 64)
 
solve(x + y == 2, x > 0, y > 0)
 
# Bit-wise operators
# & bit-wise and
# | bit-wise or
# ~ bit-wise not
solve(x & y == ~y)
 
solve(x < 0)
 
# using unsigned version of < 
solve(ULT(x, 0))
```
```py
from z3 import *

x = Real('x')
y = Real('y')
s = Solver()
s.add(x + y > 5, x > 1, y > 1)
print(s.check())
print(s.model())
```

# 数组 if else
```py
from z3 import *
l = [Int("l%d"%i) for i in range(0x2a)]
s = Solver()
for i in l:
    s.add(i>0)
    s.add(i<255)
```
# 数组 if else
```py
from z3 import *
import z3
s1 = [BitVec('s1_%d' % i, 8) for i in range(2)]  # 有时得用int值好使
key = [80, 120]

s = Solver()
for i, n in enumerate(key):
    con1 = If(And(64 < s1[i], s1[i] <= 90), s1[i] - key[i] == 0, True)
    con2 = If(And(96 < s1[i], s1[i] <= 122), s1[i] - key[i] == 0, True)
    s.add(con1)
    s.add(con2)
print(s.check())
print(s.model())
```

## 实例 [ACTF新生赛2020]rome
实现C语言中这样的效果
```c
for ( i = 0; i <= 15; ++i )
{
if ( flag[i] > 64 && flag[i] <= 90 )
  flag[i] = (flag[i] - 51) % 26 + 65;
if ( flag[i] > 96 && flag[i] <= 122 )
  flag[i] = (flag[i] - 79) % 26 + 97;
}
for ( i = 0; i <= 15; ++i )
{
result = key[i];
if ( flag[i] != result )
  return result;
}
```

```py
import string

from z3 import *

# Cae3ar_th4_Gre@t
print(list(b'Cae3ar_th4_Gre@t'))
key = list(b"Qsw3sj_lz4_Ujw@l")
s1 = [BitVec(f's1_{i:04}', 8) for i in range(len(key))]

s = Solver()
for i, n in enumerate(key):
    con1 = If(And(64 < s1[i], s1[i] <= 90), (s1[i] - 51) % 26 + 65 == key[i], s1[i]==key[i])
    con2 = If(And(96 < s1[i], s1[i] <= 122), (s1[i] - 79) % 26 + 97 == key[i], con1)
    s.add(con2)
print(s.check())
res = s.model()

lst = sorted([(k, res[k]) for k in res], key=lambda x: str(x[0]))
print([x.as_long() for a, x in lst])
for a, b in lst:
    print(chr(b.as_long()), end='')
```