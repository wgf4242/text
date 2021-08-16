import sympy as sy
# 一元一次方程
x = sy.symbols("x") # 申明未知数"x"
a = sy.solve((x+(1/5)*x-240),[x]) # 写入需要解的方程体
print(a)

# 二元一次方程
x,y = sy.symbols("x y")
a = sy.solve([3*x-2*y-3,x+2*y-5],[x,y])
print(a)
# {x: 2, y: 3/2}


# z3解方程
# 解 f1+f2 =a, f1**3 + f2**3 = b
from z3 import *
x, y, z = z3.Ints('x y z')
solver = z3.SimpleSolver()  # 如果 unknown用 solver
# solver = z3.Solver()

c1 = 2732509502629189160482346120094198557857912754
c2 = 5514544075236012543362261483183657422998274674127032311399076783844902086865451355210243586349132992563718009577051164928513093068525554

solver.add(x + y == c1)
solver.add(x**3 + y**3 == c2)

print(solver.check())
if solver.check() == z3.sat:
    print(solver.model())
    print(solver.model().eval(x))
