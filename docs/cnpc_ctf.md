18245322906  7477a70041 

# Proxy Settings

nc 114.116.54.89 10001	
nc 114.116.54.89 10001 -x 127.0.0.1:1086

10.22.11.21 8080

## install pip
    
    $ sudo -i
    export http_proxy=http://10.22.11.21:8080
	export https_proxy=https://10.22.11.21:8080
    # easy_install pip

## apt-get     
    apt-get -o Acquire::http::proxy="http://10.22.11.21:8080/" update

## git

git config --global https.proxy http://10.22.11.21:8080

git config --global https.proxy https://10.22.11.21:8080

git config --global http.proxy 'socks5://127.0.0.1:1086'
git config --global https.proxy 'socks5://127.0.0.1:1086'


git config --global --unset http.proxy

git config --global --unset https.proxy


pip install --proxy="user:password@server:port" packagename
pip install --proxy="user:password@server:port" packagename
pip install django --proxy=10.22.11.21:8080
pip --proxy http://PROXYDOM:PROXYPORT install package

pip install --proxy='socks5://127.0.0.1:1080' packagename


10.22.11.21：8080	

# Kali安装
checksec

pwngdb


sudo pip uninstall pycrypto
and reinstalling pycrypto:
sudo pip install pycrypto
cmake
  Inconsistency detected by ld.so: rtld.c: 1273: dl_main: Assertion `GL(dl_rtld_map).l_libname' failed!
# RSA

https://www.cnblogs.com/jiftle/p/7903762.html

       1. 随意选择两个大的质数p和q，p不等于q，计算N=pq。
        2. 根据欧拉函数，不大于N且与N互质的整数個数為(p-1)(q-1)。
        3. 选择一个整数e与(p-1)(q-1)互质，并且e小于(p-1)(q-1)。
        4. 用以下这个公式计算d：d× e ≡ 1 (mod (p-1)(q-1))。
        5. 将p和q的记录销毁。
 
        以上内容中，(N,e)是公钥，(N,d)是私钥。

        下面讲解RSA算法的应用。
 
        RSA的公钥和私钥是由KeyPairGenerator生成的，获取KeyPairGenerator的实例后还需要设置其密钥位数。设置密钥位数越高，加密过程越安全，一般使用1024位。如下代码：
 
