from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

text = b"0d2fd588668054da021349541e5cb64f55979d02e41c75e0ce0233f6d10e31251b40cb8e197404f9e261fba573e09191"
key = b'1234123412ABCDEF'
iv = b'ABCDEF1234123412'
mode = AES.MODE_CBC

cryptor = AES.new(key, mode, iv)
plain_text = cryptor.decrypt(a2b_hex(text))
print(bytes.decode(plain_text))
