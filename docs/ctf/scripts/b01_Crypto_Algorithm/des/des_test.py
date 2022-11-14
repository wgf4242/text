import unittest


class Test(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()

    def test_enc1(self):
        from des import Encryption
        plaintext = b'12345678'
        key = b'12345678'
        res = Encryption(plaintext, key)
        self.assertEqual(res, bytes.fromhex('96D0028878D58C89'))

    def test_decrypt2(self):
        from des import Decryption
        enc = bytes.fromhex('96D0028878D58C89')
        key = b'12345678'
        res = Decryption(enc, key)
        self.assertEqual(res, b'12345678')
