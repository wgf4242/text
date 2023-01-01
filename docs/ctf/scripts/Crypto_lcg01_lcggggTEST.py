from Crypto.Util.number import *
import libnum
import binascii

a =  978562056823367154661231724324891953762007467621
n =  749016427347710886642154346393313956385679230533
output1 =  659790491777475729494865848448903737196638977914
output2 =  486063966694351430606710544549903497571072525229
b=(output2-a*output1)%n
plaintext=b
print(plaintext)
# print(long_to_bytes(plaintext))
c =  output1
MMI = lambda A, n,s=1,t=0,N=0: (n < 2 and t%N or MMI(n, A%n, t, s-A//n*t, N or n),-1)[n<1] #逆元计算
ani=MMI(a,n)
seed=c
for i in range(1):
    seed = (ani*(seed-b))%n
print(long_to_bytes(seed))