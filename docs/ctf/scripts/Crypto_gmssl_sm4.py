# 国密ssl 加密算法
# https://gitee.com/mirrors/gmssl-python
import json

from gmssl.sm4 import CryptSM4, SM4_ENCRYPT, SM4_DECRYPT
import base64


class SM4Utils:

    def __init__(self, ):
        pass

    # 加密方法
    def encryptData_ECB(self, plain_text):
        # 创建 SM4对象
        crypt_sm4 = CryptSM4()
        # 定义key值
        secret_key = b"JeF38U9wT9wlMfs2"
        # print("key: ", secret_key)

        # 设置key
        crypt_sm4.set_key(secret_key, SM4_ENCRYPT)

        # 调用加密方法加密(十六进制的bytes类型)
        encrypt_value = crypt_sm4.crypt_ecb(plain_text)
        # print("encrypt_value: ", encrypt_value)

        # 用base64.b64encode转码（编码后的bytes）
        cipher_text = base64.b64encode(encrypt_value)

        # print("加密后：", cipher_text)
        # print(cipher_text.decode('utf-8', 'ignore'))
        # 返回加密后的字符串
        return cipher_text.decode('utf-8', 'ignore')

    def decryptData_ECB(self, cipher_text):
        crypt_sm4 = CryptSM4()
        secret_key = b"JeF38U9wT9wlMfs2"
        print(secret_key)
        crypt_sm4.set_key(secret_key, SM4_DECRYPT)
        # 将转入参数base64.b64decode解码成十六进制的bytes类型
        byt_cipher_text = base64.b64decode(cipher_text)
        # 调用加密方法解密，解密后为bytes类型
        decrypt_value = crypt_sm4.crypt_ecb(byt_cipher_text)
        print(decrypt_value)
        print(decrypt_value.decode('utf-8', 'ignore'))
        print(json.dumps(decrypt_value.decode('utf-8', 'ignore')))

        return decrypt_value.decode('utf-8', 'ignore')


if __name__ == '__main__':
    SM4_Utils = SM4Utils()

    # plain_text = b'{"t":1625451188275,"userToken":"c49bdd6a558948ec86c957c8bd07c1c8"}'
    # plain_text = b"aaa"
    # SM4_Utils.encryptData_ECB(plain_text)

    # cipher_text = r"vk2cLOFpUU9fpOs5p9+Mjdl2Ik3s/XXS/BJE1Sgbt8jPFh1kmV2Gf0UUO4ak/Xq4NVARIeK73Q9w7G4MOnRdvxnS4XCWYl7huV2GNew6MEo="
    # SM4_Utils.decryptData_ECB(cipher_text)

    plain_text = b"aaa"
    enc = SM4_Utils.encryptData_ECB(plain_text)
    SM4_Utils.decryptData_ECB(enc)
