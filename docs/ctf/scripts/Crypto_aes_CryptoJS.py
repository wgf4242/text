# https://blog.51cto.com/lang13002/6723766
import base64
from hashlib import md5

from Crypto.Cipher import AES
from Crypto import Random


def pad(s):
    return s + (16 - len(s) % 16) * chr(16 - len(s) % 16).encode()


def unpad(s):
    return s[0:-ord(s[len(s) - 1:])]


def bytes_to_key(data, salt, output=48):
    assert len(salt) == 8, len(salt)
    data += salt
    key = md5(data).digest()
    final_key = key
    while len(final_key) < output:
        key = md5(key + data).digest()
        final_key += key
    return final_key[:output]


def encrypt(data, passphrase):
    salt = Random.new().read(8)
    key_iv = bytes_to_key(passphrase, salt, 32 + 16)
    key = key_iv[:32]
    iv = key_iv[32:]
    aes = AES.new(key, AES.MODE_CBC, iv)
    cipherbyte = base64.b64encode(b"Salted__" + salt + aes.encrypt(pad(data)))
    return cipherbyte


def decrypt(data, passphrase):
    data = base64.b64decode(data)
    assert data[:8] == b'Salted__'
    salt = data[8:16]
    key_iv = bytes_to_key(passphrase, salt, 32 + 16)
    key = key_iv[:32]
    iv = key_iv[32:]
    aes = AES.new(key, AES.MODE_CBC, iv)
    plainbyte = unpad(aes.decrypt(data[16:]))
    return plainbyte


if __name__ == '__main__':
    data = b'123456'
    passphrase = b'0123456789asdfgh'

    # encrypt_data = encrypt(data, passphrase)
    # print('encrypt_data:', encrypt_data)

    encrypt_data = b"U2FsdGVkX18hyuQnNnZyAe7emBZrUR/YGmy90QN1DI4="

    decrypt_data = decrypt(encrypt_data, passphrase)
    print('decrypt_data:', decrypt_data)
