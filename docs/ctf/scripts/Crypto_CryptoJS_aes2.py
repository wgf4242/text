#
# Encryption with AES-CBC
# Adapted to work with CryptoJS (crypto-js@3.1.9) with default configuration
#
# Python 2.7.13
# pkcs7==0.1.0
# pycrypto==2.6.1
#
import binascii
import struct
import hashlib
from pkcs7 import PKCS7Encoder
from Crypto.Cipher import AES
from Crypto import Random

MODE = AES.MODE_CBC


def evpKDF(passwd, salt, key_size=8, iv_size=4, iterations=1, hash_algorithm="md5"):
    """
    https://github.com/Shani-08/ShaniXBMCWork2/blob/master/plugin.video.serialzone/jscrypto.py
    """
    target_key_size = key_size + iv_size
    derived_bytes = b""
    number_of_derived_words = 0
    block = None
    hasher = hashlib.new(hash_algorithm)
    while number_of_derived_words < target_key_size:
        if block is not None:
            hasher.update(block)

        hasher.update(passwd.encode())
        hasher.update(salt)
        block = hasher.digest()
        hasher = hashlib.new(hash_algorithm)

        for i in range(1, iterations):
            hasher.update(block)
            block = hasher.digest()
            hasher = hashlib.new(hash_algorithm)

        derived_bytes += block[0: min(len(block), (target_key_size - number_of_derived_words) * 4)]

        number_of_derived_words += len(block) / 4

    return {
        "key": derived_bytes[0: key_size * 4],
        "iv": derived_bytes[key_size * 4:]
    }


def encrypt(passphrase, plaintext):
    print("passphrase = %s" % passphrase)
    print("passphrase = %s" % binascii.b2a_hex(passphrase.encode()))
    print("plaintext = %s" % plaintext)
    print("plaintext = %s" % binascii.b2a_hex(plaintext.encode()))

    salt = Random.new().read(8)
    print("salt = %s" % binascii.b2a_hex(salt))
    resp = evpKDF(passphrase, salt, key_size=12)
    key = resp.get("key")
    iv = key[len(key) - 16:]
    key = key[:len(key) - 16]
    print("iv = %s" % binascii.b2a_hex(iv))
    print("key = %s" % binascii.b2a_hex(key))

    aes = AES.new(key, MODE, iv)
    encoder = PKCS7Encoder()
    pad_text = encoder.encode(plaintext)
    print("pad text = %s" % pad_text)
    print("pad text = %s" % binascii.b2a_hex(pad_text.encode()))
    encrypted_text = aes.encrypt(pad_text.encode())

    print("encrypted text = %s" % binascii.b2a_hex(encrypted_text))

    concat = b"Salted__" + salt + encrypted_text
    print("concat=%s" % binascii.b2a_hex(concat))
    return binascii.b2a_base64(concat).rstrip()


def decrypt(passphrase, encrypted_text):
    encrypted_text_bytes = binascii.a2b_base64(encrypted_text)
    print("Original encrypted message = %s" % binascii.b2a_hex(encrypted_text_bytes))

    # Remove "Salt__"
    encrypted_text_bytes = encrypted_text_bytes[8:]

    # Get and remove salt
    salt = encrypted_text_bytes[:8]
    print("salt = %s" % binascii.b2a_hex(salt))
    encrypted_text_bytes = encrypted_text_bytes[8:]
    print("encrypted_text_bytes = %s" % binascii.b2a_hex(encrypted_text_bytes))

    resp = evpKDF(passphrase, salt, key_size=12)
    key = resp.get("key")
    iv = key[len(key) - 16:]
    key = key[:len(key) - 16]
    print("iv = %s" % binascii.b2a_hex(iv))
    print("key = %s" % binascii.b2a_hex(key))

    aes = AES.new(key, MODE, iv)
    decrypted_text = aes.decrypt(encrypted_text_bytes)
    encoder = PKCS7Encoder()
    unpad_text = encoder.decode(decrypted_text)
    print("unpad_text = %s" % binascii.b2a_hex(unpad_text))

    return unpad_text


if __name__ == '__main__':
    KEY = 'mysecretkey'
    PLAINTEXT = 'secret text'

    encrypted_text = encrypt(KEY, PLAINTEXT)
    print("encrypted_text (base64)= %s" % encrypted_text)

    print("\n\nDECRYPT")
    decrypted_text = decrypt(KEY, encrypted_text)
    print("decrypted text = %s" % decrypted_text)
