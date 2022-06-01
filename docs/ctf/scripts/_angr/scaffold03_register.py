# 自定义起始地址 修改register
import angr
import claripy
import sys

def main(argv):
  path_to_binary = argv[1]
  project = angr.Project(path_to_binary)

  start_address = 0x08048980  # :integer (probably hexadecimal)
  initial_state = project.factory.blank_state(addr=start_address)

  password0_size_in_bits = 32  # :integer
  password0 = claripy.BVS('password0', password0_size_in_bits)  # ???
  password1 = claripy.BVS('password1', 32)  # ???
  password2 = claripy.BVS('password2', 32)  # ???
  

  initial_state.regs.eax = password0  # ???
  initial_state.regs.ebx = password1  # ???
  initial_state.regs.edx = password2  # ???

  simulation = project.factory.simgr(initial_state)

  def is_successful(state):
    stdout_output = state.posix.dumps(sys.stdout.fileno())
    return 'Good Job.'.encode() in stdout_output  # ???

  def should_abort(state):
    stdout_output = state.posix.dumps(sys.stdout.fileno())
    return 'Try again.'.encode() in stdout_output  # ???

  simulation.explore(find=is_successful, avoid=should_abort)

  if simulation.found:
    solution_state = simulation.found[0]

    solution0 = solution_state.se.eval(password0)  # ???
    solution1 = solution_state.se.eval(password1)  # ???
    solution2 = solution_state.se.eval(password2)  # ???
    
    solution =  ' '.join(map('{:x}'.format, [ solution0, solution1, solution2 ]))  # ???  # :string
    print(solution)
  else:
    raise Exception('Could not find the solution')

if __name__ == '__main__':
  main(sys.argv)
