n=0x1fb18fb44f4449f45ea938306c47b91f64b6c176bd24dbb35aa876f73859c90f0e1677d07430a1188176bc0b901ca7b01f6a99a7df3aec3dd41c3d80f0d17292e43940295b2aa0e8e5823ffcf9f5f448a289f2d3cb27366f907ee62d1aaeba490e892dc69dacbafa941ab7be809e1f882054e26add5892b1fcf4e9f1c443d93bf
e=0xe42a12145eaa816e2846200608080305c99468042450925789504307cbc54a20ed7071b68b067b703a1679d861795542f8cbd2d1cb4d3847d0940cac018cdb0fa729571afbe10c1b8be2dd8acd99ee48b77d53c435b9c2fed59e12e02ad8cfc2bcc46ad85534c266dcc1f3a1a03d87118eaf3f5b3eeeb3be84ad023a4bf34939
c=0xd19d63015bdcb0b61824237b5c67cb2ef09af0c6cd30e193ff9683357b1e45ab4df607b8c1e0b96cafc49a84d7e655c3ce0f71b1d217eec9ca6cdfa57dd3dc92533b79431aa8a7d6ca67ac9cdd65b178a5a96ab7ce7bf88440f4a9b9d10151b0c942a42fdab9ea2c2f0c3706e9777c91dcc9bbdee4b0fb7f5d3001719c1dd3d3


import gmpy2
import libnum
def transform(x,y):       #使用辗转相处将分数 x/y 转为连分数的形式
    res=[]
    while y:
        res.append(x//y)
        x,y=y,x%y
    return res
    
def continued_fraction(sub_res):
    numerator,denominator=1,0
    for i in sub_res[::-1]:      #从sublist的后面往前循环
        denominator,numerator=numerator,i*numerator+denominator
    return denominator,numerator   #得到渐进分数的分母和分子，并返回

    
#求解每个渐进分数
def sub_fraction(x,y):
    res=transform(x,y)
    res=list(map(continued_fraction,(res[0:i] for i in range(1,len(res)))))  #将连分数的结果逐一截取以求渐进分数
    return res

def get_pq(a,b,c):      #由p+q和pq的值通过维达定理来求解p和q
    par=gmpy2.isqrt(b*b-4*a*c)   #由上述可得，开根号一定是整数，因为有解
    x1,x2=(-b+par)//(2*a),(-b-par)//(2*a)
    return x1,x2

def wienerAttack(e,n):
    for (d,k) in sub_fraction(e,n):  #用一个for循环来注意试探e/n的连续函数的渐进分数，直到找到一个满足条件的渐进分数
        if k==0:                     #可能会出现连分数的第一个为0的情况，排除
            continue
        if (e*d-1)%k!=0:             #ed=1 (mod φ(n)) 因此如果找到了d的话，(ed-1)会整除φ(n),也就是存在k使得(e*d-1)//k=φ(n)
            continue
        
        phi=(e*d-1)//k               #这个结果就是 φ(n)
        px,qy=get_pq(1,n-phi+1,n)
        if px*qy==n:
            p,q=abs(int(px)),abs(int(qy))     #可能会得到两个负数，负负得正未尝不会出现
            d=gmpy2.invert(e,(p-1)*(q-1))     #求ed=1 (mod  φ(n))的结果，也就是e关于 φ(n)的乘法逆元d
            return d
    print("该方法不适用")
    
    
d=wienerAttack(e,n)
print("d=",d)
m=pow(c ,d ,n)
res = int(m)
print(libnum.n2s(res))
# d= 731297