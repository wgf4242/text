import sys
from ctypes import *

if sys.platform == 'win32':
	print(cdll.msvcrt.srand(1))
	print(cdll.msvcrt.rand())

if sys.platform == 'linux':
	libc = cdll.LoadLibrary("/lib/x86_64-linux-gnu/libc.so.6")
    # time0 = libc.time(0)
	libc.srand(1)
	print(libc.rand())

import datetime
date = datetime.datetime(2020, 3, 2)
date_seed = int(date.timestamp())

# #include <stdio.h>
# #include <stdlib.h>

# int main(int argc, char const *argv[])
# {
# 	srand(1);
# 	printf("%d\n", rand());
# 	return 0;
# }