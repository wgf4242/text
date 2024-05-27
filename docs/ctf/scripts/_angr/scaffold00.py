import angr
import sys

def main(argv):
  path_to_binary = '00_angr_find'  # :string
  project = angr.Project(path_to_binary)

  initial_state = project.factory.entry_state()
  # ./2 flag 命令行参数输入
  # symbolic_argv1 = claripy.BVS("argv1", 100 * 8)
  # initial_state = project.factory.entry_state(args=["./2", symbolic_argv1])

  simulation = project.factory.simgr(initial_state)

  print_good_address = 0x804867D  # :integer (probably in hexadecimal)
  simulation.explore(find=print_good_address)

  if simulation.found:
    solution_state = simulation.found[0]

    print(solution_state.posix.dumps(sys.stdin.fileno()))
  else:
    raise Exception('Could not find the solution')

if __name__ == '__main__':
  main(sys.argv)
