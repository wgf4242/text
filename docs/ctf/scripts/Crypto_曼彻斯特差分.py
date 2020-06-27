#coding=utf-8
flag = bin(int('flag{0123456789abcdef}'.encode('hex'),16))[2:]
s='01' # or '10'
for i in range(len(flag)):
    if flag[i]=='1':
        s+=s[-2:][::-1]
    else:
        s+=s[-2:]
print hex(int(s,2))[2:-1]
#6565659565569a99665959555956a6a55959596aa696a69aa69959aaa6569aa9655a9aa69a95656965656669
r=""
tmp = 0
for i in xrange(len(s)/2):
    c = s[i*2]
    if c == s[i*2 - 1]:
        r += '1'
    else:
        r += '0'
print hex(int(r,2))[2:-1].decode('hex')
#flag{0123456789abcdef}
