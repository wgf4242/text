# 爆破图片crc

import binascii

for i in range(16**4):
    i=hex(i)[2:].zfill(4)
    for j in range(16**4):
        j=hex(j)[2:].zfill(4)
        s= '%08x' % (binascii.crc32('IHDR'+'0000{i}0000{j}0802000000'.format(i=i,j=j).decode('hex')) & 0xffffffff)
        if s=='53d1578a':
            print 'x:',i,'y:',j,'crc:',s
    print 'x:',i
