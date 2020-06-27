s="bacoN is one of aMerICa'S sWEethEartS. it's A dARlinG, SuCCulEnt fOoD tHAt PaIRs FlawLE"
m1=""
m2=""
for i in s:
    if i.isupper():
        m1+='a'
        m2+='b'
    elif i.islower():
        m1+='b'
        m2+='a'

print(m1)
print(m2)

L=[]
for i in range(len(m2)//5):
    L.append(m2[:5])
    m2=m2[5:]

dir1 = {'aaaaa':'A','aaaab':'B','aaaba':'C','aaabb':'D','aabaa':'E','aabab':'F','aabba':'G','aabbb':'H','abaaa':'I',
        'abaab':'J','ababa':'K','ababb':'L','abbaa':'M','abbab':'N','abbba':'O','abbbb':'P','baaaa':'Q','baaab':'R',
        'baaba':'S','baabb':'T','babaa':'U','babab':'V','babba':'W','babbb':'X','bbaaa':'Y','bbaab':'Z'}

dir2 = {'AAAAA':'a','AABBA':'g','ABBAA':'n','BAABA':'t','AAAAB':'b','AABBB':'h','ABBAB':'o','BAABB':'u/v',
        'AAABA':'c','ABAAA':'i/j','ABBBA':'p','BABAA':'w','AAABB':'d','ABAAB':'k','ABBBB':'q','BABAB':'x',
        'AABAA':'e','ABABA':'l','BAAAA':'r','BABBA':'y','AABAB':'f','ABABB':'m','BAAAB':'s','BABBB':'z'}
flag1=""
flag2=""

for i in L:
    flag1+=str(dir1.get(i.lower()))
    flag2+=str(dir2.get(i.upper()))

print("flag1:%s"%flag1)
print("flag2:%s"%flag2)
