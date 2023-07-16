"""
先秀 py2 lsb.py extract mmm.png out.txt lovekfc 提取出加密的 aes数据 再用下面爆破
python lsb_bf.py <words.txt> <enc_hex>
python lsb_bf 10000.txt ee77267876ce39c51d7f4a48d0c88007ac04d354af60b5edcdbe6f04c208b863f6f588af3034fb4666729325904c0a03fed19b494509b33e8c4f4f0ee1cde50c46d642b6315e24823b5352e4cbe62ba8
"""
import sys
from Crypto.Util.Padding import unpad
from Crypto.Cipher import AES

import hashlib

def solve(filename, data_hex):
    f = open(filename, 'r', encoding='utf8')
    keys = f.read().splitlines()

    for key_plain in keys:
        iv = data_hex[:32]

        block_size = 16

        data = bytes.fromhex(data_hex)
        key = hashlib.sha256(key_plain.encode()).digest()
        enc = data[block_size:]
        iv = bytes.fromhex(iv)

        cryptor = AES.new(key, AES.MODE_CBC, iv)
        plain_text = cryptor.decrypt(data[block_size:])
        bs = 32  # block_size
        try:
            print(unpad(plain_text, bs))
            print(key_plain)
        except:
            pass


if __name__ == "__main__":
    if len(sys.argv) < 2:
        "[-] Usage: python lsb_bf.py <words.txt> <enc_hex>"
    filename = sys.argv[1]
    data_hex = sys.argv[2]
    solve(filename, data_hex)
