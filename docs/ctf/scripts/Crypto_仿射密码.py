#,只需要遍历一下字母, 字母表转为0-26
a = 123456
b = 321564 

#cipher = 'kgwsmucmuekkwemeeww'
cipher = [10, 6, 22, 18, 12, 20, 2, 12, 20, 4, 10, 10, 22, 4, 12, 4, 4, 22,22]
key = 'abcdefghijklmnopqrstuvwxyz'
for i in range(len(cipher)):
    for j in range(len(key)):
        #print(j)
        if (j*123456+321564)%26 == cipher[i]:
            print(key[j],end='')
            break