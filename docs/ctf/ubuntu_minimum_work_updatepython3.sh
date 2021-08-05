curl -x http://192.168.247.1:1081 "https://bootstrap.pypa.io/pip/get-pip.py" -o "get-pip381.py"
curl "https://bootstrap.pypa.io/pip/get-pip.py" -o "get-pip38.py"


# 切换/升级为python3.8.1


sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.8

curl -x http://192.168.247.1:1081 "https://bootstrap.pypa.io/pip/get-pip.py" -o "get-pip38.py"

sudo apt install python3.8-distutils
python3 get-pip38.py

sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.8 2