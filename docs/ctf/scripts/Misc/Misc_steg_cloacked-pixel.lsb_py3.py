"""
python3 lsb.py mmm.png out.txt 123456
python3 lsb.py mmm.png out.txt 10000.txt
python3 lsb.py <stego_file> <out_file> <password or wordlist_file>"
"""

import struct
import sys
from pathlib import Path

import cv2
import numpy as np

def solve(data_hex, wordlist_file):
    f = open(wordlist_file, 'r', encoding='utf8')
    keys = f.read().splitlines()

    for key_plain in keys:
        extract(data_hex, key_plain)


def extract(data_hex, key_plain):
    import hashlib
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import unpad
    block_size = 16
    bs = 32  # block_size

    iv = data_hex[:32]
    iv = bytes.fromhex(iv)
    key = hashlib.sha256(key_plain.encode()).digest()
    data = bytes.fromhex(data_hex)
    enc = data[block_size:]

    cryptor = AES.new(key, AES.MODE_CBC, iv)
    plain_text = cryptor.decrypt(enc)
    try:
        text = unpad(plain_text, bs)
        print(text)
        print(key_plain)
        fout_file.write(repr(text) + '\n')
        fout_file.write(key_plain + '\n')
    except:
        pass


def setUp(stego_file, out_file, password):
    img = cv2.imread(stego_file)
    cv_color = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    res = cv_color & [1, 1, 1]
    res = res.flatten().astype(np.int8)

    global baes_enc
    baes_enc = assemble(res)
    f = open('aes_enc1.txt', 'w', encoding='utf8')
    f.write(baes_enc.hex())
    f.close()

    global fout_file
    fout_file = open(out_file, 'w')

    if Path(password).is_file():
        solve(baes_enc.hex(), password)
    else:
        extract(baes_enc.hex(), password)

    fout_file.close()


def assemble(b):
    num_elements = len(b)
    num_padded_elements = (num_elements + 7) // 8 * 8  # 向上取整到最近的8的倍数
    b_padded = np.pad(b, (0, num_padded_elements - num_elements), mode='constant')

    # 重新塑造为8列
    padded = b_padded.reshape(-1, 8)

    c = padded.dot(2 ** np.arange(8, dtype=np.uint8)[::-1])
    bts = c.astype(np.int8).tobytes()  # b'AA'

    payload_size = struct.unpack("i", bts[:4])[0]
    return bts[4: payload_size + 4]


def usage(progName):
    print("LSB steganogprahy. Hide files within least significant bits of images.\n")
    print("Usage:")
    print("  %s <stego_file> <out_file> <password or wordlist_file>" % progName)
    sys.exit()


if __name__ == "__main__":
    if len(sys.argv) < 3:
        usage(sys.argv[0])

    stego_file = sys.argv[1]
    out_file = sys.argv[2]
    password = sys.argv[3]
    setUp(stego_file, out_file, password)
