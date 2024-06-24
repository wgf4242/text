# Basic
## Tools

- sshfs 挂载 火绒挂载扫描 测试 矿池扫描
- RdpGuard 是一款基于主机的入侵预防系统(HIPS)，专为保护 Windows 服务器免受各种协议和服务(如 RDP、FTP、IMAP、POP3、SMTP、MySQL、MS-SQL、IIS Web 登录、ASP.net Web 表单、MS Exchange、RD Web 访问、VoIP/SIP 等)的暴力破解攻击而设计。它通过监控服务器上的日志并检测失败的登录尝试来防止未授权访问，从而保护服务器安全。

## 隐藏文件

```sh
find . -name ".*"
```

## 隐藏的进程

```sh
ls -al /proc/*/exe
```

## 挂载linux/可火绒查杀

```sh
winfsp-2.0.23075.msi
sshfs-win-3.5.20357-x64.msi

### 挂载 /home/kali
net use W: \\sshfs\kali@192.168.80.135
### 挂载 /
net use W: \\sshfs\kali@192.168.80.135\/

net use \\sshfs\kali@192.168.80.135 /d
```

## 查杀/Webshell/不死马
1.导出 /var/www/html 在线查杀
https://ti.aliyun.com/#/webshell
https://n.shellpub.com/
2. sshfs 挂载 火绒杀

```
# 查找木马
find ./ -type f -name "*.php" | xargs grep "eval("

哥斯拉病毒是一种Java后门木马，通常用于攻击并控制Web服务器。特征就包括：
<?php
@session_start(); - 开启一个会话。
@set_time_limit(0); - 设置脚本执行时间为无限。
@error_reporting(0); - 关闭所有错误报告。

冰蝎
<?php
@error_reporting(0);
session_start();
    $key="e45e329feb5d925b"
    
    
# 不死马
## 1.看shell
## 2.看计划任务
cat /etc/rc.local
ls /etc/init.d/
systemctl list-unit-files --type=service
```

# Server

```
## IIS

IIS 6.0 及更早版本：
C:\WINDOWS\system32\LogFiles\W3SVC[SiteID]\
IIS 7.0 及更高版本：
C:\inetpub\logs\LogFiles\W3SVC[SiteID]\

# Apache HTTP Server
## Win
C:\Program Files (x86)\Apache Group\Apache2\logs\
C:\Program Files\Apache Group\Apache2\logs\
## 在Linux上，Apache日志文件通常位于以下目录：
/var/log/apache2/access.log
/var/log/httpd/access_log
/var/log/apache2/error.log
/var/log/httpd/error_log

# Nginx
/var/log/nginx/access.log
/var/log/nginx/error.log
tail -f /var/log/apache2/access.log
tail -f /var/log/nginx/access.log
```

## 日志分析

```sh
/var/log/syslog：记录系统的各种信息和错误。
/var/log/auth.log：记录身份验证相关的信息，如登录和认证失败。
/var/log/auth.log.1 SSH登录尝试
/var/log/kern.log：记录内核生成的日志信息。
/var/log/dmesg：记录系统启动时内核产生的消息。
/var/log/boot.log：记录系统启动过程中的消息。
/var/log/messages：记录系统的广泛消息，包括启动和应用程序信息。
/var/log/secure：记录安全相关的消息。
/var/log/httpd/：记录Apache HTTP服务器的访问和错误日志（若安装了Apache）。
/var/log/nginx/：记录Nginx服务器的访问和错误日志（若安装了Nginx）。
```
### ssh
```sh
## 登录失败 https://blog.csdn.net/administratorlws/article/details/139560740
cat auth.log.1 | grep -a "Failed password for root" | awk '{print $11}' | sort | uniq -c | sort -nr | more
## 登录成功的IP
cat auth.log.1 | grep -a "Accepted" | awk '{print $11}' | sort | uniq -c | sort -nr | more
## 登录的用户名
cat auth.log.1 | grep -a "Failed password" |perl -e 'while($_=<>){ /for(.*?) from/; print "$1\n";}'|uniq -c|sort -nr
sudo journalctl -u ssh
## 创建的用户
cat /var/log/auth.log.1 | grep -a "new user"
```
### apache

```
# 当天访问次数最多的IP，即黑客IP：
cut -d- -f 1 access.log.1|uniq -c | sort -rn | head -20
# 查看index.php页面被访问的次数，提交次数：
grep "index.php" access.log | wc -l
cat access.log.1 | grep "/index.php" | wc -l
# 查看黑客IP访问了多少次，提交次数：
cat access.log.1 | grep "192.168.200.2 - -" | wc -l
## 后面–是什么意思？
在 Apache 访问日志中，格式通常是标准的组合日志格式（Combined Log Format），包含了客户端 IP 地址、客户端身份验证信息、用户 ID、请求时间、请求行、状态码、响应大小、引用来源和用户代理等信息。以下是一个典型的日志条目：
例如；
192.168.200.2 - - [03/Aug/2023:08:00:00 +0000] "GET /index.php HTTP/1.1" 200 1234 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
在这个日志条目中，192.168.200.2 是客户端 IP 地址，- - 是占位符，表示客户端身份验证信息（客户端身份验证信息为空时用 - 表示）。

# 从 access.log.1 文件中筛选出指定 IP 地址的访问记录，并统计每个 IP 地址的出现次数。
cat access.log.1 | grep "192.168.200.2" | cut -d' ' -f1 | sort | uniq -c

grep "192.168.200.2" access.log.1 | cut -d' ' -f1 | sort | uniq -c：
  # 直接使用 grep 从文件 access.log.1 中搜索包含 192.168.200.2 的行。
  # 后续步骤提取、排序和统计。-- 这种推荐, 效率更高
cat access.log.1 | grep "192.168.200.2" | cut -d' ' -f1 | sort | uniq -c：
  # 先使用 cat 命令读取整个文件 access.log.1，然后将内容通过管道传递给 grep 进行搜索。
  # 后续步骤与上一个命令相同。

# 查看2023年8月03日8时这一个小时内有多少IP访问，提交次数:
cat access.log.1 | grep "03/Aug/2023:08:" | awk "{print $1}" | sort -nr| uniq -c |wc -l # 加上 wc -l：显示不同 IP 地址的总数量。
cat access.log.1 | grep “03/Aug/2023:08:” | awk ‘{print $1}’ | sort -nr| uniq -c        # 不加 wc -l：显示每个 IP 地址的访问次数。
grep “03/Aug/2023:08:” access.log.1 | awk ‘{print $1}’ | sort -nr | uniq -c | wc -l
```