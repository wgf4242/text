#include <stdint.h>
#include <stdio.h>

#define DELTA 0x33445566
#define MX (((z>>5^y<<2) + (y>>3^z<<4)) ^ ((sum^y) + (key[(p&3)^e] ^ z)))
uint8_t ida_chars[] =
        {
                0x5C, 0xAB, 0x3C, 0x99, 0x29, 0xE1, 0x40, 0x3F, 0xDE, 0x91,
                0x77, 0x77, 0xA6, 0xFE, 0x7D, 0x73, 0xE6, 0x59, 0xCF, 0xEC,
                0xE3, 0x4C, 0x60, 0xC9, 0xA5, 0xC0, 0x82, 0x96, 0x1E, 0x2A,
                0x6F, 0x55
        };
uint32_t key[] = {
        0x36B0, 0x13816, 0x10, 0x1E0F3
};
void btea(uint32_t *v, int n, uint32_t const key[4])
{
    uint32_t y, z, sum;
    unsigned p, rounds, e;
    if (n > 1)            /* Coding Part */
    {
        rounds = 6 + 52/n;
        sum = 0;
        z = v[n-1];
        do
        {
            sum += DELTA;
            e = (sum >> 2) & 3;
            for (p=0; p<n-1; p++)
            {
                y = v[p+1];
                z = v[p] += MX;
            }
            y = v[0];
            z = v[n-1] += MX;
        }
        while (--rounds);
    }
    else if (n < -1)      /* Decoding Part */
    {
        n = -n;
        rounds = 6 + 52/n;
        sum = rounds*DELTA;
        y = v[0];
        do
        {
            e = (sum >> 2) & 3;
            for (p=n-1; p>0; p--)
            {
                z = v[p-1];
                y = v[p] -= MX;
            }
            z = v[n-1];
            y = v[0] -= MX;
            sum -= DELTA;
        }
        while (--rounds);
    }
}
int main() {
    uint32_t *p = (uint32_t *)ida_chars;
    btea(p, -8, key);
    for(int i = 0; i < 32; i ++ ) {
        printf("%c", ida_chars[i]);
    }
}
// 9b34a61df773acf0e4dec25ea5fb0e29