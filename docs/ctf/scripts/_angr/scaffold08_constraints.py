# 添加约束，防止路径爆炸if ( check_equals_AUPDNNPROEZRJWKB((int)&buffer, 0x10u) )，因为这种compare是属于一个字符一个字符进行比较，所以路径太多，需要添加约束。

# The binary asks for a 16 character password to which is applies a complex
# function and then compares with a reference string with the function
# check_equals_[reference string]. (Decompile the binary and take a look at it!)
# The source code for this function is provided here. However, the reference
# string in your version will be different than AABBCCDDEEFFGGHH:
#
# #define REFERENCE_PASSWORD = "AABBCCDDEEFFGGHH";
# int check_equals_AABBCCDDEEFFGGHH(char* to_check, size_t length) {
#   uint32_t num_correct = 0;
#   for (int i=0; i<length; ++i) {
#     if (to_check[i] == REFERENCE_PASSWORD[i]) {
#       num_correct += 1;
#     }
#   }
#   return num_correct == length;
# }
#
# ...
#
# char* input = user_input();
# char* encrypted_input = complex_function(input);
# if (check_equals_AABBCCDDEEFFGGHH(encrypted_input, 16)) {
#   puts("Good Job.");
# } else {
#   puts("Try again.");
# }
#
# The function checks if *to_check == "AABBCCDDEEFFGGHH". Verify this yourself.
# While you, as a human, can easily determine that this function is equivalent
# to simply comparing the strings, the computer cannot. Instead the computer
# would need to branch every time the if statement in the loop was called (16
# times), resulting in 2^16 = 65,536 branches, which will take too long of a
# time to evaluate for our needs.
#
# We do not know how the complex_function works, but we want to find an input
# that, when modified by complex_function, will produce the string:
# AABBCCDDEEFFGGHH.
#
# In this puzzle, your goal will be to stop the program before this function is
# called and manually constrain the to_check variable to be equal to the
# password you identify by decompiling the binary. Since, you, as a human, know
# that if the strings are equal, the program will print "Good Job.", you can
# be assured that if the program can solve for an input that makes them equal,
# the input will be the correct password.

import angr
import claripy
import sys


def main(argv: sys.argv):
    path_to_binary = argv[1]
    project = angr.Project(path_to_binary)

    start_address = 0x804863c
    initial_state = project.factory.blank_state(
        addr=start_address,
        add_options={
            angr.options.SYMBOL_FILL_UNCONSTRAINED_MEMORY,
            angr.options.SYMBOL_FILL_UNCONSTRAINED_REGISTERS
        }
    )

    password = claripy.BVS('password', 8 * 16)

    password_address = 0x804a040
    initial_state.memory.store(password_address, password)

    simulation = project.factory.simgr(initial_state)

    address_to_check_constraint = 0x8048683
    simulation.explore(find=address_to_check_constraint)

    if simulation.found:
        solution_state = simulation.found[0]  # type: angr.SimState

        constraint_parameter_address = 0x804a040
        constraint_parameter_size_bytes = 16
        constraint_parameter_size_bitvector = solution_state.memory.load(
            constraint_parameter_address,
            constraint_parameter_size_bytes
        )

        constraint_parameter_desired_value = "OSIWHBXIFOQVSBZB".encode()

        solution_state.add_constraints(constraint_parameter_size_bitvector == constraint_parameter_desired_value)

        solution = solution_state.solver.eval(password, cast_to=bytes).decode()
        print(solution)
    else:
        raise Exception('Could not find the solution')


if __name__ == "__main__":
    main(sys.argv)
