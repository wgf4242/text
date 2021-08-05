sudo apt-get install -y rubygems

gem sources --remove https://rubygems.org/
gem sources --add https://gems.ruby-china.com/
gem sources -l
sudo gem install one_gadget zsteg
# one_gadget需要ruby安装高版本