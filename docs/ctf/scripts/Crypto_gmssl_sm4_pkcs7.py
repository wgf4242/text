# Source Generated with Decompyle++
# File: ezpython.pyc (Python 3.10)

from gmssl import sm4

key = 'BeginCTFBeginCTF'
enc = b'JmjJEAJGMT6F9bmC+Vyxy8Z1lpfaJzdEX6BGG/qgqUjUpQaYSON1CnZyX9YXTEClSRYm7PFZtGxmJw6LPuw1ww=='

import base64


def pad_pkcs7(data):
    '''PKCS#7填充'''
    padding_len = 16 - len(data) % 16
    padding = bytes([
                        padding_len] * padding_len)
    return data + padding


def unpad_pkcs7(padded_data):
    '''PKCS#7去填充'''
    padding_len = padded_data[-1]
    return padded_data[:-padding_len]


class SM4:

    def __init__(self):
        self.gmsm4 = sm4.CryptSM4()

    def encryptSM4(self, encrypt_key, value):
        gmsm4 = self.gmsm4
        gmsm4.set_key(encrypt_key.encode(), sm4.SM4_ENCRYPT)
        padded_value = pad_pkcs7(value.encode())
        encrypt_value = gmsm4.crypt_ecb(padded_value)
        return base64.b64encode(encrypt_value)

    def decryptSM4(self, decrypt_key, encrypted_data):
        gmsm4 = sm4.CryptSM4()
        gmsm4.set_key(decrypt_key.encode(), sm4.SM4_DECRYPT)
        decrypted_data = base64.b64decode(encrypted_data)
        decrypted_value = gmsm4.crypt_ecb(decrypted_data)
        unpadded_value = unpad_pkcs7(decrypted_value)
        return unpadded_value.decode()


if __name__ == '__main__':
    # print('请输入你的flag:')
    # flag = input()
    sm4_instance = SM4()
    # flag_1 = sm4_instance.decryptSM4(key, enc.decode())
    # flag_1 = sm4_instance.encryptSM4(key, '12341234')
    # print(flag_1)
    # print(sm4_instance.decryptSM4(key, 'uph9aUWYulzN8YmSWiZO39w3QxNVmCqpAfmQwNI8t68='))
    print(sm4_instance.decryptSM4(key, 'JmjJEAJGMT6F9bmC+Vyxy8Z1lpfaJzdEX6BGG/qgqUjUpQaYSON1CnZyX9YXTEClSRYm7PFZtGxmJw6LPuw1ww=='))
