#include <stdio.h>
#include <time.h>
#include "stdlib.h"

int main()
{
    struct tm strtime;
    time_t timeoftheday;

    strtime.tm_year = 2021;
    strtime.tm_mon = 1;
    strtime.tm_mday = 23;
    strtime.tm_hour = 4;
    strtime.tm_min = 56;
    strtime.tm_sec = 00;
     strtime.tm_isdst = 0;

    timeoftheday = mktime(&strtime);
    printf(ctime(&timeoftheday));

    // srand(time(&timeoftheday));
    // srand(1);
    srand(ctime(&timeoftheday));
    // char buff[20];
    // strftime(buff, 20, "%b %d %H:%M", timeoftheday);
    for (int i = 0; i < 33; ++i) {
//        printf("%d\n", rand());
         printf("%d--%d\n", rand(), i);
    }
    return 0;
}