import angr
import claripy
import sys


def main(argv: sys.argv):
    path_to_binary = argv[1]
    project = angr.Project(path_to_binary)

    # 这里选在ignore_me之后，把栈变量清理之后地址处
    start_address = 0x80488bc
    initial_state = project.factory.blank_state(
        addr=start_address,
        add_options={
            angr.options.SYMBOL_FILL_UNCONSTRAINED_MEMORY,
            angr.options.SYMBOL_FILL_UNCONSTRAINED_REGISTERS
        }
    )
    filename = "FOQVSBZB.txt"
    symbolic_file_size_bytes = 8

    password = claripy.BVS('password', symbolic_file_size_bytes * 8)
    password_file = angr.storage.SimFile(filename, content=password)

    initial_state.fs.insert(filename, password_file)

    simulation = project.factory.simgr(initial_state)

    def is_successful(state: angr.SimState):
        stdout_output = state.posix.dumps(sys.stdout.fileno())
        return b'Good Job.' in stdout_output

    def should_abort(state: angr.SimState):
        stdout_output = state.posix.dumps(sys.stdout.fileno())
        return b'Try again.' in stdout_output

    simulation.explore(find=is_successful, avoid=should_abort)

    if simulation.found:
        solution_state = simulation.found[0]  # type: angr.SimState

        solution = solution_state.solver.eval(password, cast_to=bytes).decode()
        print(solution)

    else:
        raise Exception('Could not find the solution')


if __name__ == "__main__":
    main(sys.argv)
