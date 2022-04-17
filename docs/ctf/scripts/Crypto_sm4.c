#include <stdio.h>

/**
 *	作用: 参数 x 左移参数 n 位
 */
#define SHL(x, n) ( ((x) & 0xFFFFFFFF) << n )

/**
 *	作用: 参数 x 逻辑左移参数 n 位
 */
#define ROTL(x, n) ( SHL((x), n) | ((x) >> (32 - n)) )

/**
 *	密钥用常量
 */
static const unsigned long FK[4] = {0xa3b1bac6, 0x56aa3350, 0x677d9197, 0xb27022dc};

/**
 *	密钥用常量
 */
static const unsigned long CK[32] =
        {
                0x00070e15, 0x1c232a31, 0x383f464d, 0x545b6269,
                0x70777e85, 0x8c939aa1, 0xa8afb6bd, 0xc4cbd2d9,
                0xe0e7eef5, 0xfc030a11, 0x181f262d, 0x343b4249,
                0x50575e65, 0x6c737a81, 0x888f969d, 0xa4abb2b9,
                0xc0c7ced5, 0xdce3eaf1, 0xf8ff060d, 0x141b2229,
                0x30373e45, 0x4c535a61, 0x686f767d, 0x848b9299,
                0xa0a7aeb5, 0xbcc3cad1, 0xd8dfe6ed, 0xf4fb0209,
                0x10171e25, 0x2c333a41, 0x484f565d, 0x646b7279
        };

unsigned int CalcRoundKey(unsigned int ka);

void SetKey(unsigned int SK[32], unsigned char key[16]);

int main(void) {
    unsigned int t[36];
    unsigned int k[] = {0xFD07C452, 0xEC90A488, 0x68D33CD1, 0x96F64587};
    int i, j;

    for (i = 32; i < 36; i++) {
        t[i] = k[i - 32];
        printf("0x%X, ", t[i]);
    }

    for (i = 35; i >= 4; i--)
        t[i - 4] = t[i] ^ (CalcRoundKey(t[i - 3] ^ t[i - 2] ^ t[i - 1] ^ CK[i - 4]));

    for (i = 0; i < 4; i++) {
        //		printf("0x%X, ", t[i] ^ FK[i]);
        t[i] ^= FK[i];
    }

    printf("Date:");
    unsigned char *p = (unsigned char *) t;
    for (i = 1; i <= 2; i++)
        for (j = 1; j <= 4; j++)
            printf("%c", p[i * 4 - j]);

    return 0;
}

unsigned int CalcRoundKey(unsigned int ka) {
    unsigned int retval = 0;
    int i;

    retval = ka ^ (ROTL(ka, 13) ^ ROTL(ka, 23));

    return retval;
}