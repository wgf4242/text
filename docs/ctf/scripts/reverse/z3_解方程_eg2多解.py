# 只添加了首字母遍历的解
from natsort import natsorted
from z3 import BitVec, Solver, sat, And, Or

enc = bytes.fromhex('02180FF8190427D8EB0035484D2A456B592E4301185C09090909B57D')

solver = None
condition = []


def add_condition(flag):
    global solver
    solver = Solver()

    solver.add(And(condition))
    for i in range(1, 28):
        solver.add(flag[i - 1] - 32 > 0)
        solver.add(flag[i - 1] - 128 < 0)
        flag[i - 1] ^= (flag[i - 1] % 17 + flag[i]) ^ 0x19
    for i in range(28):
        solver.add(flag[i] == enc[i])


def print_data(m):
    lst = natsorted([(k, m[k]) for k in m], lambda x: str(x[0]))
    for k, v in lst:
        print(chr(v.as_long()), end='')
    print('')


while True:
    flag = [BitVec('s1_%d' % i, 8) for i in range(28)]  # 有时得用int值好使
    if locals().get('value'): condition.append(flag[0] != value)
    add_condition(flag)

    if not solver.check() == sat:
        break
    m = solver.model()
    print_data(m)

    get_value = lambda k: [m[key] for key in m if str(key) == k][0]
    value = get_value(f's1_0').as_long()

    # s.add(Or(condition))
    # s.add(And(condition))
