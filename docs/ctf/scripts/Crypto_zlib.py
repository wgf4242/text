from zlib import decompress
data = open('c1.png', 'rb').read()[0xF4289:]
decompress(data)