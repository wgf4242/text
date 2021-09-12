import base64
a = open('flag.txt', 'rb').read().strip(b'\n')
b = b''
while b := base64.b64decode(a):
    if b'{' in b:
        print(b)
    a = b
