from Cryptodome.PublicKey import RSA
import base64
from Cryptodome.Cipher import PKCS1_v1_5

cipher= PKCS1_v1_5.new(RSA.import_key(base64.b64decode(public_key)))
encrypted_data = cipher.encrypt(data.encode())

# 将加密后的数据转换为Base64格式
encrypted_data_base64 = base64.b64encode(encrypted_data).decode()
return encrypted_data_base64