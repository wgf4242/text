# pip install pycrypto
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def decrypt1():
    key = base64.b64decode('cGhyYWNrICBjdGYgMjAxNg==')
    enc = base64.b64decode('sSNnx1UKbYrA1+MOrdtDTA==')

    cryptor = AES.new(key, AES.MODE_ECB)
    plain = cryptor.decrypt(enc)
    print(plain)
    print(plain.decode('utf8'))


def decrypt2():
    key = b'mfsvxueshang'.ljust(16, b'\x00')
    enc = 'yjPW8RIz0og8HX3o6BcwTmveeyyEDiCurJNTwPJeY/PMyOhHXYVKPLln6isBRyL0'
    enc = base64.b64decode(enc)
    cryptor = AES.new(key, AES.MODE_ECB)
    plain = cryptor.decrypt(enc).rstrip(b'\0')
    print(plain)


if __name__ == '__main__':
    decrypt1()
    decrypt2()
