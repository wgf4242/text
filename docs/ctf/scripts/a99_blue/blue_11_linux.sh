mkdir -p tmp/redis
copy /etc/redis/redis.conf tmp/redis

# 2.关闭不便用的服务
首先查看露些服务是开启的:
chkconfig --list |grep '3:on'
# 关闭邮件服务,使用公司邮件服务器:
service postfix stop
chkconfig postfix--level 2345 off
# 关闭 ns 服务及客户端:
service netfs stop
chkconfig netfs --level 2345 off
service nfslock stop
chkconfig nfslock --level 2345 off

# 增强特殊文件权限
chattr +i /etc/passwd
chattr +i /etc/shadow
chattr +i /etc/group
chattr +i /etc/gshadow
chattr +i /etc/services
#给系统服务端口列表文件加锁,防止未经许可的到除或添加服务
chattr +i /etc/pam.d/su
chattr +i /etc/ssh/sshd_config

echo "------------禁用不使用的用户, 注释掉------------"
cat /etc/passwd

echo "------------防止一般网络攻击 ------------"
echo 1 > /proc/sys/net/ipv4/icmp_echo_ignore_all

# 或便用 iptable 禁 ping,当然前提是你启用了 iptables 防义增,
iptables -A INPUT -p icmp --icmp-type 0 -s 0/0 -j DROP
# 不允许 ping 其他主机:
iptables -A OUTPUT -p icmp --icmp-type 8 -j DROP

