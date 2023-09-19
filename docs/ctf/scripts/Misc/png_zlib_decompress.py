import zlib, binascii

IDAT = bytes.fromhex('789c33340403030006eb0188')
result = zlib.decompress(IDAT)
print(result)
