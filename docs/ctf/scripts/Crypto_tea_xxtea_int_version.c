#include <stdint.h>
#include <stdio.h>

#define DELTA -0x61C88647
#define MX (((z>>5^y<<2) + (y>>3^z<<4)) ^ ((sum^y) + (key[(p&3)^e] ^ z)))

void btea(int *v, int n, int const key[4]) {
    int y, z, sum;
    unsigned p, rounds, e;
    if (n > 1)            /* Coding Part */
    {
        rounds = 6 + 52 / n;
        sum = 0;
        z = v[n - 1];
        do {
            sum += DELTA;
            e = (sum >> 2) & 3;
            for (p = 0; p < n - 1; p++) {
                y = v[p + 1];
                z = v[p] += MX;
            }
            y = v[0];
            z = v[n - 1] += MX;
        } while (--rounds);
    } else if (n < -1)      /* Decoding Part */
    {
        n = -n;
        rounds = 6 + 52 / n;
        sum = rounds * DELTA;
        y = v[0];
        do {
            e = (sum >> 2) & 3;
            for (p = n - 1; p > 0; p--) {
                z = v[p - 1];
                y = v[p] -= MX;
            }
            z = v[n - 1];
            y = v[0] -= MX;
            sum -= DELTA;
        } while (--rounds);
    }
}

void testEncode() {
    uint32_t key[] = {73, 83, 67, 67};
    int v[] = {
            0x34,0x33,  0x32, 0x31, 0x38,  0x37,
            0x36,0x35,  0x34, 0x33, 0x32,  0x31,
            0x38,0x37,  0x36, 0x35,
            0x39,0x39,
    };
    btea(v, 18, key);
    for (int i = 0; i < 32; i++) {
        printf("%X", v[i]);
    }
    printf("\n");
}

void testDecode() {
    uint32_t key[] = {73, 83, 67, 67};
    int v[] = {0x08EA8209, 0xF2177171, 0x5EF47E6C, 0xB0D1EDFE, 0x40871576, 0x244BA09D, 0x133A3341, 0xCDAC6E2A, 0x1C7225DF, 0x1B2F6AA7, 0x0B9D41EB, 0x4D952491, 0xF1531212, 0xF55A292D, 0xE4B525C8, 0xA9E8198C, 0xC8A68659, 0x8FFEA938

    };
    btea(v, -18, key);
    for (int i = 0; i < 32; i++) {
        printf("%X", v[i]);
    }
    printf("\n");
}

int main() {
    testEncode();
    testDecode();
}
// 9b34a61df773acf0e4dec25ea5fb0e29