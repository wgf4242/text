import angr
import sys
def main(argv):
    bin_path=argv[1]
    p=angr.Project(bin_path)

    start_addr=0x08048699

    init_state=p.factory.blank_state(addr=start_addr)

    print("ESP:",init_state.regs.esp)

    buffer0=0x7fff0000-0x100
    buffer1=0x7fff0000-0x200

    buffer0_addr=0x0ABCC8A4
    buffer1_addr=0x0ABCC8AC

    init_state.memory.store(buffer0_addr,buffer0,endness=p.arch.memory_endness)
    init_state.memory.store(buffer1_addr,buffer1,endness=p.arch.memory_endness)

    p1=init_state.solver.BVS("p1",8*8)
    p2=init_state.solver.BVS("p2",8*8)

    init_state.memory.store(buffer0,p1)
    init_state.memory.store(buffer1,p2)

    sm=p.factory.simgr(init_state)

    def is_good(state):
        return b'Good Job.'in state.posix.dumps(1)

    def is_bad(state):
        return b'Try again.' in state.posix.dumps(1)
    sm.explore(find=is_good,avoid=is_bad)

    if sm.found:
        found_state=sm.found[0]
        pass1=found_state.solver.eval(p1)
        pass2=found_state.solver.eval(p2)
        print("Solution: {} {}".format(pass1,pass2))
    else:
        raise Exception("Solution nou found")

if __name__=='__main__':
    main(sys.argv)
