#include <string.h>
#include <math.h>
#include "stdio.h"
#include "defs.h"

__int64 __fastcall enc(unsigned __int8 *in4, char *key, char *out4) {
    return 0;
}

unsigned char keys[] = {126, 31, 25, 117};
unsigned char res[] = {0xC9, 0x47, 0x75, 0x75, 0xB5};

// n 个字节的爆破
void bfChar(char offset, char *out) {
    int size = 4;
    for (int i = 0; i < pow(123 - 33, size); ++i) {
        char src[size];
        int t = i;
        for (int j = 0; j < size; ++j) {
            src[j] = t % (123 - 33) + 33;
            t /= (123 - 33);
        }

        enc(src, keys, out + offset);
        int r = strncmp(out + offset, res + offset, 4);
        if (r == 0) {
            printf("%s\n", src);
            return;
        }
    }
    printf("error , not found\n");
}

int main(int argc, char *argv[], char **env) {
    setbuf(stdout, NULL);
    char out[64] = "\0";
    for (int offset = 0; offset < sizeof(res); offset += 4) {
        bfChar(offset, out + offset);
    }
    return 0;
}


