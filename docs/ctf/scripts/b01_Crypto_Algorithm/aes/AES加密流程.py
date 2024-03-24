# NKCTF2024 login_system
s = list(b'aaaabaaacaaadaaa')
enc = bytes.fromhex('B0CC93EAE92FEF5699396E023B4F9E42')

sbox = [0x75736572, 0x30315F6E, 0x6B637466, 0x32303234, 0x77AAD1AB, 0x479B8EC5, 0x2CF8FAA3, 0x1EC8C897, 0xB36CEC5F, 0xF4F7629A, 0xD80F9839, 0xC6C750AE, 0x45681283, 0xB19F7019,
        0x6990E820, 0xAF57B88E, 0x50A1DF51, 0xE13EAF48, 0x88AE4768, 0x27F9FFE6, 0x295C1C46, 0xC862B30E, 0x40CCF466, 0x67350B80, 0x52C7CCC4, 0x9AA57FCA, 0xDA698BAC, 0xBD5C802C,
        0xC617B9C1, 0x5CB2C60B, 0x86DB4DA7, 0x3B87CD8B, 0x76A04870, 0x2A128E7B, 0xACC9C3DC, 0x974E0E57, 0xE27E554D, 0xC86CDB36, 0x64A518EA, 0xF3EB16BD, 0x4E7450B4, 0x86188B82,
        0xE2BD9368, 0x115685D5, 0x4E7450B4, 0x86188B82, 0xE2BD9368, 0x115685D5, 0xE27E554D, 0xC86CDB36, 0x64A518EA, 0xF3EB16BD, 0x76A04870, 0x2A128E7B, 0xACC9C3DC, 0x974E0E57,
        0xC617B9C1, 0x5CB2C60B, 0x86DB4DA7, 0x3B87CD8B, 0x52C7CCC4, 0x9AA57FCA, 0xDA698BAC, 0xBD5C802C, 0x295C1C46, 0xC862B30E, 0x40CCF466, 0x67350B80, 0x50A1DF51, 0xE13EAF48,
        0x88AE4768, 0x27F9FFE6, 0x45681283, 0xB19F7019, 0x6990E820, 0xAF57B88E, 0xB36CEC5F, 0xF4F7629A, 0xD80F9839, 0xC6C750AE, 0x77AAD1AB, 0x479B8EC5, 0x2CF8FAA3, 0x1EC8C897,
        0x75736572, 0x30315F6E, 0x6B637466, 0x32303234, 0xA0637780, 0x00007F01, 0xA04D8CFA, 0x00007F01]
byte_555C126E7040 = bytes.fromhex(
    '31525AC80BACF33A8B54279BAB95DE8360CB537FC4E30A97E029D568C5DFF47BAAD642786CE97017D737244975A9896703FAD991B45BC24E92FC46B17308C77409AFECF54D2DEAA5DAEFA62B7E0C8FB004066284158E121D44C0E238D44728456E9D63CFE68C18821B2CEE879410C120074AA4EB77BCD3E1662A6BE779CC8616D0D119553C9FFB3098BDB8F19E61CD90CE7C8D57AE6AB33D76A77188A2BA4F3E40640F482135362FE8145D51D8B5FED29693A1B6430D4C80C9FFA3DD720559BF0E26341F13E5DCF2C6501EE485B7398ACAED9CBB56231AF03258B265336F41BE3F6D1100AD5FC38125A8A09AF6F75E99222E4BF93B027AB95C69F81CDB017DFD')

print(len(sbox) * 4)
print(len(byte_555C126E7040))


def transpose(s):
    # 4x4 纵向填充
    lst = [None] * 16
    for i in range(4):
        for j in range(4):
            lst[j * 4 + i] = s[i * 4 + j]
    return lst


def xor_cipher(a1, v13):
    lst = []
    for row in range(4):
        for j in range(4):
            c = a1[4 * row + j] ^ (v13[j] >> (8 * (3 - row)) & 0xff)
            lst.append(c)
    return lst


def sub_bytes(vin):
    lst = []
    for row in range(4):
        for j in range(4):
            c = byte_555C126E7040[vin[4 * row + j]]
            lst.append(c)
    return lst


def shift_rows(arr):
    # 分组4x4, i从0开始, 第i行循环左移i次
    for row in range(4):
        lst_r = arr[row * 4:(row + 1) * 4]
        arr[row * 4:(row + 1) * 4] = lst_r[row:] + lst_r[:row]
    return arr


def Galois_Field(a1, a2):
    v5 = 0
    for i in range(8):
        if ((a1 & 1) != 0):
            v5 ^= a2
        v7 = a2 & 0x80
        a2 <<= 1
        if v7:
            a2 ^= 0x1b
        a1 >>= 1
    return v5


def mix_columns(a1):
    matrix = [0] * 4
    matrix[0] = 0x1010302
    matrix[1] = 0x1030201
    matrix[2] = 0x3020101
    matrix[3] = 0x2010103

    v9 = [None] * 16
    for row in range(4):
        for j in range(4):
            v9[4 * row + j] = a1[4 * row + j]

    lst = []
    for row in range(4):
        for m in range(4):
            v1 = Galois_Field(matrix[row] & 0xff, v9[m] & 0xff)
            v2 = Galois_Field(matrix[row] >> 8 & 0xff, v9[m + 4]) ^ v1
            v3 = Galois_Field(matrix[row] >> 16 & 0xff, v9[m + 8]) ^ v2
            c = v3 ^ Galois_Field(matrix[row] >> 24 & 0xff, v9[m + 12])
            c &= 0xff
            lst.append(c)
    return lst


v11Idx = 0
# initial round 初始变换
s2 = transpose(s)
s2 = xor_cipher(s2, sbox)

# 9 main round
for i in range(1, 10):
    v11Idx += 4
    s2 = sub_bytes(s2)
    s2 = shift_rows(s2)
    s2 = mix_columns(s2)
    xor_cipher(s2, sbox[v11Idx:])

# final round
s2 = sub_bytes(s2)
s2 = shift_rows(s2)
s2 = xor_cipher(s2, sbox[v11Idx + 4:])
s2 = transpose(s2)
