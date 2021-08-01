sudo apt-get update
#sudo apt-get upgrade

xset r rate 220 30
sudo dpkg --add-architecture i386
sudo apt-get update
sudo apt-get install -y checksec foremost gdb libgmp3-dev libmpc-dev python3-pip g++ libssl-dev zlib1g-dev gnuplot steghide outguess texinfo ncat  strace
sudo apt-get install -y python3-tornado acejump volatility 
gem sources --remove https://rubygems.org/
gem sources --add https://gems.ruby-china.com/
gem sources -l
sudo gem install one_gadget zsteg
echo "------config pip file -------"
mkdir ~/.pip;cat <<EOT >> ~/.pip/pip.conf
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
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
