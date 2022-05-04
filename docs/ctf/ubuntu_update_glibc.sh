wget https://mirrors.tuna.tsinghua.edu.cn/gnu/libc/glibc-2.34.tar.gz
sudo tar zxvf glibc-2.34.tar.gz -C /usr/local
cd /usr/local/glibc-2.34/
sudo mkdir build
cd build/
sudo apt install -y bison
../configure --prefix=/usr/glibc-2.34
make
make install


# https://blog.csdn.net/moliyiran/article/details/104134625