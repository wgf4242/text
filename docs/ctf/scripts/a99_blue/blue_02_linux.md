# Linux

## 隐藏文件

```sh
find . -name ".*"
```

## 隐藏的进程

```sh
pstree
ls -al /proc/*/exe

# 1
cat /proc/$$/mountinfo # $$ 表示当前shell PID
umount /proc/xxxx
# 2
ls -la /proc | sort -nr -k 5 | head -n 10
#
busybox echo $LD_PRELOAD
busybox cat /etc/ld.so.preload
## 发现 libsystem.so
busy stat /etc/libsystem.so

# 3.
busybox ls -alt /etc/systemd/system

## 隐藏原理: 隐藏进程id为42的进程信息：
mkdir /home/kali/tmp/empty
mount -o bind /home/kali/tmp/empty /proc/42
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

```sh
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

## 如何杀死守护进程
ps axj | grep 守护进程名字
kill -9 守护进程名
查看计划任务
排查 /etc/systemd/system
```
