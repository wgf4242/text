# Method 1
# import hashlib
# def md5(fname):
#     hash_md5 = hashlib.md5()
#     with open(fname, "rb") as f:
#         for chunk in iter(lambda: f.read(4096), b""):
#             hash_md5.update(chunk)
#     return hash_md5.hexdigest()

# Method 2
# import hashlib

# with open("your_filename.png", "rb") as f:
#     file_hash = hashlib.md5()
#     while chunk := f.read(8192):
#         file_hash.update(chunk)

# print(file_hash.digest())
# print(file_hash.hexdigest())  # to get a printable str instead of bytes

import hashlib
hashlib.md5(open("123.txt", 'rb').read()).hexdigest()


# this
print(MD5.new(b'1').hexdigest())

from Crypto.Hash import MD5
h = MD5.new()
h.update(b'ffifdyop')
print(h.hexdigest())

import hashlib
m = hashlib.md5()
m.update(b"ffifdyop")
print(m.hexdigest())


