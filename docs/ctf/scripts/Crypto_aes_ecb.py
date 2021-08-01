# pip install pycrypto
import base64
from Crypto.Cipher import AES
 
key=base64.b64decode('cGhyYWNrICBjdGYgMjAxNg==')
enc=base64.b64decode('sSNnx1UKbYrA1+MOrdtDTA==')

cryptor=AES.new(key,AES.MODE_ECB)
plain=cryptor.decrypt(enc)
print(plain)
print(plain.decode('utf8'))
