from Cryptodome.PublicKey import RSA

# 加载私钥文件
with open('private_key.pem', 'r') as f:
    private_key_data = f.read()

# 解析私钥
private_key = RSA.import_key(private_key_data)

# 获取公钥
public_key = private_key.publickey().export_key().decode()

# 打印公钥
print(public_key)