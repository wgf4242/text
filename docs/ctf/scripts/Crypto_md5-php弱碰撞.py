import hashlib

for i in range(0,10**41):
    i='0e'+str(i)
    md5=hashlib.md5(i.encode()).hexdigest()
    if md5[:2]=='0e' and md5[2:].isdigit():
        print('md5:{} '.format(i))
        break
