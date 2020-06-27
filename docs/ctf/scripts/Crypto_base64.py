# base64 自定义变化码表
import base64

cipher = '5rFf7E2K6rqN7Hpiyush7E6S5fJg6rsi5NBf6NGT5rs='
my_base64chars = "vwxrstuopq34567ABCDEFGHIJyz012PQRSTKLMNOZabcdUVWXYefghijklmn89+/"
STD_BASE64CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
# base64chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'

cipher = cipher.translate(str.maketrans(my_base64chars, STD_BASE64CHARS))
data = base64.b64decode(cipher)
print(data)
