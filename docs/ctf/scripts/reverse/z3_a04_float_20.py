import z3

solver = z3.SimpleSolver()  # 如果 unknown用 solver


def abs(x):
    return z3.If(x >= 0, x, -x)


# 定义 Z3 的 Real 类型变量
in1 = 9636.363
in2 = 9469.46
in3 = z3.Real("in3")  # 将Python浮点数转换为Z3的Real
temp6 = z3.Real('temp6')

# 现在所有操作数都是 Z3 Real 类型，可以进行加法运算
temp1 = in1 + in2 + 0 + in3
temp2 = temp1 / 3
temp3 = abs(in1 - temp2)
temp4 = abs(in2 - temp2)
temp5 = abs(in3 - temp2)
temp6 = z3.If(z3.And(temp3 >= temp4, temp3 >= temp5), in1, temp6)
temp6 = z3.If(z3.And(temp3 <= temp4, temp4 >= temp5), in2, temp6)
temp6 = z3.If(z3.And(temp3 <= temp5, temp4 <= temp5), in3, temp6)

out = (temp1 - temp6) / 2
solver.add(out == 9498.563)

print(solver.check())
res = solver.model()
print(res)
val = lambda x: float(x.as_fraction())
r3 = res[in3]
# v3 = float(r3.as_fraction())
v3 = val(r3)
print(f'{v3=}')

"""
c1:
  temp3>=temp4 && temp3>=temp5 , temp6=in1
c2:
  temp3<=temp4 && temp4>=temp5 , temp6=in2
c3:
  temp3<=temp5 && temp4<=temp5 , temp6=in3
out=(temp1-temp6) /2 == 9498.563
"""
