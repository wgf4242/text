#include <stdio.h>
#include <stdint.h>

uint32_t key[4] = {0x4445, 0x4144, 0x4245, 0x4546};

void encrypt(uint32_t v0, uint32_t v1) {
    uint32_t sum = 0, i;             // set up
    uint32_t delta = 0x9e3779b9;                       // a key schedule constant
    for (i = 0; i < 32; i++) {                         // basic cycle start
        sum += delta;
        v0 += ((v1 << 4) + key[0]) ^ (v1 + sum) ^ ((v1 >> 5) + key[1]);
        v1 += ((v0 << 4) + key[2]) ^ (v0 + sum) ^ ((v0 >> 5) + key[3]);
    }                                                // end cycle
    printf("%x", v0);
    printf("%x", v1);
}

void decrypt(uint32_t v0, uint32_t v1) {
    uint32_t index = 0x9e3779b9;
    uint32_t sum = index * 32;
    for (int i = 0; i < 32; i++) {
        v1 -= ((((v0 << 4) + key[2]) ^ (v0 + sum)) ^ ((v0 >> 5) + key[3]));
        v0 -= ((((v1 << 4) + key[0]) ^ (v1 + sum)) ^ ((v1 >> 5) + key[1]));
        sum -= index;
    }
    printf("%x", v0);
    printf("%x", v1);
}

int main() {

    uint32_t v1[3] = {0x3E8947CB, 0x31358388, 0xDA627361};
    uint32_t v2[3] = {0xCC944639, 0x3B0B6893, 0x3B2E6427};
    for (int i = 0; i < 3; i++)
        decrypt(v1[i], v2[i]);
    return 0;
}
//XBvfaEdQvbcrxPBh8AOcJ6gA