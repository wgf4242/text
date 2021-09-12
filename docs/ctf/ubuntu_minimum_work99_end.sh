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

## ---- install segamath
# sudo apt-add-repository -y ppa:aims/sagemath
# sudo apt-get update
# sudo apt-get install sagemath-upstream-binary

sudo update-alternatives  --set python3 /usr/bin/python3.8

git clone https://github.com.cnpmjs.org/Ganapati/RsaCtfTool.git --depth=1  ~/Downloads/RsaCtfTool &
git clone https://github.com.cnpmjs.org/pwndbg/pwndbg --depth=1 ~/Downloads/pwndbg &
git clone https://gitee.com/wgf4242/LibcSearcher.git --depth=1 ~/Downloads/LibcSearcher &
git clone https://github.com.cnpmjs.org/niklasb/libc-database.git --depth=1 ~/Downloads/libc-database &
for job in `jobs -p`; do
    echo Wait on $job
    wait $job
done
rm -rf ~/Downloads/LibcSearcher/libc-database
mv  ~/Downloads/libc-database ~/Downloads/LibcSearcher/


## ---- install apache2, php
# sudo apt-get install -y apache2 php libapache2-mod-php php-dev
sudo apt install -y php 
sudo apt install -y mariadb-server-10.0
sudo apt install -y php-dev autoconf automake
systemctl disable apache2 

## ---- install xdebug
wget https://xdebug.org/files/xdebug-2.8.1.tgz -P ~/Downloads
cd ~/Downloads && tar -xvzf xdebug-2.8.1.tgz
cd xdebug-2.8.1
phpize
./configure && make
sudo cp modules/xdebug.so /usr/lib/php/20151012

# echo "zend_extension = /usr/lib/php/20151012/xdebug.so" | sudo tee -a /etc/php/7.0/apache2/conf.d/99-xdebug.ini
sudo tee -a /etc/php/7.0/apache2/conf.d/99-xdebug.ini <<-'EOF'
zend_extension = /usr/lib/php/20151012/xdebug.so
xdebug.remote_port = 9000
xdebug.idekey = PHPSTORM
xdebug.remote_autostart=1
xdebug.remote_host= localhost
xdebug.remote_enable=1
EOF

sudo systemctl restart apache2.service
