# https://github.com/Threekiii/Awesome-Redteam/blob/98e374fdae125bec00228fa364b72f2ffbff407c/tips/%E6%B5%81%E9%87%8F%E5%88%86%E6%9E%90-Webshell.md?plain=1#L289
# @Function: Brute Force of Behinder4 secret key
# 需要复制 response 的base64信息爆破, 不要用request的
"""keys.txt
pass
pass1024
rebeyond
123456
"""

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
    data = '''0g4nH1rJhBvxKa+TLIZ1U9Q4UOMAPDeXWzffS/oisaxW1sy3HcFK4foq2L5976hihTHnVQ4n4x1XadYf/0ahL7cLm/G0Tgfl3Bg25+WXmCw='''
    with open('keys.txt', 'r', encoding='utf-8') as f:
        keys = f.readlines()

    for key in keys:
        key = key.strip()
        c2_key = md5_truncate(key)
        print('[CURRENT KEY]\t{} {}'.format(key, c2_key))
        try:
            data_b64_decode = base64.b64decode(data.strip())
            data_aes_decode = aes_decode(data_b64_decode, c2_key)
            if data_aes_decode:
                print('[Ooooops, We found it!]')
                print(data_aes_decode)
                break
        except:
            pass
