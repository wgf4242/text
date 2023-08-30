import hashlib

import itertools
import string

target_hash = '748007e861908c03'

charset = string.digits + string.ascii_lowercase

for combination in itertools.product(charset, repeat=4):
    attampt = "1" + "".join(combination) + 'y'
    md5_hash = hashlib.md5(attampt.encode()).hexdigest()[:16]
    if md5_hash == target_hash:
        print(md5_hash, attampt, hashlib.md5(attampt.encode()).hexdigest())
        break
else:
    print("No match found")
# 之前解密信息里有 the key is 1****y
# 748007e861908c03 14mk3y