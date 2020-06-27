# RSA
# n, c 求 明文 , 已经 PQ积 官文 求明文

import gmpy2
import binascii
def decrypt(dp,dq,p,q,c):
	InvQ = gmpy2.invert(q,p)
	mp = pow(c,dp,p)
	mq = pow(c,dq,q)
	m=(((mp-mq)*InvQ)%p)*q+mq
	temp_flag=binascii.unhexlify(hex(m)[2:]).decode()
	flag='flag'+temp_flag[6:]
	print(flag)
p = 8637633767257008567099653486541091171320491509433615447539162437911244175885667806398411790524083553445158113502227745206205327690939504032994699902053229 
q = 12640674973996472769176047937170883420927050821480010581593137135372473880595613737337630629752577346147039284030082593490776630572584959954205336880228469 
dp = 6500795702216834621109042351193261530650043841056252930930949663358625016881832840728066026150264693076109354874099841380454881716097778307268116910582929 
dq = 783472263673553449019532580386470672380574033551303889137911760438881683674556098098256795673512201963002175438762767516968043599582527539160811120550041 
c = 24722305403887382073567316467649080662631552905960229399079107995602154418176056335800638887527614164073530437657085079676157350205351945222989351316076486573599576041978339872265925062764318536089007310270278526159678937431903862892400747915525118983959970607934142974736675784325993445942031372107342103852

decrypt(dp,dq,p,q,c)