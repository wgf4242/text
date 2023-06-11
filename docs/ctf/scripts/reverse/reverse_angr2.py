import angr   #导入angr
import claripy    #导入claripy
proj = angr.Project("./ais3_crackme")    #载入文件
argv1 = claripy.BVS('argv1',50*8)    #B是bit 1字节=8bit  猜测输入不多于50字节 就是50*8
state = proj.factory.entry_state(args=['./ais3_crackme',argv1])
simgr = proj.factory.simgr(state)
simgr.explore(find=0x400602,avoid=0x40060E)    #成功位置及失败位置
print(simgr.found[0].solver.eval(argv1))    #转成ascll码输出
print(simgr.found[0].solver.eval(argv1,cast_to=bytes))    #直接输出字符