import angr
import sys

def main(argv):
    bin_path=argv[1]
    p=angr.Project(bin_path)
    start_addr=0x08048601
    init_state=p.factory.blank_state(addr=start_addr)

    p1=init_state.solver.BVS('p1',64)  
    p2=init_state.solver.BVS('p2',64)
    p3=init_state.solver.BVS('p3',64)
    p4=init_state.solver.BVS('p4',64)
    p4_addr=0x0A1BA1D8
    p3_addr=0x0A1BA1D0
    p2_addr=0x0A1BA1C8
    p1_addr=0x0A1BA1C0

    init_state.memory.store(p1_addr,p1)
    init_state.memory.store(p2_addr,p2)
    init_state.memory.store(p3_addr,p3)
    init_state.memory.store(p4_addr,p4)

    sm=p.factory.simgr(init_state)

    def is_good(state):
        return b'Good Job.' in state.posix.dumps(1)

    def is_bad(state):
        return b'Try again.' in state.posix.dumps(1)

    sm.explore(find=is_good,avoid=is_bad)

    if sm.found:
        found_state=sm.found[0]
        pass1=found_state.solver.eval(p1,cast_to=bytes)
        pass2=found_state.solver.eval(p2,cast_to=bytes)
        pass3=found_state.solver.eval(p3,cast_to=bytes)
        pass4=found_state.solver.eval(p4,cast_to=bytes)
        print("Solution:{} {} {} {}".format(pass1.decode('utf-8'),pass2.decode('utf-8'),pass3.decode('utf-8'),pass4.decode('utf-8')))
    else:
        raise Exception("Solution not found")
if __name__=="__main__":
    main(sys.argv)

