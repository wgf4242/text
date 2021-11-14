
在一些程序语言，比如C，C++，C#，Java，有符号整数和无符号整数在位向量的层面上没有任何区别。然而，z3为有符号数与无符号数提供了不同的运算操作版本。在z3py中，运算符<, <=, >, >=, /, %和>>用于有符号数，而无符号数对应的操作符是ULT, ULE, UGT, UGE, UDiv, URem 和 LShR。


```python
# Create to bit-vectors of size 32
x, y = BitVecs('x y', 32)
 
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