import angr
proj = angr.Project("./r100",auto_load_libs=False)
state = proj.factory.entry_state()
simgr = proj.factory.simgr(state) 
simgr.explore(find=0x400844,avoid=0x400855) # 0x400844 =>输出正确答案的地址, 0x400855 错误跳转到erorr的地址
a = simgr.found[0].posix.dumps(0)
print(a) # 直接跑出答案