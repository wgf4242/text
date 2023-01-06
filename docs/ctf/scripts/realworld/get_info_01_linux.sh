#!/bin/bash

# 输出文件
filename=$(date +%s)'.log'

a="uname -a    #uname -a
uname -m    #uname -m
cat /proc/version    #version
cat /etc/*-release   #release
cat /etc/issue    #issue
hostname    #hostname
cat /etc/passwd    #passwd
cat /etc/group    #group
getent group sudo #imsudo
w    #w
whoami    #whoami
id    #id
sudo -l    #sudo -l
ps aux    #ps aux
ls -la /etc/cron*    #cron
ls -la /tmp #tmp
ip a | awk '{print $2,$4}' #IP和网卡信息
cat /etc/network/interfaces    #interfaces
arp -a    #arp
route    #route
history    #history
netstat -anplt    #netstat
cat /etc/resolv.conf #dnsinfo
iptables -L    #iptable"

while IFS='#' read -r line label; do
  echo -e "========== $label: \n$($line)\n\n" >> $filename
done <<< "$a"


echo -e "\n" | tee -a $filename
echo "========== 增加用户的日志" | tee -a $filename
grep "useradd" /var/log/secure  | tee -a $filename
cat ~/.*history | tee -a $filename
echo -e "\n" | tee -a $filename
echo "登录成功的IP" | tee -a $filename
grep "Accepted " /var/log/secure* | awk '{print $11}' | sort | uniq -c | sort -nr | more | tee -a $filename   
echo -e "\n" | tee -a $filename
echo "查看 SSH key" | tee -a $filename
sshkey=${HOME}/.ssh/authorized_keys
if [ -e "${sshkey}" ]; then
    cat ${sshkey} | tee -a $filename
else
    echo -e "SSH key文件不存在\n" | tee -a $filename
fi
echo -e "\n" | tee -a $filename
echo "查看 known_hosts" | tee -a $filename
cat ~/.ssh/known_hosts | tee -a $filename
echo -e "\n" | tee -a $filename
echo "查找WEB-INF" | tee -a $filename
find / -name *.properties 2>/dev/null | grep WEB-INF | tee -a $filename
echo -e "\n" | tee -a $filename
echo "user|pass|pwd|uname|login|db_" | tee -a $filename
find / -name "*.properties" | xargs egrep -i "user|pass|pwd|uname|login|db_" | tee -a $filename
echo -e "\n" | tee -a $filename
echo "jdbc:|pass=|passwd=" | tee -a $filename
find / -regex ".*\.properties\|.*\.conf\|.*\.config\|.*\.sh" | xargs grep -E "=jdbc:|pass=|passwd=" | tee -a $filename
echo -e "\n" | tee -a $filename
# Author cances
echo -e "\n" | tee -a $filename
echo "可登陆用户" | tee -a $filename
cat /etc/passwd | grep -E -v 'sync$|halt$|nologin$|false|shutdown' | tee -a $filename
echo -e "\n" | tee -a $filename
echo "用户登陆日志" | tee -a $filename
lastlog | tee -a $filename
echo -e "\n" | tee -a $filename
echo "查看 hosts" | tee -a $filename
cat /etc/hosts | tee -a $filename
echo -e "\n" | tee -a $filename
