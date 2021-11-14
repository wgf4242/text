p= 122148491423639510060358520247326001415378756960123061340205031810235511253496233656913937819798161138467669802058794431258364815048474953088507274866256378381409951959750689384174071189227238884101846565741054406768547752624840426474750191838000550894022573930877154168207130498171735566553517132962856855111
q= 142755578574113482683875150345372577363277111983736520709390192691018628850982550669601255375276434229753811206425659062428721779518168263620205357414671725791655926862817648459031593998074454782619982558995296893592414687691579260619395713067522690127560706829880215532804483197706245921702087884445862908311
N= 17437378565136796938110429615460109306513763994515441361700826128854509816577500859330683620324942811798278054720514628441058958796253590667597639564320226081313246692273260392020172668686109508486701867559622051759183126919749044186432732690010275229298964648509739981889494014237283495021762548037876030067888443161621760780099178071080783305102758292721482026470985598146884711243792995042285939445306378914554641176698591510703687482228868400552567474489250501034857093624184577568397256397519711404394386053806918127762571356839381312261171823757803194242506737946861441555551672977659019959562416882973604727521
c= 3136716033729239841651527855193478838856206237778382623476323002673660140993283468296727521269046606643005570111263565370046029024734759921698482194871684883853668185647585044859555880105903361901008649
e= 2

import gmpy2
# radin 加密 , e=2

# with open('flag.enc', 'rb') as f:
#     c = f.read().hex()
#     c = int(c, 16)
#     print(c)

yp = gmpy2.invert(p, q)
yq = gmpy2.invert(q, p)

# 计算mp和mq
mp = pow(c, (p + 1) // 4, p)
mq = pow(c, (q + 1) // 4, q)

# 计算a,b,c,d
a = (yp * p * mq + yq * q * mp) % N
b = N - int(a)
c = (yp * p * mq - yq * q * mp) % N
d = N - int(c)

for i in (a, b, c, d):
    s = '%x' % i
    if len(s) % 2 != 0:
        s = '0' + s
    print (s)
    print(bytearray.fromhex(s).decode('Latin1'))
    # print(codecs.decode(s, "hex"))
    # print (bytearray.fromhex(s).decode())