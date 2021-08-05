# 1. 先断网再安装
# 2. 安装好后设置网络 ,
# 3. 把CDROM连接上,看好是CD1还是CD2, 以CD2为例 /dev/sr1
# sudo dhclient
# sudo mount /dev/sr1 /media/cdrom
# 4. 安装 ssh, 修改源再继续
sudo apt install openssh-server
sudo service ssh start
# ssh上安装下面
sudo rm /etc/apt/sources.list
sudo tee -a /etc/apt/sources.list <<-'EOF'
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security main restricted universe multiverse
EOF

sudo apt update
sudo apt install -y gcc python3-dev curl gdb open-vm-tools open-vm-tools-dkms git zsh

mkdir ~/.pip;cat <<EOT >> ~/.pip/pip.conf
[global]
index-url=https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host=pypi.tuna.tsinghua.edu.cn
EOT

#  --------快照一下
sudo apt install -y python3-pip

sudo apt-get install software-properties-common -y

sudo add-apt-repository -y ppa:deadsnakes/ppa

sudo apt update
sudo apt install -y python3.8 python3.8-distutils
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1
sudo apt install -y python3-pip
## lib32z1 lib32stdc++6

curl "https://bootstrap.pypa.io/pip/get-pip.py" -O
python3 get-pip.py
pip3 install pwntools==4

# 其他可装 zsh 
