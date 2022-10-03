"""
PKCS5 要填充7个字节,那么填入的值就是0×7;

PKCS7和PKCS5的区别是数据块的大小；
  PKCS5填充块的大小为8bytes(64位)
  PKCS7填充块的大小可以在1-255bytes之间。
因为AES并没有64位的块, 如果采用PKCS5, 那么实质上就是采用PKCS7
"""

# pip install pycrypto
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def encrypt():
    block_size = 16 # 8, 16, 32
    enc = b'08412823411101692325329511727110819824832456838286186275904827514650901136712580'
    key = b'HandDownManDown\x00'

    cryptor = AES.new(key, AES.MODE_ECB)
    enc = pad(enc, block_size)
    plain = cryptor.encrypt(enc)
    assert plain.hex().upper() == 'DD99F735AC7E1C1C1EFADABA729393843AD354AED3F73EDA83618A398CB358518BC577A333C4407368AF7063B9C833A40B0BCA6D8C1EED0AC8B71BB1CB178B5BC03578D042F02431DAB3F0532181C88EA8C19439722B048926B7EFC6D2362E29'


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


def decrypt3():
    from Crypto.Util.Padding import pad, unpad
    BLOCK_SIZE = 32  # Bytes

    key = 'abcdefghijklmnop'
    cipher = AES.new(key.encode('utf8'), AES.MODE_ECB)
    msg = cipher.encrypt(pad(b'hello', BLOCK_SIZE))
    print(msg.hex())
    decipher = AES.new(key.encode('utf8'), AES.MODE_ECB)
    msg_dec = decipher.decrypt(msg)
    print(unpad(msg_dec, BLOCK_SIZE))


if __name__ == '__main__':
    decrypt1()
    decrypt2()
    decrypt3()
