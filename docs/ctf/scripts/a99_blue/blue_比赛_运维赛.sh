#  查看特权用户
awk -F: '{if($3==0) print $1}' /etc/passwd 

# 隐藏文件
## 使用命令查找隐藏文件,发现...进行删除 .
ls -A /*  | grep "^\."

# 命令劫持 , 找到~/.bashrc 删除相关
echo $LD_PRELOAD
## 用chattr去掉特殊权限，进行删除hook文件。
## chattr -i xx.so && chattr -a xx.so && rm -f xx.so

# suid
find / -user root -perm -4000 -exec ls -ldb {} \;

# 恶意进程
ps -ef | grep python

# Apache设置禁止访问网站目录
vim /etc/httpd/conf/httpd.conf
Options Indexes FollowSymLinks 修改为：Options FollowSymLinks

# 9.mysql安全加固
## 查看发现mysql存在弱口令 root root ，更改root口令为强口令。
update user set authentication_string=password("AnyWhereis5@0") where user='root';

# php漏洞修改
libxml_disable_entity_loader(true);  改为 false避免产生XXE漏洞