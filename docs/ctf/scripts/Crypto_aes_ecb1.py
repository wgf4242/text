from Crypto.Cipher import AES
import base64

key = b'happy_1024_2233\x00'
aes = AES.new(key,AES.MODE_ECB)

passwd = 'e9ca6f21583a1533d3ff4fd47ddc463c6a1c7d2cf084d3640408abca7deabb96a58f50471171b60e02b1a8dbd32db156'
passwd = base64.b16decode(passwd.upper())

result = aes.decrypt(passwd).strip(b'\x00')
print(result)