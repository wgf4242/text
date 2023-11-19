# 2023工业信息安全技能大赛\钢铁行业锦标赛\_05easy_vm\05.zip
# 需要改汇编puts出来加密后的结果

from pwn import *

s = process('./easy_vm')

input_value = "abbaaaaaaaaaaaaaaaaa"
target_output = "d9e1d5c9f8b8d5fdd3f2fdd0b6cfe4f68bddd3f2"
characters = ''.join(c for c in string.printable if c not in string.whitespace)


def get_output(s: process):
    out_enc = s.recvuntil(b'\n', drop=True)
    return out_enc.hex()


for i in range(len(input_value)):
    for char in characters:
        s.recvline()  # b'please input flag\n' , TODO:测试流程
        test_value = list(input_value)
        test_value[i] = char
        test_value = ''.join(test_value)
        s.sendline(test_value)

        output = get_output(s)
        print(f"Trying with input '{test_value}' -> Output: '{output}'")
        if output[i * 2:(i + 1) * 2].lower() == target_output[i * 2:(i + 1) * 2]:
            input_value = test_value
            print(f"Character at position {i + 1} found: '{char}' -> Current input: {input_value}")
            break
