import zipfile
import string
import binascii

def CrackCrc(crc):
    for i in dic:
        for j in dic:
            for k in dic:
                for h in dic:
                    s = i + j + k + h
                    if crc == (binascii.crc32(s.encode())):
                        f.write(s)
                        return

def CrackZip():
        for i in range(0,68):
            file = 'out'+str(i)+'.zip'
            crc = zipfile.ZipFile(file,'r').getinfo('data.txt').CRC
            CrackCrc(crc)

dic = string.ascii_letters + string.digits + '+/='

f = open('out.txt','w')
CrackZip()
print("CRC32碰撞完成")
f.close
