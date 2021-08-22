# sha256碰撞,得出xxxx的值
import hashlib
import itertools
import string

code = ''
sha256enc = 'f84b299c25a5b5c4bc7977cbf1f82e44f04a72300fb639bd4b464e1b9641bc4f'
String = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz'
strlist = itertools.product(String, repeat=4)


String = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz'

def proof_of_work():
    STR = ''.join([String[random.randint(0,len(String)-1)] for _ in range(16) ])
    HASH = hashlib.sha256(STR.encode()).hexdigest()
    return STR[:4],STR[4:],HASH

# for i in strlist:
#     code = i[0] + i[1] + i[2] + i[3]
#     encinfo = hashlib.sha256(code.encode()).hexdigest()
#     if encinfo == sha256enc:
#         print(code)
#         break