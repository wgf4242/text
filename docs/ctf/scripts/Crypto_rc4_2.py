def crypt(data, key):
    x = 0
    box = list(range(256))
    for i in range(256):
        x = (x + box[i] + ord(key[i % len(key)])) % 256
        box[i], box[x] = box[x], box[i] ^ 0x37
    x = y = 0
    out = []
    for char in data:
        x = (x + 1) % 256
        y = (y + box[x]) % 256
        box[x], box[y] = box[y], box[x]
        out.append(chr(ord(char) ^ box[(box[x] + box[y]) % 256]))
    return ''.join(out)


key = 'flechao10'
stdata = '\x83\x1b\xf2K\xaf\x01\x05#9]\xa2\x9b\x92\xf1\x9d\xdd\xdd\x99\xbcw\xcb\x19r\xe5d/\xd6>\x0f\x12\x05l\x900\xb7\x02\xc6\xd0\xe8#<#'

decoded_data = crypt(data=stdata, key=key)
print(decoded_data)
# flag{c8d4d879-7a03-405f-8b12-9085a944adad}
