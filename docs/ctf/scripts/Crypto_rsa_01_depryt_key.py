import gmpy2
import rsa
p = 275127860351348928173285174381581152299
q = 319576316814478949870590164193048041239
n = 87924348264132406875276140514499937145050893665602592992418171647042491658461
e = 65537
d = int(gmpy2.invert(e , (p-1) * (q-1)))
privatekey = rsa.PrivateKey(n , e , d , p , q) #根据已知参数，计算私钥
with open("flag.enc" , "rb") as f:
	print(rsa.decrypt(f.read(), privatekey).decode()) #使用私钥对密文进行解密，并打印