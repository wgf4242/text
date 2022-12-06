import claripy

cipher = [0x7A, 0x08, 0x2E, 0xBA, 0xAD, 0xAF, 0x82, 0x8C, 0xEF, 0xD8, 0x0D, 0xF8, 0x99, 0xEB, 0x2A, 0x16, 0x05, 0x43, 0x9F, 0xC8, 0x6D, 0x0A, 0x7F, 0xBE, 0x76, 0x64, 0x2F, 0xA9, 0xAC, 0xF2, 0xC9, 0x47, 0x75, 0x75, 0xB5, 0x33]
key = [0x7E, 0x1F, 0x19, 0x75]
for i in range(0, len(cipher) // 4):
    cur_cipher = cipher[i * 4:(i + 1) * 4]
    inp = [claripy.BVS(f"inp_{i}", 8) for i in range(4)]
    res = [claripy.BVS(f"res_{i}", 8) for i in range(4)]
    v3 = key[3]
    v4 = inp[3]
    v5 = key[0]
    v6 = inp[0]
    v7 = inp[1]
    v8 = key[1]
    v9 = inp[2]
    v10 = (v6 + v4) * (key[0] + v3)
    v11 = key[2]
    v12 = v3 * (v6 + v7)
    v13 = (v3 + v11) * (v7 - v4)
    v14 = v4 * (v11 - v5)
    v15 = v5 * (v9 + v4)
    res[0] = v14 + v10 + v13 - v12
    res[2] = v15 + v14
    res[1] = v6 * (v8 - v3) + v12
    res[3] = v6 * (v8 - v3) + (v8 + v5) * (v9 - v6) + v10 - v15

    s = claripy.Solver()
    for j in range(4):
        s.add(cur_cipher[j] == res[j])
        s.add(inp[j] >= 32)
        s.add(inp[j] <= 125)
    if s.check_satisfiability() == "SAT":
        for j in s.batch_eval(inp, 1):
            for k in j:
                print(chr(k), end="")
# NCTF{f6dffab6-173f-4bb1-a973-62f3f8254eba}
