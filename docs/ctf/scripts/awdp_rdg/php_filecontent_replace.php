<?php
// 删除 php 字符
move_uploaded_file($tmp_name, "$uploads_dir/$filename");

$handle = fopen("$uploads_dir/$filename", "r");
$contents = fread($handle, filesize($filename));
fclose($handle);


$s2 = str_replace("php", "", $contents);
echo $s2;
$handle = fopen("$uploads_dir/$filename", "w");
fwrite($handle, $s2);
fclose($handle);