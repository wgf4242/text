from Crypto.Cipher import AES
from os import urandom
import random
import string

# key = urandom(16)
# iv = urandom(16)
# print(key)
# print(iv)


# str_list = [random.choice(string.digits + string.ascii_letters) for i in range(32)]
# plaintext = ''.join(str_list)
# print(plaintext)
key = b'\xc2d\x1d+\xbe\xc9\x8a\xa6;\xd1t41\xbe\x15\xe7'
iv = b'\x83Z\x8dn\xc3s\xcb\xfe\xe11cP\x00\xb1\xfcg'
plaintext = 'XQlj3iR3uNpFceKhF4IlpWty3x8EsOMu'


def encrypt(iv, plaintext):
    aes_encrypt = AES.new(key, AES.MODE_CBC, IV=iv)
    return aes_encrypt.encrypt(plaintext.encode())


def decrypt(iv, cipher):
    aes_decrypt = AES.new(key, AES.MODE_CBC, IV=iv)
    return aes_decrypt.decrypt(cipher)


def main():
    cipher = encrypt(iv, plaintext)
    print(cipher)

    bin_cipher = bytearray(cipher)

    # bin_cipher[15] = bin_cipher[15] ^ ord('u') ^ ord('G')
    # bin_cipher[14] = bin_cipher[14] ^ ord('M') ^ ord('N')
    for i in range(16):
        bin_cipher[i] = bin_cipher[i] ^ ord(plaintext[16 + i]) ^ ord('6')

    de_cipher = decrypt(iv, bytes(bin_cipher))
    print(de_cipher)
    de_cipher = bytearray(de_cipher[:16])
    bin_iv = bytearray(iv)
    for i in range(16):
        bin_iv[i] = bin_iv[i] ^ de_cipher[i] ^ ord('9')
    de_cipher = decrypt(bytes(bin_iv), bytes(bin_cipher))
    print(de_cipher.decode('utf-8', errors='ignore'))


if __name__ == '__main__':
    
    main()

