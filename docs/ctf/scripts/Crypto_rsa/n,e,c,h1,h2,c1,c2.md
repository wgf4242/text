## 风二西_RSA29
又见数论h1h2c1c2

题目

```python
import gmpy2
import libnum
import uuid

flag="flag{"+str(uuid.uuid4())+"}"
print(flag)
m=libnum.s2n(flag)
p=libnum.generate_prime(512)
q=libnum.generate_prime(512)
e=65537
n=p*q

h1=pow(2022*p+2021*q,1919,n)
h2=pow(2021*p+2022*q,9191,n)

c=pow(m,e,n)
print("h1=",h1)
print("h2=",h2)
print("n=",n)
print("c=",c)
h1= 30855822627962989585229048864635672320544672090785297155723423466786046363050770166911337642023073726938940720811335150158356617935867424913657952916327330494297125827029212326952561052030408154856279444698976262609160644653834177066135162450457878611978648445980131216562928824964574836061694756466154667205
h2= 40100423593623305059775303455521238466361560139512541341649592368069344035986841719639287569549223369845132085965748305686682111656643181380183441717688410643280141958261131108758470255679260104010792458818255865919591927360182698571973058572267041626051012344432873060584028954870019976713790755601324558548
n= 64102959876468100680156640535847855388761634133282097987245513821195616433464232166471238446539383399142190819132167640251487788433828354971655930602252481995598958979413328369264306739790569021167918377152867054737871100808301104788028284764159363852402951908183073134132550874656189587590198702783318894869
c= 45131183832310284041286970164837452402860781494367814170537748979786683176908409834474718536824887130743650179867181711815561375866637642188028690304179190358058486755191379316599103162356440279017384835373685350107932236214472686050587719705355548868691431799158695967203810074232266157701183923093912519832

```

 推导
$$
\begin{multline}
\shoveleft
\begin{aligned}
& h_1 = (2022*p + 2021*q)^{1919}\%n \\ 
& h_2 = (2021*p + 2022*q)^{9191}\%n \\ 
& 若 a \equiv b \ (mod \ p), 则对于正整数c，都有(a**c) \equiv (b ** c)(mod \ p) \\
& h_1^{9191} = (2022*p + 2021*q)^{1919 * 9191}\%n \\ 
& h_2^{1919} = (2021*p + 2022*q)^{9191 * 1919}\%n \\ 
& \\
& h_1^{9191} = (2022*p + 2021*q)^{1919 * 9191}+kn \\ 
& h_2^{1919} = (2021*p + 2022*q)^{9191 * 1919}+kn \\ 
& 同时模上 q \\
& h_1^{9191} \% q = (2022*p + 2021*q)^{1919 * 9191}\%q \\ 
& h_1^{9191} = (2022*p)^{1919 * 9191} + k_1q \\
& h_2^{1919} = (2021*p)^{9191 * 1919} + k_2q \\ 
& \\

& h_1同时乘以2021^{1919*9191} \\
& h_1^{9191}*2021^{1919*9191} = 2021^{1919*9191}*(2022*p)^{1919 * 9191} + k_3q \\
& h_2两侧 2022^{1919*9191} \\
& h_2^{1919}*2022^{1919*9191} = 2022^{1919*9191}* (2021*p)^{9191 * 1919} + k_4q \\ 

& \\
& 两式相减 \\ 
& h_2^{1919}*2022^{1919*9191} - h_1^{9191}*2021^{1919*9191} = k_5q \\
& q = gcd(h_2^{1919}*2022^{1919*9191} - h_1^{9191}*2021^{1919*9191}, n) \\
& 同时 \% n减少计算量 \\
& (h_2^{1919}*2022^{1919*9191} - h_1^{9191}*2021^{1919*9191}) \%n = k_5q \% n \\ 
& (h_2^{1919}*2022^{1919*9191} - h_1^{9191}*2021^{1919*9191}) \%n = k_5q + kn \\ 
& (h_2^{1919}*2022^{1919*9191} - h_1^{9191}*2021^{1919*9191}) \%n = k_5q + kpq \\ 
& (h_2^{1919}*2022^{1919*9191}\%n - h_1^{9191}*2021^{1919*9191}\%n) \%n = k_6q \\ 

\end{aligned}
\end{multline}
$$


```python
import gmpy2
from Crypto.Util.number import long_to_bytes

h1= 30855822627962989585229048864635672320544672090785297155723423466786046363050770166911337642023073726938940720811335150158356617935867424913657952916327330494297125827029212326952561052030408154856279444698976262609160644653834177066135162450457878611978648445980131216562928824964574836061694756466154667205
h2= 40100423593623305059775303455521238466361560139512541341649592368069344035986841719639287569549223369845132085965748305686682111656643181380183441717688410643280141958261131108758470255679260104010792458818255865919591927360182698571973058572267041626051012344432873060584028954870019976713790755601324558548
n= 64102959876468100680156640535847855388761634133282097987245513821195616433464232166471238446539383399142190819132167640251487788433828354971655930602252481995598958979413328369264306739790569021167918377152867054737871100808301104788028284764159363852402951908183073134132550874656189587590198702783318894869
c= 45131183832310284041286970164837452402860781494367814170537748979786683176908409834474718536824887130743650179867181711815561375866637642188028690304179190358058486755191379316599103162356440279017384835373685350107932236214472686050587719705355548868691431799158695967203810074232266157701183923093912519832
e=65537

h3 = pow(h2, 1919, n) * pow(2022, 1919 * 9191, n) - pow(h1, 9191, n) * pow(2021, 9191 * 1919, n)
p = gmpy2.gcd(n, h3)
q = n // p
phi = (p - 1) * (q - 1)

assert p * q == n
assert gmpy2.gcd(e, phi) == 1

d = gmpy2.invert(e, phi)
m = pow(c, d, n)
print(long_to_bytes(m))

```
