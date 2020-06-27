# python3
from pwn import *
print(asm('XCHG EAX,ESP\nRET\nMOV ECX,[EAX]\nMOV [EDX],ECX\nPOP EBX\nRET'.lower()).hex())
a = asm('XCHG EAX,ESP\nRET\nMOV ECX,[EAX]\nMOV [EDX],ECX\nPOP EBX\nRET'.lower())
print(a.hex())
# 94c38b08890a5bc3