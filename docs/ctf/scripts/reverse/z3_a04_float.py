import z3

solver = z3.SimpleSolver()  # 如果 unknown用 solver

in1 = 9636.363
in3 = z3.FP("in3", z3.Float32())  # 将Python浮点数转换为Z3的Float16

solver.add(in3 == in1 - 36.0)
print(solver.check())
res = solver.model()
b = res[in3]
print(b)
print(eval(str(b)))
# 1.171919345855712890625*(2**13)
