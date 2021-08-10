from zlib import decompress, compress
data = open('c1.png', 'rb').read()[0xF4289:]
decompress(data)

compress(b'123')