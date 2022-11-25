import CreateSubkey as cs
import F_function as f

# 十六进制转二进制比特串
Hex2bin = lambda m: [val for x in list(m) for val in f"{x:08b}"]

# 二进制比特串转十六进制
bin2Hex = lambda txt: bytes([int(''.join(txt[i:i + 8]), 2) for i in range(0, 64, 8)])


# 按照DES算法的流程图进行运算
def Encryption(plaintext, key):
    text = Hex2bin(plaintext)
    keybit = Hex2bin(key)

    keylist = cs.Subkey(keybit)
    text1 = f.IP(text, 0)  # IP置换
    L = text1[:32]
    R = text1[32:64]
    for i in range(16):
        tmp = R
        tmp = f.Extend(tmp)
        tmp = f.Xor(tmp, keylist[i])
        tmp = f.S_replace(tmp)
        tmp = f.P_replace(tmp)
        tmp = f.Xor(tmp, L)
        L = R
        R = tmp
    L, R = R, L
    ctext = L
    ctext.extend(R)
    ctext = f.IP(ctext, 1)
    return bin2Hex(ctext)


def Decryption(ptext, key):
    text = Hex2bin(ptext)
    keybit = Hex2bin(key)

    keylist = cs.Subkey(keybit)
    text1 = f.IP(text, 0)  # IP置换
    L = [text1[i] for i in range(32)]
    R = [text1[i] for i in range(32, 64)]
    for i in range(16):
        tmp = R
        tmp = f.Extend(tmp)
        tmp = f.Xor(tmp, keylist[15 - i])
        tmp = f.S_replace(tmp)
        tmp = f.P_replace(tmp)
        tmp = f.Xor(tmp, L)
        L = R
        R = tmp
    L, R = R, L
    ctext = L
    ctext.extend(R)
    ctext = f.IP(ctext, 1)
    return bin2Hex(ctext)
