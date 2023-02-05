from Crypto.Cipher import ARC4
import unittest
from Crypto.Hash import SHA
from Crypto.Random import get_random_bytes
import base64


def rc4_crypt(msg, key):
    cipher = ARC4.new(key)
    return cipher.decrypt(msg)
    # cipher.encrypt(txt) 一样的 rc4 加密解密用一个函数


class Test(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()

    def test_rc4_crypt(self):
        key = "flag{123321321123badbeef012}"
        key1 = bytes(key, encoding="utf-8")
        rc4enc = b'\x1d\xc5\x80_\xe7\x0cX\x06\xb1\x9e\x1d=x?\x85v\xa6\x97\x89\x0f\xe2\x8c\x84U\xc6[\xc4V\x02\xbb\xf2\xbaq\xa3\x16\xc1x\xa6!\xa7\x04\x96)'
        flag = b'flag{RC_f0ur_And_Base_s1xty_f0ur_Encrypt_!}'
        self.assertEqual(rc4_crypt(rc4enc, key1), flag)
