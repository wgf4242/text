"""
根据末位e3穷举列表
"""
enc = [0x25, 0x15, 0xDF, 0xA2, 0xC0, 0x93, 0xAD, 0x14, 0x46, 0xC5, 0xF, 0x2E, 0x9A, 0xEB, 0x30, 0xF8, 0x20, 0xE9, 0xCB, 0x88, 0xC6, 0xBE, 0x8D, 0xE3]
print(len(enc))
exit()
enc_len = 23
start = [None] * enc_len + [0xe3]

lst = []


def DFS(flag, deep):
    if len(lst) > 30:
        raise Exception
    if deep == 0:
        return lst.append(flag.copy())

    for i in range(255):
        if (i ^ 0x41) ^ (i % 0x12 + flag[deep] + 0x05) == enc[deep - 1]:
            flag[deep - 1] = i
            DFS(flag, deep - 1)


DFS(start, enc_len)
for x in lst:
    print(x)
