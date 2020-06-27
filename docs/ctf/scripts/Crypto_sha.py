import hashlib

a="a test string".encode('utf8')

print(hashlib.md5(a).hexdigest())
print(hashlib.sha1(a).hexdigest())
print(hashlib.sha224(a).hexdigest())
print(hashlib.sha256(a).hexdigest())
print(hashlib.sha384(a).hexdigest())
print(hashlib.sha512(a).hexdigest())

from Crypto.Hash import SHA256
h = SHA256.new()
h.update(b'150753')
print(h.hexdigest())

# shell
# echo -n 1 | openssl dgst -sha256
# echo -n 1 | sha256sum
