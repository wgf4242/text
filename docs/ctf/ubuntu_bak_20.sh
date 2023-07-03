# Ubuntu备用 pwn 环境安装
# https://mirrors.ustc.edu.cn/repogen/
# 如要用于其他版本，把 focal 换成其他版本代号即可: 23.04: lunar; 22.04：jammy；20.04：focal；18.04：bionic；16.04：xenial；14.04：trusty。
base=focal

sudo tee /etc/apt/sources.list <<-EOF
deb http://mirrors.ustc.edu.cn/ubuntu/ $base main restricted universe multiverse
deb-src http://mirrors.ustc.edu.cn/ubuntu/ $base main restricted universe multiverse

deb http://mirrors.ustc.edu.cn/ubuntu/ $base-security main restricted universe multiverse
deb-src http://mirrors.ustc.edu.cn/ubuntu/ $base-security main restricted universe multiverse

deb http://mirrors.ustc.edu.cn/ubuntu/ $base-updates main restricted universe multiverse
deb-src http://mirrors.ustc.edu.cn/ubuntu/ $base-updates main restricted universe multiverse

# deb http://mirrors.ustc.edu.cn/ubuntu/ $base-proposed main restricted universe multiverse
# deb-src http://mirrors.ustc.edu.cn/ubuntu/ $base-proposed main restricted universe multiverse

deb http://mirrors.ustc.edu.cn/ubuntu/ $base-backports main restricted universe multiverse
deb-src http://mirrors.ustc.edu.cn/ubuntu/ $base-backports main restricted universe multiverse
EOF

sudo apt update
sudo apt install -y patchelf python3-pip gdb git vim-tiny tmux
sudo rm -rf /usr/lib/python3/dist-packages/OpenSSL/

mkdir ~/Downloads
git clone https://ghproxy.com/https://github.com/pwndbg/pwndbg --depth=1 ~/Downloads/pwndbg
rm ~/.gdbinit
echo "source ~/Downloads/pwndbg/gdbinit.py" >> ~/.gdbinit

pip3 config set global.index-url https://pypi.mirrors.ustc.edu.cn/simple/
pip3 config set global.break-system-packages "true" # 允许全局安装
pip3 install -r ~/Downloads/pwndbg/requirements.txt 

tee -a ~/.pwn.conf <<-'EOF'
[context]
terminal = ["tmux", "splitw", "-h"]
[update]
interval=never
EOF

tee -a ~/.tmux.conf <<-'EOF'
setw -g xterm-keys on
set -s escape-time 0
set -s focus-events on
set -g mouse on
EOF
