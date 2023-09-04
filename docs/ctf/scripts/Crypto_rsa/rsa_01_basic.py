# 导入cryptography库中的rsa模块
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric.padding import OAEP, MGF1
from cryptography.hazmat.primitives import hashes

# 生成一对公钥和私钥，长度为2048位
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()
print("私钥:", private_key)
print("公钥:", public_key)

# 定义一个明文字符串
plaintext = "Hello, world!"

# 使用公钥对明文进行加密，得到一个字节串类型的密文
ciphertext = public_key.encrypt(plaintext.encode(), OAEP(mgf=MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
print("密文:", ciphertext)

# 使用私钥对密文进行解密，得到一个字节串类型的明文
decrypted = private_key.decrypt(ciphertext, OAEP(mgf=MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
print("解密后的明文:", decrypted.decode())

