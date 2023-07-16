<!-- java filter https://github.com/Drun1baby/JavaSecFilters -->
<?php

$dbms="mysql";
$host = "127.0.0.1";
$username = "root";
$password = "root";
$dbName = "fish";
$conn=new PDO("$dbms:host=$host;dbname=$dbName", $username, $password);
function waf($s){
  if (preg_match("/select|flag|update|sleep|extract|show|tables|extractvalue|union|floor|table|and|or|delete|insert|updatexml|truncate|char|into|substr|ascii|declare|exec|count|master|drop|execute|\\\\$|\'|\"|--|#|-|\*|\/|\n| |\t|alert|img|prompt|set|\.|if|\^|\+|hex|0x|0b1111101000|\?|desc|order by|order|by|~~|`|ord|group_concat|concat|limit|alter|read|rename|columns|replace|=|\>|\<|\(|\)|\||database|information_schema|where|from|prepare|like|rlike|regexp|left|right|mid|as|handler|next|close|load_file/is", $s) ||strlen($s)>1000){
    header("Location: /");
    die();
  }
}

foreach ($_GET as $key => $value) {
    waf($value);
}

foreach ($_POST as $key => $value) {
    waf($value);
}

foreach ($_SERVER as $key => $value) {
    waf($value);
}

?>