#!/bin/bash
user=root
pass=AnyWhereis5@0

# mysql -u$user -p$pass -e "DROP USER ''@'$(hostname)'"
# 防写日志
# revoke ALL on *.* from admin@'%';

# .sql
# mysql -sfu root < "mysql_secure_installation.sql"
# $ mysql -h "server-name" -u "root" "-pXXXXXXXX" "database-name" < "filename.sql"

# --- Generate sql file ---
tee secure_mysql.sql <<-EOF
use mysql;
CREATE USER 'root'@'%' IDENTIFIED BY 'AnyWhereis5@0';
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'AnyWhereis5@0';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%';
# mysql5 update password sql
UPDATE mysql.user SET Password = PASSWORD('AnyWhereis5@0') WHERE User = 'root';
DROP USER ''@'';
DROP USER ''@'localhost';

DELETE FROM mysql.user WHERE User='';
DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1', '::1');
DROP DATABASE IF EXISTS test;
DELETE FROM mysql.db WHERE Db='test' OR Db='test\\_%';
EOF

# force 忽略错误执行
mysql -u$user -p$pass --force < "secure_mysql.sql"

# --- secure my.cnf ---
bind_addr() {
  property="bind_address"
  value="127.0.0.1"

  # 检查 my.cnf 文件中是否存在 [mysqld] 属性
  if grep -q "bind_address" /etc/my.cnf; then
    # 如果存在，使用 sed 命令进行修改
    sed -i "s/\($property *= *\).*/\1$value/" /etc/my.cnf
  else
    # 如果不存在，使用 echo 命令添加 [mysqld] 和属性
    sed -i "s/\(\[mysqld\]\)/\1\n$property=$value/" /etc/my.cnf
  fi
}

sed -i '/secure_file_priv/d' /etc/my.cnf
bind_addr
