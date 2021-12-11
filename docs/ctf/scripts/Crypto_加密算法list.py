def rot13_1():
    rot13 = str.maketrans(
        'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
        'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')
    'Hello World!'.translate(rot13)
    # 'Uryyb Jbeyq!'


def rot13_2():
    import codecs
    codecs.encode('foobar', 'rot_13')


def hmac_encrypt():
    import hmac
    import hashlib

    str_encrypt = "hello！"
    key = "abc"
    # 第一个参数是密钥key，第二个参数是待加密的字符串，第三个参数是hash函数

    mac = hmac.new(key.encode(encoding="utf-8"), str_encrypt.encode("utf8"), hashlib.md5)

    value = mac.hexdigest()  # 加密后字符串的十六进制格式

    # 十六进制
    print("十六进制的字符串", value)


def des_encrypt():
    from Crypto.Cipher import DES
    import binascii

    # DES加密数据的长度须为8的的倍数，不够可以用其它字符填充
    text = 'Welcome to DES'
    if len(text) % 8 != 0:
        text = text + "+" * (8 - len(text) % 8)
    # 密钥：必须为8字节
    key = b'12345678'
    # 使用 key 初始化 DES 对象，使用 DES.MODE_ECB 模式
    des = DES.new(key, DES.MODE_ECB)
    # 加密
    result = des.encrypt(text.encode())

    print('加密后的数据：', result)
    # 转为十六进制    binascii 的 b2a_hex 或者 hexlify 方法
    print('转为十六进制：', binascii.b2a_hex(result))
    # 解密
    print('解密后的数据：', des.decrypt(result))


def aes_encrypt_ecb():
    import base64
    from Crypto.Cipher import AES

    # ECB加密模式

    import base64
    from Crypto.Cipher import AES

    # 使用补0方法

    # # 需要补位，补足为16的倍数
    def add_to_16(s):
        while len(s) % 16 != 0:
            s += '\0'
        return str.encode(s)  # 返回bytes

    # 密钥长度必须为16、24或32位，分别对应AES-128、AES-192和AES-256
    key = 'abc4567890abc458'
    # 待加密文本
    text = 'hello'
    # 初始化加密器
    aes = AES.new(add_to_16(key), AES.MODE_ECB)
    # 加密
    encrypted_text = str(base64.encodebytes(aes.encrypt(add_to_16(text))), encoding='utf8').replace('\n', '')
    # 解密
    decrypted_text = str(
        aes.decrypt(base64.decodebytes(bytes(encrypted_text, encoding='utf8'))).rstrip(b'\0').decode("utf8"))

    print('加密值：', encrypted_text)
    print('解密值：', decrypted_text)


def aes_encrypt_cbc_pkcs7():
    from cryptography.hazmat.primitives import padding
    from cryptography.hazmat.primitives.ciphers import algorithms
    from Crypto.Cipher import AES
    from binascii import b2a_hex, a2b_hex
    import json

    '''
    AES/CBC/PKCS7Padding 加密解密
    环境需求:
    pip3 install pycryptodome==3.9.0

    '''

    class PrpCrypt(object):

        def __init__(self, key='0000000000000000'):
            # self.key = key.encode('utf-8')
            self.key = b'1234123412ABCDEF'
            self.mode = AES.MODE_CBC
            self.iv = b'ABCDEF1234123412'
            # block_size 128位

        # 加密函数，如果text不足16位就用空格补足为16位，
        # 如果大于16但是不是16的倍数，那就补足为16的倍数。
        def encrypt(self, text):
            cryptor = AES.new(self.key, self.mode, self.iv)
            text = text.encode('utf-8')

            # 这里密钥key 长度必须为16（AES-128）,24（AES-192）,或者32 （AES-256）Bytes 长度
            # 目前AES-128 足够目前使用

            text = self.pkcs7_padding(text)

            self.ciphertext = cryptor.encrypt(text)

            # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
            # 所以这里统一把加密后的字符串转化为16进制字符串
            return b2a_hex(self.ciphertext).decode().upper()

        @staticmethod
        def pkcs7_padding(data):
            if not isinstance(data, bytes):
                data = data.encode()

            padder = padding.PKCS7(algorithms.AES.block_size).padder()

            padded_data = padder.update(data) + padder.finalize()

            return padded_data

        @staticmethod
        def pkcs7_unpadding(padded_data):
            unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
            data = unpadder.update(padded_data)

            try:
                uppadded_data = data + unpadder.finalize()
            except ValueError:
                raise Exception('无效的加密信息!')
            else:
                return uppadded_data

        # 解密后，去掉补足的空格用strip() 去掉
        def decrypt(self, text):
            #  偏移量'iv'
            cryptor = AES.new(self.key, self.mode, self.iv)
            plain_text = cryptor.decrypt(a2b_hex(text))
            # return plain_text.rstrip('\0')
            return bytes.decode(plain_text).rstrip("\x01"). \
                rstrip("\x02").rstrip("\x03").rstrip("\x04").rstrip("\x05"). \
                rstrip("\x06").rstrip("\x07").rstrip("\x08").rstrip("\x09"). \
                rstrip("\x0a").rstrip("\x0b").rstrip("\x0c").rstrip("\x0d"). \
                rstrip("\x0e").rstrip("\x0f").rstrip("\x10")

        def dict_json(self, d):
            '''python字典转json字符串, 去掉一些空格'''
            j = json.dumps(d).replace('": ', '":').replace(', "', ',"').replace(", {", ",{")
            return j

    # 加解密
    if __name__ == '__main__':
        import json
        pc = PrpCrypt()  # 初始化密钥
        a = "0d2fd588668054da021349541e5cb64f55979d02e41c75e0ce0233f6d10e31251b40cb8e197404f9e261fba573e09191"
        b = pc.decrypt(a)
        print(b)


