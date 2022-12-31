from sm4 import SM4Key


# [python]SM4算法实现
# https://blog.csdn.net/weixin_43936250/article/details/124425082

def sm4_decrypt(str_bytes, key_bytes):
    key0 = SM4Key(key_bytes)
    return key0.decrypt(str_bytes)


def sm4_decrypt_ECB_by_gmssl(byt_cipher_text, secret_key):
    from gmssl.sm4 import CryptSM4, SM4_ENCRYPT, SM4_DECRYPT
    crypt_sm4 = CryptSM4()
    crypt_sm4.set_key(secret_key, SM4_DECRYPT)
    decrypt_value = crypt_sm4.crypt_ecb(byt_cipher_text)
    return decrypt_value


def sm4_encrypt_ECB_by_gmssl(plain_text, secret_key):
    from gmssl.sm4 import CryptSM4, SM4_ENCRYPT, SM4_DECRYPT
    crypt_sm4 = CryptSM4()
    crypt_sm4.set_key(secret_key, SM4_ENCRYPT)
    encrypt_value = crypt_sm4.crypt_ecb(plain_text)
    # return encrypt_value.


import unittest


class Test(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        """
        eg2:
        m = bytes.fromhex("26289786B91D24860DE5492672906E67")
        key = bytes.fromhex('0123456789ABCDEFFEDCBA9876543210')
        assert b'aAa_bBb_cCc_dddd' == sm4_decrypt(m, key)
        """

    def test_sm4_decrypt(self):
        m = bytes.fromhex("fa18a3514eff62c1da89bec2fd26803326f4fed752a658813346b827a3eff52d9f7f5a04510bff515f3a5d7e3f1ef92fe4ac19c0af8597bd3096e62e4213da9c5fa13f606760e112c9492dde2f59a472")
        key = b'xc08asb890ajds0a'
        r = sm4_decrypt(m, key)
        assert b'hackerpersonalcrackmepersonalflag{c6545808-81ba-48c6-b082-df559da10751}' in r
        # ECB
        # cyberchef #recipe=SM4_Decrypt(%7B'option':'Latin1','string':'xc08asb890ajds0a'%7D,%7B'option':'Hex','string':''%7D,'ECB','Hex','Raw')&input=ZmExOGEzNTE0ZWZmNjJjMWRhODliZWMyZmQyNjgwMzMyNmY0ZmVkNzUyYTY1ODgxMzM0NmI4MjdhM2VmZjUyZDlmN2Y1YTA0NTEwYmZmNTE1ZjNhNWQ3ZTNmMWVmOTJmZTRhYzE5YzBhZjg1OTdiZDMwOTZlNjJlNDIxM2RhOWM1ZmExM2Y2MDY3NjBlMTEyYzk0OTJkZGUyZjU5YTQ3Mg

    def test_sm4_decrypt_ECB_by_gmssl(self):
        m = bytes.fromhex("fa18a3514eff62c1da89bec2fd26803326f4fed752a658813346b827a3eff52d9f7f5a04510bff515f3a5d7e3f1ef92fe4ac19c0af8597bd3096e62e4213da9c5fa13f606760e112c9492dde2f59a472")
        key = b'xc08asb890ajds0a'
        r = sm4_decrypt_ECB_by_gmssl(m, key)
        assert b'hackerpersonalcrackmepersonalflag{c6545808-81ba-48c6-b082-df559da10751}' in r

    def test_sm4_encrypt_ECB_by_gmssl(self):
        plain = b'hackerpersonalcrackmepersonalflag{c6545808-81ba-48c6-b082-df559da10751}'
        key = b'xc08asb890ajds0a'
        r = sm4_encrypt_ECB_by_gmssl(plain, key)
        assert r.hex() == 'fa18a3514eff62c1da89bec2fd26803326f4fed752a658813346b827a3eff52d9f7f5a04510bff515f3a5d7e3f1ef92fe4ac19c0af8597bd3096e62e4213da9c5fa13f606760e112c9492dde2f59a472'
