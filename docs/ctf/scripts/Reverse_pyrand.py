import sys
from ctypes import *

if sys.platform == 'win32':
	print(cdll.msvcrt.srand(1))
	print(cdll.msvcrt.rand())

if sys.platform == 'linux':
	libc = cdll.LoadLibrary("/lib/x86_64-linux-gnu/libc.so.6")
	libc.srand(1)
	print(libc.rand())



# #include <stdio.h>
# #include <stdlib.h>

# int main(int argc, char const *argv[])
# {
# 	srand(1);
# 	printf("%d\n", rand());
# 	return 0;
# }