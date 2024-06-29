<?php
$str ="";
foreach ($_POST as $key => $value) {
    $str.=$value;
}
foreach ($_GET as $key => $value) {
    $str.=$value;
}
$str.=file_get_contents('php://input'); // 支持过滤xxe
$pattern="system|passthru|exec|shell_exec|proc_open|popen|pcntl_exec|ob_start";
$pattern.="|eval|assert|preg_replace|create_function|array_map|call_user_func|call_user_func_array";
$pattern.="|include|require|include_once|require_once";
$pattern.="|readfile|file_get_contents|file_put_contents|unlink|move_uploaded_file";
$pattern.="|select|and|or|into|from|where|join|sleexml|extractvalue|regex|copy|read|file|create|grand|dir|insert|link|server|drop";
$pattern.="|http|cookie|script";
$pattern.="|\/|\@|\=|\>|\<|\;|\"|\'|\^|\`";
$pattern.="|base64";
$pattern.="|flag";
$pattern.="|public|DOCTYPE|ENTITY";
$pattern.="|dict\:\/\/|gopher\:\/\/|file\:\/\/"; // ssrf
if (preg_match("/".$pattern."/i", $str)) {
    die('no!');
}

?>