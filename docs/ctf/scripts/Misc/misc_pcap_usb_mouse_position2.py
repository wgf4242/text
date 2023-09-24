# WMCTF2023 Truncate
import struct
import matplotlib.pyplot as plt
f=open('a.txt').readlines()
ff = ''
for i in f:
    ff += i.replace(' ','')[7:]
ff = bytes.fromhex(ff)

key_x = []
key_y = []

while 1:
    if len(ff) < 24:
        break
    data = ff[:24]
    ff = ff[24:]
    type = int.from_bytes(data[16:18], byteorder='big')
    code = int.from_bytes(data[18:20], byteorder='big')
    value = int.from_bytes(data[20:22], byteorder='big')
    if(type == 1):
        minlen = min(len(key_x), len(key_y))
        key_x = key_x[:minlen]
        key_y = key_y[:minlen]
        fig, ax = plt.subplots()
        ax.plot(key_x, key_y)
        ax.set_aspect('equal')
        plt.show()
        key_x = []
        key_y = []
    elif(type == 3 and code == 0 ):
        key_x.append(value)
    elif(type == 3 and code == 1 ):
        key_y.append(value * -1)