<?php

namespace MyTest1{
    class Test {}
    function test() {}
}

namespace MyTest2{
    class Test {}
    function test() {}
}

namespace {
    $v = new MyTest2\Test();
    $s = new MyTest1\Test();
    $s->xxx = $v;
    echo serialize($s);
}