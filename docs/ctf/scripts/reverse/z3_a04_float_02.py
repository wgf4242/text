from z3 import *


# 定义一个浮点数问题的近似解法
def solve_float_problem():
    s = Solver()
    # 假设我们想找到一个x，使得x^2接近于2（这里用有理数的区间来逼近）
    x = Real('x')  # 使用Real类型表示有理数
    # 定义一个误差范围，例如我们接受x^2在1.99到2.01之间的解
    epsilon = 0.01
    s.add(1.99 <= x * x)
    s.add(x * x <= 2.01)

    # 检查是否存在解
    if s.check() == sat:
        model = s.model()
        r = model[x]
        x2 = r.as_fraction()
        v = float(x2)
        # x_float = float(x2.numerator) / float(x2.denominator)
        print(f"找到一个解: x = {v}, 其平方大约是: {v ** 2}")
    else:
        print("无解")


# 调用函数求解
solve_float_problem()