def aes_encrypt_cbc1():
    # CBC加密模式
    import base64
    from Crypto.Cipher import AES
    from urllib import parse
    AES_SECRET_KEY = 'helloBrook2abcde'  # 此处16|24|32个字符
    IV = 'helloBrook2abcde'
    # padding算法
    BS = len(AES_SECRET_KEY)
    # 填充方案
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
    # 解密时删除填充的值
    unpad = lambda s: s[0:-ord(s[-1:])]

    def cryptoEn(string, key, iv):
        # param string: 原始数据
        # param key: 密钥
        # param iv: 向
        mode = AES.MODE_CBC
        cipher = AES.new(key.encode("utf8"), mode, iv.encode("utf8"))
        encrypted = cipher.encrypt(bytes(pad(string), encoding="utf8"))
        return base64.b64encode(encrypted).decode("utf-8")

    # CBC模式的解密代码
    def cryptoDe(destring, key, iv):
        # param destring: 需要解密的数据
        # param key: 密钥
        # param iv: 向量
        mode = AES.MODE_CBC
        decode = base64.b64decode(destring)
        cipher = AES.new(key.encode("utf8"), mode, iv.encode("utf8"))
        decrypted = cipher.decrypt(decode)
        return unpad(decrypted).decode("utf-8")

    secret_str = cryptoEn('hello', AES_SECRET_KEY, IV)
    print(secret_str)
    clear_str = cryptoDe(secret_str.encode("utf8"), AES_SECRET_KEY, IV)
    print(clear_str)


def aes_encrypt_cbc2():
    import base64
    from Crypto.Cipher import AES
    from urllib import parse

    AES_SECRET_KEY = 'helloBrook2abcde'  # 此处16|24|32个字符
    IV = 'helloBrook2abcde'

    # padding算法
    BS = len(AES_SECRET_KEY)
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
    unpad = lambda s: s[0:-ord(s[-1:])]

    class AES_ENCRYPT(object):
        def __init__(self):
            self.key = AES_SECRET_KEY
            self.mode = AES.MODE_CBC

        # 加密函数
        def encrypt(self, text):
            cryptor = AES.new(self.key.encode("utf8"), self.mode, IV.encode("utf8"))
            self.ciphertext = cryptor.encrypt(bytes(pad(text), encoding="utf8"))
            # AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题，使用base64编码
            return base64.b64encode(self.ciphertext).decode("utf-8")

        # 解密函数
        def decrypt(self, text):
            decode = base64.b64decode(text)
            cryptor = AES.new(self.key.encode("utf8"), self.mode, IV.encode("utf8"))
            plain_text = cryptor.decrypt(decode)
            return unpad(plain_text).decode("utf-8")

    if __name__ == '__main__':
        aes_encrypt = AES_ENCRYPT()
        text = "Python中中"
        # 如果字符串包含中文，先对文本转ascii码，将支持中文加密
        is_unicode = any(ord(c) > 255 for c in text)
        text = base64.b64encode(text.encode('utf-8')).decode('ascii') if is_unicode else text
        e = aes_encrypt.encrypt(text)
        d = aes_encrypt.decrypt(e)
        d = base64.b64decode(text.encode()).decode('utf8') if is_unicode else d
        print(text)
        print(e)
        print(d)


def rc4(data, key):
    # https://code.activestate.com/recipes/576736-rc4-arc4-arcfour-algorithm/
    x = 0
    box = list(range(256))
    for i in range(256):
        x = (x + box[i] + ord(key[i % len(key)])) % 256
        box[i], box[x] = box[x], box[i]
    x = 0
    y = 0
    out = []
    for char in data:
        x = (x + 1) % 256
        y = (y + box[x]) % 256
        box[x], box[y] = box[y], box[x]
        out.append(chr(ord(char) ^ box[(box[x] + box[y]) % 256]))

    return ''.join(out)

    if __name__ == '__main__':
        key = '12345678abcdefghijklmnopqrspxyz'
        data = b'\xc2\xbc\xc3\x85\x12}\xc2\x85#\xc2\x84q{9(\x02\xc3\x93Q\xc3\xb3,\xc2\x89+\xc2\xa6,\xc2\xaf\t'.decode()
        print(rc4(data, key))


if __name__ == '__main__':
    # hmac_encrypt()
    # des_encrypt()
    # aes_encrypt_ecb()
    # aes_encrypt_cbc1()
    aes_encrypt_cbc2()
    # rc4()
