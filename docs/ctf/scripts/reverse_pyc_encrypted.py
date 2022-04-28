# https://gift1a.github.io/2022/04/23/DASCTF-FATE-Reverse/#0x02-%E5%A5%87%E6%80%AA%E7%9A%84%E4%BA%A4%E6%98%93
#!/usr/bin/env python3
import tinyaes
import zlib

CRYPT_BLOCK_SIZE = 16

# 从crypt_key.pyc获取key，也可自行反编译获取
key = bytes('0000000000000tea', 'utf-8')

inf = open('cup.pyc.encrypted', 'rb')  # 打开加密文件
outf = open('cup.pyc', 'wb')  # 输出文件

# 按加密块大小进行读取
iv = inf.read(CRYPT_BLOCK_SIZE)

cipher = tinyaes.AES(key, iv)

# 解密
plaintext = zlib.decompress(cipher.CTR_xcrypt_buffer(inf.read()))

# 补pyc头(最后自己补也行)
head = open('../struct.pyc', 'rb').read(16)
outf.write(head)

# 写入解密数据
outf.write(plaintext)

inf.close()
outf.close()

