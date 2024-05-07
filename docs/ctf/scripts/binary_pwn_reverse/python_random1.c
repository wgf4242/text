#include <stdio.h>
#include <stdlib.h>
#include <time.h>

time_t get_timestamp(int year, int month, int day);
void brute_force_hash_check(time_t seed, const int *string, size_t len);

int main(void) {
    int target[] = {239,99,223,211};
    time_t start_seed = get_timestamp(2024, 4, 13);
    time_t end_seed = get_timestamp(2024, 4, 14);

    // for (time_t seed = 0; seed < 0x10000; ++seed) {
    for (time_t seed = start_seed; seed < end_seed; ++seed) {
        brute_force_hash_check(seed, target, sizeof target / sizeof target[0]);
    }
    return 0;
}

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

void brute_force_hash_check(time_t seed, const int *string, size_t len) {
    srand((unsigned) seed);
    for (size_t i = 0; i < len; ++i) {
        int rand_num = rand() & 0xff;
        // int rand_num = rand() % 0xff;
        if (rand_num != string[i]) {
            break;
        } else if (i == len - 1) {
            printf("final get, seed is %lu\n", seed);
            exit(0);
        }
    }
}