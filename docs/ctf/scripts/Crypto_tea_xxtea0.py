aimport xxtea

enc = [172, 175, 29, 52, 247, 132, 72, 9, 115, 145, 51, 244, 16, 251, 118, 2, 197, 167, 77, 177, 218, 209, 241, 15, 174, 130, 184, 103, 96, 180, 248, 191, 159, 66, 60, 58, 186, 3, 234, 87, 122, 51, 83, 3]
key = [ord(i) for i in "S1ert1ng"] + [0] * (16 - len("S1ert1ng"))
key = (b'S1ert1ng' + b'\x00' * 16)[:16]
print(xxtea.decrypt(bytes(enc), bytes(key), padding=False))
