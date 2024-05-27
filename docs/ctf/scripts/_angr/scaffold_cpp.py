import angr
import claripy

p = angr.Project('3')

# 创建flag,其长度为28
flag_chars = [claripy.BVS(f'{i}', 8) for i in range(28)]
# 程序使用 gets函数 进行输入，所以在flag末尾加上'\n',让程序知道读完了
flag = claripy.Concat(*flag_chars + [claripy.BVV(b'\n')])

# 如果要使用CPP的库函数，就要用 full_init_state
state = p.factory.full_init_state(
    args=['./3'],
    # 设置unicorn引擎，因为我们必须深入到C ++标准库中才能正常工作
    add_options={angr.options.unicorn},
    # 设置输入为我们前面创建的flag
    stdin=flag,
)

# 接下来就是常规操作了
simgr = p.factory.simgr(state)
simgr.explore(find=0x40E2AF, avoid=0x40E36C)

if simgr.found:
    print(simgr.found[0].posix.dumps(0))