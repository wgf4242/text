"""
from Crypto.Cipher import AES
import os
from flag import flag
from Crypto.Util.number import *

def padding(data):
    return data + b"".join([b'\x00' for _ in range(0, 16 - len(data))])

def execute_program():
    secret_data = padding(flag)
    secret_key = os.urandom(16) * 2
    init_vector = os.urandom(16)
    print(bytes_to_long(secret_key) ^ bytes_to_long(init_vector) ^ 1)
    cipher = AES.new(secret_key, AES.MODE_CBC, init_vector)
    encrypted_flag = cipher.encrypt(secret_data)
    print(encrypted_flag)

if __name__ == "__main__":
    execute_program()
#113271863767201424639329153097952947311122854394813183532903131317262533549675
#b'_1\x16\xc2;\xb1\xddy\x14\xdd\x14\xe5{\x19\x04:'
"""
from Crypto.Util.number import *
from Crypto.Cipher import AES

a = 113271863767201424639329153097952947311122854394813183532903131317262533549675
c = b'_1\x16\xc2;\xb1\xddy\x14\xdd\x14\xe5{\x19\x04:'
key = long_to_bytes(a)[:16]
iv = bytes_to_long(key) ^ bytes_to_long(long_to_bytes(a)[16:]) ^ 1

aes = AES.new(key * 2,AES.MODE_CBC,long_to_bytes(iv))
flag = aes.decrypt(c)
print(flag)
# RSAKEYISFTCE
# 密码1 ISFTCE