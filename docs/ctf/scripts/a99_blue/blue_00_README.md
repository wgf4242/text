# Basic

## Tools

- sshfs 挂载 火绒挂载扫描 测试 矿池扫描
- RdpGuard 是一款基于主机的入侵预防系统(HIPS)，专为保护 Windows 服务器免受各种协议和服务(如
  RDP、FTP、IMAP、POP3、SMTP、MySQL、MS-SQL、IIS Web 登录、ASP.net Web 表单、MS Exchange、RD Web 访问、VoIP/SIP 等)
  的暴力破解攻击而设计。它通过监控服务器上的日志并检测失败的登录尝试来防止未授权访问，从而保护服务器安全。
- [web日志取证分析工具](https://security.tencent.com/index.php/opensource/detail/15)

```sh
perl ./LogForensics.pl -file logfile -websvr (nginx|httpd) [-ip ip(ip,ip,ip)|-url url(url,url,url)]
./LogForensics.pl -file /var/log/nginx/access.log -websvr nginx

/var/log/nginx/access.log.db	
/var/log/nginx/access.log.log	
```

## 隐藏文件

```sh
find . -name ".*"
```

## 隐藏的进程

```sh
ls -al /proc/*/exe
```

## 挂载 linux/可火绒查杀

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
## 找到攻击者写入的恶意后门文件
find / -name a.php
## 找到攻击者隐藏在正常web应用代码中的恶意代码
一个一个看 或者
grep -E 密码 ./
grep -r '\/\*-\*\/'

## 识别系统中存在的恶意程序进程/黑客留下的后门中黑客服务器的ip及端口
ps -aux
ls /var/spool/cron/
find /var/spool/cron/ -type f -exec cat {} \;

## 修复漏洞
查看 index.php 末尾看是什么系统 找到修复方法修复
### Windows

```

### evtx

[evtx](https://blog.csdn.net/administratorlws/article/details/139887217)

找到关键“登录”，事件 ID 4624

| 1          | 2               |
|------------|-----------------|
| 事件 ID 4624 | 成功的账户登录         |
| 事件 ID 4625 | 登录失败            |
| 事件 ID 4634 | 用户注销            |
| 事件 ID 4647 | 用户主动注销          |
| 事件 ID 4624 | 成功的账户登录         |
| 事件 ID 4625 | 登录失败            |
| 事件 ID 4634 | 用户注销            |
| 事件 ID 4647 | 用户主动注销          |
| 事件 ID 4720 | 用户账户已创建         |
| 事件 ID 4722 | 用户账户已启用         |
| 事件 ID 4725 | 用户账户已禁用         |
| 事件 ID 4726 | 用户账户已删除         |
| 事件 ID 4670 | 权限服务状态变更        |
| 事件 ID 4719 | 系统审计策略已更改       |
| * 系统事件     |                 |
| 事件 ID 6005 | 事件日志服务启动        |
| 事件 ID 6006 | 事件日志服务停止        |
| 事件 ID 6008 | 系统意外关机          |
| 事件 ID 4672 | 特权服务已分配         |
| 事件 ID 4673 | 特权服务已请求         |
| * 防火墙事件    |                 |
| 事件 ID 4946 | Windows 防火墙规则添加 |
| 事件 ID 4947 | Windows 防火墙规则修改 |
| * 文件访问     |                 |
| 事件 ID 4663 | 记录对象访问尝试的安全审计事件 |
| * 服务状态     |                 |
| 事件 ID 7036 | 服务已更改状态（如启动或停止） |

# 题目类型

## 黑客首次入侵方式

* 先看POST请求, 也许有script -> XSS

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

## 修复js劫持

```sh
find . | xargs grep -ri '<script type="text/javascript">' -l | sort | uniq -c
grep -ri '<script type="text/javascript">' -l | sort | uniq -c
```

## 提权方式
查看日志  及 搜索 udf.dll|udf.so

## 黑客上传的webshell
https://ti.aliyun.com/#/webshell 检测

## 识别系统中存在的恶意程序进程2 - 提交C&C服务器IP地址和端口
* Linux
 
```sh
pkill -9 php-fpm
./php-fpm &
netstat -apntu | grep php
```

* Windows

netstat -ano  # SYN_SEND连接模式

## 删除黑客留下的后门木马

* autoruns 查看
 
* %userprofile\AppData\Roaming\Microsoft\Windows\Start Menu\Programs
* 所有用户的 startup
* 计划任务
计算机\HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Run
计算机\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run

# Windows 

```sh
#只允许超级管理员（administrator）关闭操作系统
管理工具 -> 本地安全策略 ->  本地策略 -> 用户权限分配 ->关闭系统 删除其他用户

#设置远程桌面用户空闲会话超过5分钟自动断开连接
win+r-gpedit.msc -> 计算机配置 -> 管理模板 -> Windows 组件 -> 远程桌面服务 -> 远程桌面会话主机-> 会话时间限制 > 设置活动但空闲的远程桌面服务会话的时间限制 10分钟
## 值为秒支持16进制 0x000927c0
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services" /v MaxIdleTime /t reg_dword /d 600000 /f

#开启开启IIS的日志审计记录
服务器管理 -> 用户  -> Web服务器IIS -> 角色服务 添加角色服务 -> 健康与诊断 -> 勾选HTTP日志记录

#九、 ftp安全 关闭ftp匿名用户（注意ftp服务不能关闭）
控制面板 -> 管理工具 -> IIS管理器 -> ftp身份验证禁用匿名用户
```
# Untitled

[Redis](https://blog.csdn.net/administratorlws/article/details/140024637)
