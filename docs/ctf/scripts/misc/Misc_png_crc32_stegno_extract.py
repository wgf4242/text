data = open('alien.png','rb').read()
flag = ''
pos = data.index(b'IDAT')
data = data[pos+5:]
while 1:
    try:
        pos = data.index(b'IDAT')
        flag += str(hex(data[pos-5])[2:].zfill(2))
        data = data[pos+5:]
    except:
        f1 = open('out.rar','w')
        f1.write(flag)
        exit(1)