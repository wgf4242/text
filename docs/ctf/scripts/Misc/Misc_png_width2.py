import os
os.system('mkdir out 2>nul')

f = open("2.png",'rb').read()
for i in range(1800):
    fw = open(f'./out/{i}.png','wb')
    data = b''
    data += f[:16]
    w = i.to_bytes(4, 'big')
    data += w
    data += f[20:]
    fw.write(data)