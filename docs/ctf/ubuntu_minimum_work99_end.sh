sudo apt-get install -y rubygems 


sudo update-alternatives  --set python3 /usr/bin/python3.5

sudo add-apt-repository ppa:brightbox/ruby-ng
sudo apt-get update
sudo apt-get purge --auto-remove ruby
sudo apt-get install ruby2.6 ruby2.6-dev


gem sources --remove https://rubygems.org/
gem sources --add https://gems.ruby-china.com/
gem sources -l
sudo gem install one_gadget zsteg
# one_gadget需要ruby安装高版本

sudo apt-get install -y aircrack-ng  python3.8-dev libc6 libc6-dev libc6-dev-i386 qemu mktemp perl tar grep zstd file rpm2cpio cpio jq binutils
pip3 install ciphey uncompyle6 dirsearch egcd gmpy2 egcd sympy z3-solver

### segamath
# sudo apt-add-repository -y ppa:aims/sagemath
# sudo apt-get update
# sudo apt-get install sagemath-upstream-binary

sudo update-alternatives  --set python3 /usr/bin/python3.8

git clone https://github.com.cnpmjs.org/Ganapati/RsaCtfTool.git --depth=1  ~/Downloads/RsaCtfTool
