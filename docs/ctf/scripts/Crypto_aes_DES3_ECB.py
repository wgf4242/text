from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

key = DES3.adjust_key_parity(get_random_bytes(24))  # DES3 requires 24-byte keys.

cipher = DES3.new(key, DES3.MODE_ECB)

plaintext = 'This is a text that we will encrypt.'
padded_plaintext = pad(plaintext.encode('utf-8'), DES3.block_size)  # DES3.block_size is 8.

ciphertext = cipher.encrypt(padded_plaintext)

print("Ciphertext:", ciphertext)  # Output: Encrypted text in bytes.

cipher = DES3.new(key, DES3.MODE_ECB)

decrypted_data = cipher.decrypt(ciphertext)
unpadded_plaintext = unpad(decrypted_data, DES3.block_size)

print("Decrypted text:", unpadded_plaintext.decode('utf-8'))  # Output: 'This is a text that we will encrypt.'