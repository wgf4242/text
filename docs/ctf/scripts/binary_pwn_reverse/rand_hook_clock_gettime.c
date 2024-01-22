// [挂钩clock_gettime](https://mp.weixin.qq.com/s/ksGjGGeYjvWpgmRA5xyBpg)
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <dlfcn.h>
#include <time.h>

typedef int (*PFN_clock_gettime)(clockid_t clock_id, struct timespec *tp);

int clock_gettime(clockid_t clock_id, struct timespec *tp)
{
    void *handle = dlopen("libc.so.6", RTLD_LAZY);
    PFN_clock_gettime real = (PFN_clock_gettime)dlsym(handle, "clock_gettime");
    
    int res = real(clock_id, tp);
    int ts = atoi(getenv("TS_VALUE"));
    tp->tv_sec = ts;
    // printf("clock_gettime: %ld\n", tp->tv_sec);
    return res;
}

// gcc hook.c -shared -o hook.so