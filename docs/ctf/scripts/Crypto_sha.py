import hashlib
from Crypto.Hash import SHA256

# a = "a test string".encode('utf8')
a = "123".encode('utf8')

print(b"sha1: ".rjust(12) + hashlib.sha1(a).digest())  # b"\x12\xac\x56"
print("md5 : ".rjust(12) + hashlib.md5(a).hexdigest())
print("sha1: ".rjust(12) + hashlib.sha1(a).hexdigest())
print("sha224 is: ".rjust(12) + hashlib.sha224(a).hexdigest())
print("sha256 is: ".rjust(12) + SHA256.new(a).hexdigest())
print("sha256 is: ".rjust(12) + hashlib.sha256(a).hexdigest())
print("sha384 is: ".rjust(12) + hashlib.sha384(a).hexdigest())
print("sha512 is: ".rjust(12) + hashlib.sha512(a).hexdigest())

# a = SHA256.new()
# a.update(b'123')
# print(a.hexdigest())

# echo -n 1 | openssl dgst -sha256
# echo -n 1 | sha256sum
