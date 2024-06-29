#!/bin/bash
user=root
pass=root
secure_pass=AnyWhereis5@0
# mysql -u$user -p$pass -e "DROP USER ''@'$(hostname)'"
# 防写日志
# revoke ALL on *.* from admin@'%';

# .sql
# mysql -sfu root < "mysql_secure_installation.sql"
# $ mysql -h "server-name" -u "root" "-pXXXXXXXX" "database-name" < "filename.sql"

# --- Generate sql file ---
tee secure_mysql.sql <<-EOF
use mysql;
CREATE USER 'root'@'%' IDENTIFIED BY '$secure_pass';
UPDATE mysql.user SET authentication_string = PASSWORD('$secure_pass') WHERE User = 'root';
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY '$secure_pass';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
## GRANT ALL PRIVILEGES ON *.* TO 'root'@'%';
## use mysql;update user set grant_priv='y' where user='root' and host='%';
# mysql5 update password sql
UPDATE mysql.user SET Password = PASSWORD('$secure_pass') WHERE User = 'root';
DROP USER ''@'';
DROP USER ''@'localhost';

DELETE FROM mysql.user WHERE User='';
DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1', '::1');
DROP DATABASE IF EXISTS test;
DELETE FROM mysql.db WHERE Db='test' OR Db='test\\_%';
EOF

if [ -f "/etc/my.cnf" ]; then
    file="/etc/my.cnf"
else
    file="/etc/mysql/my.cnf"
fi

# --- secure my.cnf ---
bind_addr() {
  property="bind_address"
  value="127.0.0.1"

  # 检查 my.cnf 文件中是否存在 [mysqld] 属性
  if grep -q "bind_address" $file; then
    # 如果存在，使用 sed 命令进行修改
    sed -i "s/\($property *= *\).*/\1$value/" $file
  else
    # 如果不存在，使用 echo 命令添加 [mysqld] 和属性
    sed -i "s/\(\[mysqld\]\)/\1\n$property=$value/" $file
  fi
}

sed -i '/secure_file_priv/d' $file
sed -i '/secure-file-priv/d' $file
echo "显式增加 secure_file_priv = NULL"
bind_addr

echo systemctl restart mysqld
echo service mysql restart

# force 忽略错误执行
mysql -u$user -p$pass --force < "secure_mysql.sql"
