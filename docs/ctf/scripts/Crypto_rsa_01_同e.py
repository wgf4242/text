import gmpy2
import binascii
# 两组数中e相同，n，c不同，求出n1与n2的最大公因数即为p，之后就可以得到q和d，从而求解m。
e = 65537
n1 = 23686563925537577753047229040754282953352221724154495390687358877775380147605152455537988563490716943872517593212858326146811511103311865753018329109314623702207073882884251372553225986112006827111351501044972239272200616871716325265416115038890805114829315111950319183189591283821793237999044427887934536835813526748759612963103377803089900662509399569819785571492828112437312659229879806168758843603248823629821851053775458651933952183988482163950039248487270453888288427540305542824179951734412044985364866532124803746008139763081886781361488304666575456680411806505094963425401175510416864929601220556158569443747
c1 = 1627484142237897613944607828268981193911417408064824540711945192035649088104133038147400224070588410335190662682231189997580084680424209495303078061205122848904648319219646588720994019249279863462981015329483724747823991513714172478886306703290044871781158393304147301058706003793357846922086994952763485999282741595204008663847963539422096343391464527068599046946279309037212859931303335507455146001390326550668531665493245293839009832468668390820282664984066399051403227990068032226382222173478078505888238749583237980643698405005689247922901342204142833875409505180847943212126302482358445768662608278731750064815

n2 = 22257605320525584078180889073523223973924192984353847137164605186956629675938929585386392327672065524338176402496414014083816446508860530887742583338880317478862512306633061601510404960095143941320847160562050524072860211772522478494742213643890027443992183362678970426046765630946644339093149139143388752794932806956589884503569175226850419271095336798456238899009883100793515744579945854481430194879360765346236418019384644095257242811629393164402498261066077339304875212250897918420427814000142751282805980632089867108525335488018940091698609890995252413007073725850396076272027183422297684667565712022199054289711
c2 = 2742600695441836559469553702831098375948641915409106976157840377978123912007398753623461112659796209918866985480471911393362797753624479537646802510420415039461832118018849030580675249817576926858363541683135777239322002741820145944286109172066259843766755795255913189902403644721138554935991439893850589677849639263080528599197595705927535430942463184891689410078059090474682694886420022230657661157993875931600932763824618773420077273617106297660195179922018875399174346863404710420166497017196424586116535915712965147141775026549870636328195690774259990189286665844641289108474834973710730426105047318959307995062

p = gmpy2.gcd(n1,n2)
q = n1 // p
phi = (p-1)*(q-1)

d = gmpy2.invert(e,phi)
m = gmpy2.powmod(c1,d,n1)

print(binascii.unhexlify(hex(m)[2:]))
