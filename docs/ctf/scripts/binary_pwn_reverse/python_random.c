#pragma ide diagnostic ignored "cert-msc50-cpp"
#pragma ide diagnostic ignored "cert-msc51-cpp"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void process(time_t seed, const int *string);

time_t get_timestamp(int year, int month, int day) {
    struct tm timeinfo;
    time_t timestamp;

    timeinfo.tm_year = year - 1900;
    timeinfo.tm_mon = month - 1;
    timeinfo.tm_mday = day;
    timeinfo.tm_hour = 0;
    timeinfo.tm_min = 0;
    timeinfo.tm_sec = 0;
    timeinfo.tm_isdst = -1;

    timestamp = mktime(&timeinfo);

    return timestamp;
}


int main(void) {
    setbuf(stdout, NULL);


    time_t start = get_timestamp(2023, 1, 1);
    time_t end = get_timestamp(2025, 1, 1);
    int string[] = {5, 85, 47, 190, 0};
    for (time_t i = start; i < end; ++i) {
        process(i, string);
    }
    printf("Not found\n");

}

void process(time_t seed, const int *string) {
    srand(seed);
    for (int i = 0; i < 4; ++i) {
        if ((rand() & 0xff) != string[i])
            break;

        if (i > 1) {
            printf("%d get, seed is %lld\n", i, seed);
        }
        if (i == 3) {
            printf("final get, seed is %lld\n", seed);
            exit(0);
        }
    }
}
