import zlib
import binascii

IDAT = """78 9C"""
IDAT = bytes.fromhex(IDAT)  # 默认会将十六进制做为字符串解码，此时就会出现错误，就需要转换成字节码
# HEX_str = IDAT.hex()#字节码转换成十六进制
# print(HEX_str)#检查一下是否有误
result = binascii.hexlify(zlib.decompress(IDAT))
print(result)
