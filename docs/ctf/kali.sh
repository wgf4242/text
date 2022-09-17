sudo systemctl enable ssh.service
sudo service ssh start

echo "------ sysconfig: autologin -------"
sudo sed -i "s/^\[Seat:\*]/\[Seat:\*]\nautologin-user=kali/g" /etc/lightdm/lightdm.conf
tee -a ~/.dmrc <<-'EOF'
autologin-user=kali
autologin-session=session
EOF


sudo rm /etc/apt/sources.list
sudo tee -a /etc/apt/sources.list <<-'EOF'

deb http://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main contrib non-free
deb-src https://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main contrib non-free
# deb https://mirrors.aliyun.com/kali kali-rolling main non-free contrib
# deb-src https://mirrors.aliyun.com/kali kali-rolling main non-free contrib
# deb http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib
# deb-src http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib
EOF

sudo apt-get update

xset r rate 220 30
sudo dpkg --add-architecture i386
sudo apt-get update
sudo apt-get install -y checksec foremost gdb libgmp3-dev libmpc-dev python3-pip g++ libssl-dev zlib1g-dev gnuplot steghide outguess texinfo ncat  strace proxychains  docker docker-compose
sudo apt-get install -y python3-tornado acejump volatility tmux

# 7z2john
sudo apt-get install libcompress-raw-lzma-perl -y

gem sources --remove https://rubygems.org/
gem sources --add https://gems.ruby-china.com/
gem sources -l
sudo gem install one_gadget zsteg
echo "------config pip file -------"
mkdir ~/.pip;cat <<EOT >> ~/.pip/pip.conf
[global]
index-url=https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host=mirrors.aliyun.com
EOT
echo "------pip install file -------"
pip3 install gmpy2 pycrypto rsa pillow pwntools angr ropgadget wscan flask-unsign utf9
# pip install xortools

echo "------Config vim -------"
echo "set mouse=c">>~/.vimrc
echo "syntax on">>~/.vimrc
echo "------ Downloads -------"

echo "get pwndbg"
# rm ~/.gdbinit;echo "source ~/peda/peda.py" >> ~/.gdbinit 
git clone https://github.com.cnpmjs.org/longld/peda.git ~/peda --depth=1 &
git clone https://github.com.cnpmjs.org/pwndbg/pwndbg --depth=1 ~/Downloads/pwndbg &
git clone https://github.com.cnpmjs.org/slimm609/checksec.sh.git --depth=1 ~/Downloads/checksec.sh &
git clone https://github.com.cnpmjs.org/Ganapati/RsaCtfTool.git --depth=1  ~/Downloads/RsaCtfTool &

for job in `jobs -p`; do
    echo Wait on $job
    wait $job
done
sudo ln -sf ~/Downloads/checksec.sh/checksec /usr/bin/

echo "------ Install pwndbg -------"
~/Downloads/pwndbg/setup.sh
rm ~/.gdbinit;echo "source ~/Downloads/pwndbg/gdbinit.py" >> ~/.gdbinit

# 结束后的收尾工作
# ln -s /usr/local/lib/python3.8/dist-packages/bin/ROPgadget /usr/bin
# sudo gzip -d /usr/share/wordlists/rockyou.txt.gz


echo "------ Install docker -------"
sudo tee -a /etc/docker/daemon.json << EOF
{
  "registry-mirrors": ["https://docker.mirrors.ustc.edu.cn"]
}
EOF



echo "------ ********************* -------"
echo "------ 手动添加vmware共享文件夹 -------"
echo "------ ********************* -------"
echo ".host:/vmware /home/kali/vmware fuse.vmhgfs-fuse   allow_other   0   0" | sudo tee -a /etc/fstab

