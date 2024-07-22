# windows 溯源

everyting 搜索 exe 倒序排列

windows 下进程执行了什么在哪里看。

```sh
md C:\wgflog
cd /d C:\wgflog
netstat -aon > netstat_01_aon.txt
netstat -abn > netstat_02_abn.txt
dir /a %userprofile%\AppData\Roaming\Microsoft\Windows\Recent > 10_recent.txt

# everything
.exe file: dc:>=2024/04/18
```

# linux 1.取证

取证

```sh
# 切 root
sudo su
cd /tmp
mkdir log/files
cd log/files
cat /etc/passwd                      > 01_passwd.txt
ps -ef                               > 10_ps_ef.txt
ps aux                               > 10_ps_aux.txt
netstat -apnt                        > 11_netstat.txt
lsof -i                              > 12_lsof.txt
tac ~/.bash_history                  > 02_bash_history.txt
crontab -l                           > 03_crontab_l.txt
cat /var/spool/cron/*                > 03_crontab.txt
last                                 > 05_last.txt
# Accepted password 为登录成功
tail -n +1  /var/log/secure  | less  > 06_secure.log
last                                 > 07_last.log
lastb                                > 08_lastb.log
tac /var/log/auth.log | more         > 09_auth.log  # - 记录系统认证和授权相关的事件，包括登录尝试。
more /etc/passwd | egrep -v '^#|^(\+:\*)?:0:0:::' | awk -F: '{if($3==0) print $1}' > 09_uid_is_0.log  # - 记录系统认证和授权相关的事件，包括登录尝试。
more /etc/group | grep -v '^#' | gawk -F: '{if ($1!="root"&&$3==0) print $1}' > 09_root_group_user.log
ls -alt /etc/rc.local 
ls -alt /etc/rc.d/rc[0~6].d
ls -alt /etc/init.d
find /home -type f -executable -mtime -3 > 04_exefiles.txt
tar zcvf ../log-$(date +%F-%H%M%S).tar.gz ./

不同用户的历史命令 /home/test/.bash_profile
可疑进程 ls -alt /proc/pid, exec ->xxx 对应的即为文件位置
tac /var/log/secure           - 包含类似于 auth.log 的信息，但在某些 Linux 发行版中使用。
tac /var/log/messages         - 记录系统的各种消息和事件，包括登录尝试。
/var/log/syslog               - 包含系统日志的综合记录，可能包括登录尝试。


/usr/bin  查看
/usr/lib  查看
# 6、分析数据库的日志
# 4、分析中间件日志
## apache
Windows: <Apache安装目录>\logs\access.log
Linux:  /usr/local/apache/logs/access_log
若不存在，参考Apache配置文件httpd.conf中相关配置
/etc/httpd/logs/access_log
/var/log/httpd/access_log
## tomcat
tomcat\access_log
## IIS服务器
默认位置：%systemroot%\system32\logfiles\ 
## nginx服务器
日志存储路径在Nginx配置文件中 access***
```

linux 搜索 +x 时间倒序排列.
# 溯源
```
百度ID
新浪ID
根据QQ号  搜Q群/微信
博客溯源
手机号溯源 先存到通讯录, 再查看钉钉、支付宝、微信，qq是否绑定。
邮箱溯源 www.reg007.com, 邮箱忘记密码 查看手机号
域名反查  站长工具, 微步(高级账户)
IP地址定位  https://www.opengps.cn/Data/IP/ipplus.aspx
telegram内置大量社工库
```
# 应用系统

## 泛微

## 帆软

| 1           | 2                                   | 3                         |
| ----------- | ----------------------------------- | ------------------------- |
| \* 访问日志 | localhost_access_log.2024-04-18.txt | 有 POST 请求大小，无 body |
| 报错信息    | catalina.2024-04-19.log             |
| 异常信息    | fanruan.log.2024-04-18.gz           |

filter log
```
/webroot/decision/login HTTP/1.1" 200 \d{5,}
channel HTTP/1.1" 200 \d{5,}
```