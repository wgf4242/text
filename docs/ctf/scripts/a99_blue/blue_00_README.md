# Basic

## Tools

- sshfs 挂载 火绒挂载扫描 测试 矿池扫描
- RdpGuard 是一款基于主机的入侵预防系统(HIPS)，专为保护 Windows 服务器免受各种协议和服务(如
  RDP、FTP、IMAP、POP3、SMTP、MySQL、MS-SQL、IIS Web 登录、ASP.net Web 表单、MS Exchange、RD Web 访问、VoIP/SIP 等)
  的暴力破解攻击而设计。它通过监控服务器上的日志并检测失败的登录尝试来防止未授权访问，从而保护服务器安全。
- [web 日志取证分析工具](https://security.tencent.com/index.php/opensource/detail/15)

```sh
perl ./LogForensics.pl -file logfile -websvr (nginx|httpd) [-ip ip(ip,ip,ip)|-url url(url,url,url)]
./LogForensics.pl -file /var/log/nginx/access.log -websvr nginx

/var/log/nginx/access.log.db
/var/log/nginx/access.log.log
```

# Server

```sh
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

### apache/nginx

```sh
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
grep "03/Aug/2023:08:" access.log.1 | awk '{print $1}' | sort -nr | uniq -c | wc -l

# nginx access.log 访问日志中的 IP 地址，并统计每个 IP 地址的访问次数
cut -d- -f 1 /var/log/nginx/access.log|uniq -c | sort -rn | head -20
## 攻击者目录扫描所使用的工具名称
cat access.log | grep HEAD | head -n 20
## 提交攻击者首次攻击成功的时间
cat access.log | grep POST | head -n 20
cat access.log | awk '/POST / {print $1, $6, $7}' | sort | uniq -c | sort -nr
## 显示404状态的IP访问次数
grep -v "GET /favicon.ico" access.log  | awk '/404 / {print $1}' | sort | uniq -c | sort -nr # 去掉 /favicon.ico
## 根据数据流量传输量找出攻击者/根据IP分组汇总数量传输量
awk '{sum[$1]+=$10} END {for (ip in sum) print "IP:", ip, "Total Size:", sum[ip]}' access.log | sort -nr -k5 | more
awk '{sum[$1]+=$10} END {for (ip in sum) print "IP:", ip, "Total Size:", sum[ip]}' access.log
## 找到攻击者写入的恶意后门文件
find / -name a.php
## 找到攻击者隐藏在正常web应用代码中的恶意代码
一个一个看 或者
grep -E 密码 ./
grep -r '\/\*-\*\/'

## 识别系统中存在的恶意程序进程/黑客留下的后门中黑客服务器的ip及端口
ps -aux
ls /var/spool/cron/
find /var/spool/cron/ /var/spool/anacron/ -type f -exec cat {} \;
cat /etc/anacrontab

## 修复漏洞
查看 index.php 末尾看是什么系统 找到修复方法修复
### Windows

```

# 题目类型

## 黑客首次入侵方式

- 先看 POST 请求, 也许有 script -> XSS

## 黑客添加的账号并删除

```
cat /etc/passwd
userdel aman
groupdel aman
```

## 修复黑客篡改的命令并且删除篡改命令生成的免杀马

```sh
# 有没有类似 ps_, ls2 的文件
ps
ls -la /bin/
```

## 修复 js 劫持

```sh
find . | xargs grep -ri '<script type="text/javascript">' -l | sort | uniq -c
grep -ri '<script type="text/javascript">' -l | sort | uniq -c
```

## 提权方式

查看日志 及 搜索 udf.dll|udf.so

## 黑客上传的 webshell

https://ti.aliyun.com/#/webshell 检测

```sh
## 120 分钟内/2 小时内修改过的文件
find . -name '*.php|jsp|asp|java' -mmin -120
find /var/www/html/ -ctime 0 -name "*.ph*" | grep -v /proc/ # 查找今天生成的文件
# windows 用 everything
```

## 识别系统中存在的恶意程序进程 2 - 提交 C&C 服务器 IP 地址和端口

- Linux

```sh
pkill -9 php-fpm
./php-fpm &
netstat -apntu | grep php
netstat -anp

psg              # 查询全部进程
psg -u root      # 查询用户root的进程：
psg -s R         # 查询状态为R（运行中）的进程：
psg -f nginx     # 查询进程名包含”nginx”的进程：
psg -u root -f   # 查询用户root并显示完整信息的进程：
psg -g 1         # 查询进程组为1的进程：
```

- Windows

netstat -ano # SYN_SEND 连接模式

## 删除黑客留下的后门木马

- autoruns 查看

- %userprofile\AppData\Roaming\Microsoft\Windows\Start Menu\Programs
- 所有用户的 startup
- 计划任务
  计算机\HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Run
  计算机\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run

# Untitled

[Redis](https://blog.csdn.net/administratorlws/article/details/140024637)
[Linux | 记录某次"有趣的"挖矿木马排查](https://xz.aliyun.com/t/14548)

## 工具

[Live-Forensicator](https://github.com/Johnng007/Live-Forensicator) [介绍](https://www.freebuf.com/articles/security-management/328804.html)
[GitHub - RoomaSec/RmTools: 蓝队应急工具](https://github.com/RoomaSec/RmTools)
