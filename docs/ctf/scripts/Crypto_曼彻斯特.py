flag = bin(int('flag{0123456789abcdef}'.encode('hex'),16))[2:]
s='00'
for i in range(len(flag)):
    if flag[i]=='1':
        s+='10'
    else:
        s+='01'
print hex(int(s,2))[2:-1]
#296969a56956696a6a9a5a555a565a595a5a5a655a665a695a6a5a955a9669566959695a6965696669696aa6
r=""
for i in range(len(s)/2):
    if s[i*2:i*2+2] == '10':
        r += '1'
    else:
        r += '0'
print hex(int(r,2))[2:-1].decode('hex')
#flag{0123456789abcdef}
