#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <Windows.h>

void fdec() {
    __int64 dq_key = 88777897;
    BYTE flag[] = {
            0x4D, 0xB8, 0x76, 0x29, 0xF5, 0xA9, 0x9E, 0x59,
            0x55, 0x56, 0xB1, 0xC4, 0x2F, 0x21, 0x2C, 0x30,
            0xB3, 0x79, 0x78, 0x17, 0xA8, 0xED, 0xF7, 0xDB,
            0xE1, 0x53, 0xF0, 0xDB, 0xE9, 0x03, 0x51, 0x5E,
            0x09, 0xC1, 0x00, 0xDF, 0xF0, 0x96, 0xFC, 0xC1,
            0xB5, 0xE6, 0x62, 0x95, 0x01, 0x00, 0x00, 0x00,
    };
    __int64 p;
    int j, i;
    for (i = 0; i < 6; i++) {
        p = *((__int64 *) &flag[i * 8]);
        for (j = 0; j < 64; j++) {
            if (p & 1) //其实这就是根据某个特征来的
            {
                p = ((unsigned __int64) p ^ dq_key) >> 1;
                p |= 0x8000000000000000;//还原那个符号位1

            } else {
                p = (unsigned __int64) p >> 1;
            }
        }
        *((__int64 *) &flag[i * 8]) = p;
    }
    for (i = 0; i < 48; i++)
        printf("%c", flag[i]);
    printf("\n");
    return;
}

int main(int argc, char *argv[], char **env) {
    fdec();
    return 0;
}