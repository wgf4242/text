from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

text = b"0d2fd588668054da021349541e5cb64f55979d02e41c75e0ce0233f6d10e31251b40cb8e197404f9e261fba573e09191"
key = b'1234123412ABCDEF'
iv = b'ABCDEF1234123412'
mode = AES.MODE_CBC

cryptor = AES.new(key, mode, iv)
plain_text = cryptor.decrypt(a2b_hex(text))
print(bytes.decode(plain_text))


"""
    pkcs7 https://www.cnblogs.com/Testking/p/11991153.html
    明文使用PKCS7填充,如果块长度是16，数据长度9，那么还差7个字节，就在后面补充7个0x07
    数据：  FF FF FF FF FF FF FF FF FF
    填充后：FF FF FF FF FF FF FF FF FF 07 07 07 07 07 07 07
    
    from Crypto.Util.Padding import pad
    data = pad(b'123', 16, style='pkcs7')  # default pkcs7 ,不用写
"""
