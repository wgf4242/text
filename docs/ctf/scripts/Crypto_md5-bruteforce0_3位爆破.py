import hashlib
str1='abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
payload=''
for i in str1:
    for j in str1:
        for k in str1:
            s = hashlib.md5(('ctfshow'+i+j+k).encode()).hexdigest()
            #print(type(s))
            if s=='a6f57ae38a22448c2f07f3f95f49c84e':
                print(i+j+k)
         
