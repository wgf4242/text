tee random1.c <<-'EOF'
#include <stdlib.h>
#include <time.h>

void set_seed() {
   time_t seed = time(NULL);
   srand(seed);
}

int random_number() {
   return rand();
}
EOF

# gcc -shared -o random1.so random1.c
gcc -fPIC -shared random1.c -o random1.so 

tee main.py <<-'EOF'
import ctypes
# 加载动态链接库
lib = ctypes.CDLL('./random1.so')
lib.random_number.restype = ctypes.c_int
# 调用C语言的set_seed函数
lib.set_seed()
# 调用C语言的random_number函数
result = lib.random_number()
print(result)
EOF

python3 main.py