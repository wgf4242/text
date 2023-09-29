tee mystrcmp1.c <<-'EOF'
// gcc -m32 -shared -O2 mystrcmp.c -o mystrcmp1.so
#include "stdio.h"

int strcmp(const char *s1, const char *s2){
    static  int counter = 0;
    printf("%02d strcmp called!\n", counter++);

    while (*s1 && (*s1 == *s2)) {
        ++s1;
        ++s2;
    }

    return 0;
}
EOF
gcc -m32 -shared -O2 mystrcmp1.c -o mystrcmp1.so

tee mystrcmp2.c <<-'EOF'
// gcc -m32 -shared -O2 mystrcmp2.c -o mystrcmp.so
#include "stdio.h"

int strcmp(const char *s1, const char *s2){
    printf("strcmp called!\n");

    while (*s1 && (*s1 == *s2)) {
        ++s1;
        ++s2;
    }

    return *s1 - *s2;
}
EOF

gcc -m32 -shared -O2 mystrcmp2.c -o mystrcmp2.so

tee test1.py <<-'EOF'
from pwn import *

p = process('./moveAside', env={'LD_PRELOAD': './mystrcmp1.so'})
p.sendline('1')
recv = p.recvall(timeout=0.01).decode()
print(recv, end='')
print(f'count: 42 = 41+1')
EOF

python3 test1.py
echo 'pause'
read nn

tee test1.py <<-'EOF'
from pwn import *
import string

context.log_level = 'error'

ans = ''

for i in range(42):
    for ch in string.printable:
        current_flag = ans + ch # '' + 'f' right:3 line false: 2line
        print(current_flag)
        p = process('./moveAside', env={'LD_PRELOAD': './mystrcmp2.so'})
        p.recvline()
        p.sendline(current_flag.encode())
        recv = p.recvall(timeout=0.01)
        recvs = recv.splitlines()
        if len(recvs) > len(ans) + 2:
            ans += ch
            break

EOF

python3 test2.py
