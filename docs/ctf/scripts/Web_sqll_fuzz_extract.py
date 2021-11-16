a = """/**/,sElect,uNion,.,oR,aNd,	,",',^,+,Hex,0x,0b1111101000,?,sHow,dEsc,orDer By,--,~~,`,CONcat,aLter,Columns,*,UpdateXml,ExtractValue,load_file"""
a = a.split(',')
print(a)
b = """//
'
"
substr
mid
=
like
into
"""
b = b.split('\n')
print(b)
lowera = [x.lower() for x in a]
for x in b:
    lx = x.lower()
    if lx not in lowera:
        if len(lx) < 2:
            a.append(lx.upper())
        else:
            c1 = lx[0]
            c2 = lx[1]
            c3 = lx[2:]
        a.append(''.join([c1, c2.upper(), ''.join(c3)]))
print(a)
print(','.join(a))