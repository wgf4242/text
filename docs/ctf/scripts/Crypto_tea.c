#include <stdio.h>
#include <stdint.h>
#include <string.h>

uint32_t key[4];
uint32_t delta;
unsigned int num_rounds;

void encrypt(uint32_t v0, uint32_t v1) {
    uint32_t sum = 0, i;             // set up
    for (i = 0; i < 32; i++) {                         // basic cycle start
        sum += delta;
        v0 += ((v1 << 4) + key[0]) ^ (v1 + sum) ^ ((v1 >> 5) + key[1]);
        v1 += ((v0 << 4) + key[2]) ^ (v0 + sum) ^ ((v0 >> 5) + key[3]);
    }                                                // end cycle
    printf("%x", v0);
    printf("%x", v1);
}

void decrypt(uint32_t v[2]) {
    int sum = delta * num_rounds;
    uint32_t v0 = v[0], v1 = v[1];
    for (int i = 0; i < num_rounds; i++) {
        v1 -= ((((v0 << 4) + key[2]) ^ (v0 + sum)) ^ ((v0 >> 5) + key[3]));
        v0 -= ((((v1 << 4) + key[0]) ^ (v1 + sum)) ^ ((v1 >> 5) + key[1]));
        sum -= delta;
    }
    printf("%x", v0);
    printf("%x", v1);
}

int main() {
    setbuf(stdout, 0);

    delta = 0x9e3779b9; // 0x9e3779b9 == -0x61C88647
    uint32_t k[4] = {0x4445, 0x4144, 0x4245, 0x4546};
    uint32_t v[] = {0x3E8947CB, 0xCC944639, 0x31358388, 0x3B0B6893, 0xDA627361, 0x3B2E6427};
    num_rounds = 32;

    size_t vlen = sizeof(v) / 4 ; // int: 4bytes
    memcpy(key, k, sizeof(k));

    for (int i = 0; i < vlen; i+=2) // 每次处理2个, 指针向前走2步
        decrypt(&v[i]);
    return 0;
}
// 5842766661456451766263727850426838414f634a366741
// XBvfaEdQvbcrxPBh8AOcJ6gA