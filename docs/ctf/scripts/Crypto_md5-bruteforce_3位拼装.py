#coding=UTF-8


import hashlib   
for i in range(65,91):
    for j in range(65,91):
        for k in range(65,91):
            m=hashlib.md5()
            m.update(('TASC'+chr(i)+'O3RJMV'+chr(j)+'WDJKX'+chr(k)+'ZM').encode())#改
            des=m.hexdigest()
            if 'e9032' in des and 'da' in des and '911513' in des:#改
                print(des)