Session 中的反序列化机制：当 session_start () 被调用或者 php.ini 中 session.autostart 为 1 时， PHP 内部调用会话管理器， 当前访问用户 Session 被序列化后存储至指定目录， 默认为/tmp。

PHP 处理器的三种序列化方式:

- php_binary: 键名的长度对应的 ASCII 字符+键名+经过 serialize() 函数序列处理的值
- php: 键名+竖线+经过 serialize() 函数序列处理的值
- php_serialize: serialize() 函数序列处理数组方式

如果网站序列化并存储 Session 与反序列化并读取 Session 的方式不同，就可能导致漏洞的产生。如果存储页面的代码为：

```php
<?php
ini_set('session.serialize_handler', 'php_serialize');
session_start();
$_SESSION['ctf'] = $_GET['ctf'];
?>
```

这是因为，当我们读取页面时，会反序列化已存储的 session,新的 php 处理方式会把“”后的值当作 KEY 值再 serialize (0,相当于我们实例化了这个页面的 ctf 类
`a:1:{s:3:"ctf";s:34:"|O:3:"ctf":1:{s:1:"a";s:4:"ls /";}";}`

处理器为 php 时实际进行反序列化的内容

相当于执行：

```php
$class = new ctf ();
$class->a = 'ls /';
```
