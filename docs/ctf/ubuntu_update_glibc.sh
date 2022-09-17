# list:     strings /lib/x86_64-linux-gnu/libc.so.6 | grep GLIBC_

wget https://mirrors.tuna.tsinghua.edu.cn/gnu/libc/glibc-2.36.tar.gz -P ~/Downloads
cd ~/Downloads
sudo tar zxvf glibc-2.36.tar.gz
cd glibc-2.36/
mkdir build
cd build/
sudo apt install -y bison
# compiler too old ,更新gcc

../configure --prefix=/usr/glibc-2.36
make
sudo make install
# sudo cp /usr/glibc-2.36/lib/libc.so.6 /lib/x86_64-linux-gnu/libc-2.36.so

# Docs
# https://blog.csdn.net/moliyiran/article/details/104134625
# ---- Test
# export LD_PRELOAD=/home/kali/Downloads/glibc-2.36/build/libc.so.6
# ./runit
# ln -s /opt/glibc-2.14/lib/libc-2.14.so /lib64/libc.so.6

# download
# https://pkgs.org/download/libc.so.6()(64bit)
# check:  /usr/glibc-2.36/bin/ldd --version