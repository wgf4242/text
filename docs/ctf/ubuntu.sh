sudo rm /etc/apt/sources.list
sudo tee -a /etc/apt/sources.list <<-'EOF'
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security main restricted universe multiverse

# 预发布软件源，不建议启用
# deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-proposed main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-proposed main restricted universe multiverse
EOF

sudo dpkg --add-architecture i386

sudo apt-get update
sudo apt-get install -y open-vm-tools
sudo apt install -y open-vm-tools-desktop fuse zlib1g:i386 libstdc++6:i386 libc6:i386 git build-essential openssh-server gcc g++ libssl-dev libncurses5-dev libncurses-dev libffi-dev zsh python3 curl libgmp3-dev libmpc-dev zstd
sudo apt install -y gdb vim zsh tmux
sudo apt install -y open-vm-tools-desktop fuse
# apps
sudo apt install -y imagemagick


mkdir ~/.pip;cat <<EOT >> ~/.pip/pip.conf
[global]
index-url=https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host=mirrors.aliyun.com
EOT

sudo apt-get install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.8

sudo apt install -y python3-pip
pip3 install --upgrade pip

pip3 install setuptools pwntools==4

sudo service ssh start


wget https://ghproxy.com/https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh
sed -i "s/-https:\/\/github.com/-https:\/\/github.com.cnpmjs.org/g" install.sh

. ~/.bashrc
bash install.sh

chsh -s `which zsh`

mkdir ~/vmware
sudo vmhgfs-fuse .host:/vmware /home/kali/vmware -o subtype=vmhgfs-fuse,allow_other
# sudo vmhgfs-fuse .host:/ /mnt/hgfs -o subtype=vmhgfs-fuse,allow_other -o nonempty
