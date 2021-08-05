# 先断网安装
sudo apt install openssh-server
sudo apt update
sudo apt install -y gcc python3-dev curl gdb open-vm-tools open-vm-tools-dkms git lib32z1 lib32stdc++6
curl -x http://192.168.247.1:1081 "https://bootstrap.pypa.io/pip/3.5/get-pip.py" -o "get-pip35.py"

mkdir ~/.pip;cat <<EOT >> ~/.pip/pip.conf
[global]
index-url=https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host=mirrors.aliyun.com
EOT

python3 get-pip35.py --user
pip3 install pwntools

# 其他可装 zsh 