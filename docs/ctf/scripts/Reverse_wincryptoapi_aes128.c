//https://gift1a.github.io/2022/04/23/DASCTF-FATE-Reverse/#more
#include <stdbool.h>
#include <windows.h>
#include <windef.h>
#include <wincrypt.h>
#include <stdio.h>

bool __stdcall encflag(BYTE *key, DWORD dwDataLen, BYTE *input, DWORD *pdwDataLen, DWORD dwBufLen) {
    BOOL v6;
    HCRYPTKEY phKey;
    HCRYPTPROV phProv;
    HCRYPTHASH phHash;

    phProv = 0;
    phHash = 0;
    phKey = 0;
    v6 = CryptAcquireContextA(&phProv, 0, 0, 0x18u, 0xF0000000);
    if (v6) {
        // CryptGetHashParam(phHash, 2u, key, (DWORD *)v8, 0); 在加密函数中会将hash值写入key->addr的值
        v6 = CryptCreateHash(phProv, 0x8003u, 0, 0, &phHash);
        if (v6) {
            v6 = CryptHashData(phHash, key, dwDataLen, 0); // 将key 按hashalg生成 写入key->addr
            if (v6) {
                v6 = CryptDeriveKey(phProv, 0x660Eu, phHash, 1u, &phKey);
                CryptDecrypt(phKey, 0, 1, 0, input, pdwDataLen);
                for (int i = 0; i < 32; ++i) {
                    putchar(input[i]);
                }
            }
        }
    }
    if (phKey)
        CryptDestroyKey(phKey);
    if (phHash)
        CryptDestroyHash(phHash);
    if (phProv)
        CryptReleaseContext(phProv, 0);
    return v6;
}

void main() {
    BYTE flag_data[] = {0x5B, 0x9C, 0xEE, 0xB2, 0x3B, 0xB7, 0xD7, 0x34, 0xF3, 0x1B, 0x75, 0x14, 0xC6, 0xB2, 0x1F, 0xE8,
                        0xDE, 0x33, 0x44, 0x74, 0x75, 0x1B, 0x47, 0x6A, 0xD4, 0x37, 0x51, 0x88, 0xFC, 0x67, 0xE6, 0x60,
                        0xDA, 0x0D, 0x58, 0x07, 0x81, 0x43, 0x53, 0xEA, 0x7B, 0x52, 0x85, 0x6C, 0x86, 0x65, 0xAF, 0xB4};
    BYTE keyBuf[] = {0x5c, 0x53, 0xa4, 0xa4, 0x1d, 0x52, 0x43, 0x7a, 0x9f, 0xa1, 0xe9, 0xc2, 0x6c, 0xa5, 0x90, 0x90};
    DWORD dwDataLen_2;
    DWORD *pdwDataLen = &dwDataLen_2;
    *pdwDataLen = 0x20;
    encflag(keyBuf, 0x10, flag_data, pdwDataLen, 0x104);
}