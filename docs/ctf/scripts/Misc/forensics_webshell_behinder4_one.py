import base64
import hashlib
from Crypto.Cipher import AES


def aes_decode(data, key):
    try:
        aes = AES.new(str.encode(key), AES.MODE_ECB)
        decrypted_text = aes.decrypt(data)
        decrypted_text = decrypted_text[:-(decrypted_text[-1])]
    except Exception as e:
        print(e)
    else:
        return decrypted_text.decode()


def base64_decode(data):
    res = base64.b64decode(data.strip()).decode()
    print(res)
    return res


def md5_truncate(key):
    return hashlib.md5(key.encode()).hexdigest()[:16]


if __name__ == '__main__':
    data = '''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'''
    key = "123456".strip()
    c2_key = md5_truncate(key)
    print('[CURRENT KEY]\t{} {}'.format(key, c2_key))
    try:
        data_b64_decode = base64.b64decode(data.strip())
        data_aes_decode = aes_decode(data_b64_decode, c2_key)
        if data_aes_decode:
            print('[Ooooops, We found it!]')
            print(data_aes_decode)
    except:
        pass
