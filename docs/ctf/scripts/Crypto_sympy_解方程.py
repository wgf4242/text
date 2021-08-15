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