from Crypto.Cipher import DES3
from Crypto import Random

key = 'Sixteen byte key'
iv = Random.new().read(DES3.block_size)  # DES3.block_size is 8

cipher = DES3.new(key, DES3.MODE_OFB, iv)
plaintext = 'This is a text that we will encrypt'
# Convert plaintext to bytes
msg = iv + cipher.encrypt(plaintext.encode('utf-8'))

print(msg)  # Output: Encrypted text in bytes


cipher = DES3.new(key, DES3.MODE_OFB, iv)
decrypted_text = cipher.decrypt(msg[DES3.block_size:]).decode('utf-8')

print(decrypted_text)  # Output: 'This is a text that we will encrypt'
