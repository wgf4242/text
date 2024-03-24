from z3 import *
from functools import reduce
enc = "kcGXlcG9ihRqlYy5"
maps = StringVal("3GHIJKLMNOPQRSTUb=cdefghijklmnopWXYZ/12+406789VaqrstuvwxyzABCDEF5")
sol = reduce(Concat, [Int2BV(If(i == '=', 0, IndexOf(maps, i, 0)), 6) for i in enc])
arr = reversed([chr(simplify(Extract(i + 7, i, sol)).as_long()) for i in range(0, sol.size(), 8)])
print("".join(arr))