# wget -O install.sh https://notdocker.xp.cn/install.sh && sudo bash install.sh
echo ##----------------install  php5-------------
wget https://www.php.net/distributions/php-5.6.10.tar.bz2 -P ~/Downloads
sudo apt-get install apache2-dev libxml2-dev
cd ~/Downloads
tar jxvf php-5.6.10.tar.bz2
cd php-5.6.10
./configure --with-apxs2=/usr/bin/apxs --with-mysql --prefix=/usr/local/php5.6 --with-iconv-dir=/usr/local/lib
# ./configure --with-apxs2=/usr/bin/apxs --with-mysql --prefix=/usr/local/php5.6 --with-iconv-dir=/usr/local/lib --with-fpm-user=www-data --with-fpm-group=www-data --enable-fpm --with-config-file-scan-dir=/etc/php5/
make && sudo make install


# 手动启动php5 
# sudo vi /etc/apache2/mods-enabled/php7.0.load
# LoadModule php7_module /usr/lib/apache2/modules/libphp7.0.so
# LoadModule php5_module /home/kali/Downloads/php-5.6.10/.libs/libphp5.so
# sudo systemctl restart apache2.service

# /bin/php -i | grep ini    # 看php配置位置
# Configuration File (php.ini) Path => /usr/local/php5.6/lib
# Loaded Configuration File => /usr/local/php5.6/lib/php.ini
