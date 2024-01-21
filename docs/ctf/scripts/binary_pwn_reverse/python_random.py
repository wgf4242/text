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





def rand_win():
    return cdll.msvcrt.rand()

def rand_win_ff():
    return cdll.msvcrt.rand() % 0xff

enc = [0x09, 0x63, 0xD9, 0xF6, 0x58, 0xDD, 0x3F, 0x4C, 0x0F, 0x0B, 0x98, 0xC6, 0x65, 0x21,
       0x41, 0xED, 0xC4, 0x0B, 0x3A, 0x7B, 0xE5, 0x75, 0x5D, 0xA9, 0x31, 0x41, 0xD7, 0x52,
       0x6C, 0x0A, 0xFA, 0xFD, 0xFA, 0x84, 0xDB, 0x89, 0xCD, 0x7E, 0x27, 0x85, 0x13, 0x08]

def process(seed):
    cdll.msvcrt.srand(seed)
    lst_rand = []
    for i in range(42):
        lst_rand.append(rand_win_ff())
    if lst_rand[0] ^ enc[0] == ord('f'):
        if lst_rand[11] ^ enc[11] == ord('l'):
            print('1 get', seed)
            if lst_rand[12] ^ enc[12] == ord('g'):
                print('2 get', seed)
                if lst_rand[32] ^ enc[32] == ord('a'):
                    print('GET ------ ')
                    print(seed)
                    exit(0)


def bruteforce():
    date = datetime.datetime(2023, 4, 22)
    date_seed = int(date.timestamp())
    for seed in range(date_seed, date_seed + 1054099200, 1):
        process(seed)


bruteforce()
