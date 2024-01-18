from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP

# 生成RSA密钥对
key = RSA.generate(2048)

# 获取公钥和私钥
public_key = key.publickey()
private_key = key.export_key()

# 要加密的数据
data = "Hello, RSA encryption!"

# 使用公钥进行加密
cipher = PKCS1_OAEP.new(public_key)
encrypted_data = cipher.encrypt(data.encode())

# 使用私钥进行解密
cipher = PKCS1_OAEP.new(key)
decrypted_data = cipher.decrypt(encrypted_data).decode()

print("Original data:", data)
print("Decrypted data:", decrypted_data)