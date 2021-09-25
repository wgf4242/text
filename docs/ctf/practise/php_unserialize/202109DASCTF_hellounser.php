<?php
class A {
    public $var;
    public function show(){
        echo $this->var;
    }
    public function __invoke(){
        $this->show();
    }
}

class B{
    public $func;
    public $arg;

    public function show(){
        $func = $this->func;
        if(preg_match('/^[a-z0-9]*$/isD', $this->func) || preg_match('/fil|cat|more|tail|tac|less|head|nl|tailf|ass|eval|sort|shell|ob|start|mail|\`|\{|\%|x|\&|\$|\*|\||\<|\"|\'|\=|\?|sou|show|cont|high|reverse|flip|rand|scan|chr|local|sess|id|source|arra|head|light|print|echo|read|inc|flag|1f|info|bin|hex|oct|pi|con|rot|input|\.|log/i', $this->arg)) {
            die('No!No!No!');
        } else {
            include "flag.php";
            //There is no code to print flag in flag.php
            $func('', $this->arg);
        }
    }

    public function __toString(){
        $this->show();
        return "<br>"."Nice Job!!"."<br>";
    }


}

if(isset($_GET['pop'])){
    $aaa = unserialize($_GET['pop']);
    $aaa();
}
else{
    highlight_file(__FILE__);
}

?>