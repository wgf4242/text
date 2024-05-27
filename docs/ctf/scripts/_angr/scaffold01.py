import angr
import sys

def main(argv):
  path_to_binary = '01_angr_avoid' # ???
  project = angr.Project(path_to_binary)
  initial_state = project.factory.entry_state()
  simulation = project.factory.simgr(initial_state)

  print_good_address = 0x080485E0  # ???
  will_not_succeed_address = 0x080485EF  # ???
  simulation.explore(find=print_good_address, avoid=will_not_succeed_address)
  # will_not_succeed_address = [0x40060E, 0x4005DA]  # 可用数组
  # simulation.explore(find=print_good_address, avoid=will_not_succeed_address)

  if simulation.found:
    solution_state = simulation.found[0]
    print(solution_state.posix.dumps(sys.stdin.fileno()))
  else:
    raise Exception('Could not find the solution')

if __name__ == '__main__':
  main(sys.argv)
