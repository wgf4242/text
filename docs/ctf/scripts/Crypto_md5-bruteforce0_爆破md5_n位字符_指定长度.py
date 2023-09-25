import hashlib

import itertools
import string

target_hash = 'c4d038'

charset = string.digits + string.ascii_lowercase

# 1到6位爆破
for i in range(1, 7):
    for combination in itertools.product(charset, repeat=i):
        attampt = "".join(combination)
        md5_hash = hashlib.md5(attampt.encode()).hexdigest()[:16]
        if md5_hash.startswith(target_hash):
            print(md5_hash, attampt, hashlib.md5(attampt.encode()).hexdigest())
            exit(0)
    else:
        print("No match found")
# 之前解密信息里有 the key is 1****y
# 748007e861908c03 14mk3y
