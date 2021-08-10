from Crypto.Cipher import ARC4
from Crypto.Hash import SHA
from Crypto.Random import get_random_bytes
import base64


def rc4_encrypt(plain, key):
    cipher = ARC4.new(key)
    msg = cipher.encrypt(plain)
    return base64.b64encode(msg)


def rc4_decrypt(msg, key):
    cipher = ARC4.new(key)
    txt = base64.b64decode(msg)
    return cipher.decrypt(txt)


# nonce = get_random_bytes(16)
# tempkey = SHA.new(key+nonce).digest()

# hello
# 123456
# U2FsdGVkX18R2EchFoOOMYN3GDxx

if __name__ == '__main__':
    key = b'123456'
    enc = rc4_encrypt(b'hello', key)
    print(enc)
    print(rc4_decrypt(enc, key))
