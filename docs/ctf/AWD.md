[TOC]

awd有时间帮人修复漏洞, 让其他人不能攻，只有自己能进行攻击。

awd平台 https://github.com/vidar-team/Cardinal

连接后先运行 bash

找出ssh连接
ps -ef | grep @pts | grep sshd | awk '{print $9}' # loginuser
ps -ef | grep @pts | grep sshd | awk '{print $2}' # pid
ps -ef | grep @pts | grep sshd | awk '{printf($2); system("kill " $2)}' # pid

修改密码
echo 'ctf:gggggg' | chpasswd


用别人的webshell, 来执行。测试其他IP是否有此shell。

# CTF线下攻防赛

## SSH登录修改账秘

### 下载Web信息

### 上WAF
### 文件监控

log分析 - 利用别人家的脚本

### 端口扫描

## 主机发现

RouterScan.exe , HttpScan.py

### 端口扫描 - Nmap

服务分析

nmap 192.168.50.161
nmap 192.168.0.10 #获取基本信息
nmap -O 192.168.50.161 #获取系统版本信息
nmap -A 192.168.0.10 #获取系统综合信息
nmap 192.168.50.0/24 #获取一个网段工作设备基本信息

nmap -sU -p 1-65535 192.168.50.0/24

sudo nmap --min-hostgroup 100 -F -sS -n -T4 192.168.50.161

nmap -sS -Pn -p 80 -n --open --min-hostgroup 1024 --min-parallelism 10 --host-timeout 30 -T4 -v -oG results-all.txt -iL ipduan.txt
详细说一下各参数的含义：
```
   -sS：使用SYN方式扫描，默认用的是-sT方式，即TCP方式，需要完成完整的三次握手，比较费时，SYN就比较快一些了，具体自己百度了解
   -Pn： 禁用PING检测
   -p： ports，要检测的端口号，比如80
   -n： 功能未知，在V2EX上看到的
   --open： 只输出检测状态为open的端口，即开放的端口，参考文章《快速高效:Nmap结果整理方法》 
   --min-hostgroup 1024：调整并行扫描组的大小，参考文章《详尽的Nmap扫描参数解析》 
   --min-parallelism 1024：调整探测报文的并行度
   --host-timeout 30：检测超时的跳过 
   -T4：总共有T0-T5，貌似T4比较折中，参考文章《Nmap参考指南：十一、 时间和性能》
    -v：打印详细扫描过程
    -oG：输出为比较人性化的格式，一条记录一行，后期好处理
   -iL：载入ip段文件，批量扫，不用一条条执行了。
   -F: Fast - Scan only the ports listed in the nmap-services file)
```
### 黑盒测试

* 目录扫描
    
    * 后门爆破 - k8一句话爆破
    * k8fly

#### 权限维持

种植不死马(文件隐藏) - 条件竞争 - 批量上传+批量访问

    不死马解决方案： 1.杀进程 2.竞争写入3.断Apache（被发现扣分）
    最好是种md5马。防止反打。
    echo system("curl 10.0.0.1") => 批量获取

反弹shell

信息隐藏

     文件前面加.比如1.php => .1.php
     多个目录下种马，asp, jsp马都尝试下。

[AWD线下备忘录](https://www.fuzzer.xyz/2019/04/02/AWD线下准备指南/)

#### 清除痕迹

var/log, 日志
bash_history等 等

# AWD 
ABC3人

1.dump目录的源码。。。备份下。 /var/www/html，
2.D盾扫一下。
2.1 同时派一个人 nmap等工具 信息收集
关闭非必要端口，留下基本端口。
看下目录结构。
准备waf，放上，然后测试自己主机的服务（不要让自己的主机当机）。主办方定时会check基本服务有没有。
上文件监控和流量监控(Wireshark监控一下)
看/var/log 里的日志。

   
自动化批量提交脚本, curl, getflag,

## 攻击流程

3. 上WAF、上监控、只留必要端口

部署WAF

部署文件监控脚本

部署流程监控脚本或开启服务器日志记录。

[AWD攻防赛之各类漏洞FIX方案](https://www.freebuf.com/articles/web/208778.html)

## 常用命令

    ssh <-p 端口>  用户名@IP
    scp 文件路径  用户名@IP：存放路径
    tar -zcvf web.tar.gz /var/www/html
    pkill -kill -t <用户tty>

查看已建立网络连接及进程

    netstat -antulp | grep EST

查看指定端口被哪个进程占用

    lsof -i:端口号 或者 netstat -tunlpl | grep 端口号

结束进程命令

    kill PID
    killall <进程名>
    kill - <PID>

封杀某个IP或者ip段， 如:

    iptables -I INPUT -s . j DROP 
    iptables -I INPUT-S ./ j DROP

禁止从某个主机ssh远程访问登陆到本机，如123..

    iptable -t filter -A INPUT -s . p tcp -- dport j DROP

备份mysql数据库

    mysqldump -u 用户名 -p密码 数据库名 > back.sql
    mysqldump --all-databases >> bak.sql

还原mysql数据库

    mysql -u 用户名 -p 密码 数据库名 < bak.sql
    find / *.php -perm
    awk -F: /etc/passwd
    crontab -l

检测所有的tcp连接数量及状态

    netstat --ant | awk | grep | sed -e -e | sort | uniq -c | sort -rn

查看页面访问排名前十的IP
    
    cat /var/1og/apache2/access.1og | cut -f1 -d | sort | uniq -c | sort -k -r | head

查者页面访问排名前十的URL

    cat /var/log/apache2/access.log | cut -f4 -d | sort | uniq -c | sort -k -r | head

## 资源分享

[AWD 资源小合集(持续更新)](https://neversec.top/20190415/how-to-awd.html)

[linux-kernel-exploits](https://github.com/SecWiki/linux-kernel-exploits)

[AWD线下赛脚本集合](https://github.com/admintony/Prepare-for-AWD)

### 常用工具

    Burpsuite
    Sqlmap
    Nmap、masscan、 御剑、wpscan
    nc
    D盾、Seay、 Rips、 安全狗
    MobaXterm、Xshell、 Xftp
    菜刀或蚁剑
    Chrome、Firefox各类插件
    Hackbar
    Kali
    Python的各类函数库、软件包

### 代码比较工具

BeyondCompare(Windows)

Kaleidoscope(MacOS)

### 一句话木马

php,asp,aspx,jsp, 内存马

## 其他准备

提前准备好各种cmd的poc、exp(phpwin, phpcms, dz)

还有各种自动化脚本，起码有个模板
