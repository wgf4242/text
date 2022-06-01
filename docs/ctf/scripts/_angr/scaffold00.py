import angr
import sys

def main(argv):
  path_to_binary = '00_angr_find'  # :string
  project = angr.Project(path_to_binary)

  initial_state = project.factory.entry_state()

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
