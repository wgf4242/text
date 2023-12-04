import binascii
import itertools

target_crc = 0xd2b184ff
length = 3

chars = [chr(x) for x in range(256)]

for i in itertools.product(chars, repeat=length):
    enc = ''.join(i).encode('latin')
    char_crc = binascii.crc32(enc)  # 获取遍历字符的CRC32值
    calc_crc = char_crc & 0xffffffff  # 将遍历的字符的CRC32值与0xffffffff进行与运算
    if calc_crc == target_crc:
        print(enc.hex())
        exit(0)
