from Crypto.Util.number import *

# Crypto_base64_修错.py

print(long_to_bytes(0x65a6d78685a33733059584e6b4e575266613346704d5770754d563878614446696233303d))

# print(bytes.fromhex('5a6d78685a33733059584e6b4e575266613346704d5770754d563878614446696233303d'))

from Crypto.Hash import MD5


h = MD5.new()
h.update(b'savedInstanceState')
print(h.hexdigest())
