from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
import base64

# 读取PEM证书文件并提取公钥
with open('public_key.pem', 'rb') as f:
    pem_data = f.read()
    public_key = RSA.import_key(pem_data)

# 要加密的数据
data = "Hello, RSA encryption!"

# 加密数据
cipher = PKCS1_OAEP.new(public_key)
encrypted_data = cipher.encrypt(data.encode())

# 将加密后的数据转换为Base64格式
encrypted_data_base64 = base64.b64encode(encrypted_data).decode()

print("Encrypted data (Base64):", encrypted_data_base64)