from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad, pad
# key = pad(key, DES.block_size)

key = b'-8B key-'
cipher = DES.new(key, DES.MODE_ECB)


def DES_enc(plaintext):
    msg = cipher.encrypt(plaintext)
    print(msg)
    return msg


def DES_dec(msg):
    plain = cipher.decrypt(msg)
    print(plain)


plaintext = b'sona si latine loqueris '
msg = DES_enc(plaintext)
print(cipher.decrypt(msg))
