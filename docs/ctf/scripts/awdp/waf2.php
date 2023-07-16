<?php

$str ="";
foreach ($_POST as $key => $value) {
    $str.=$value;
}
foreach ($_GET as $key => $value) {
    $str.=$value;
}
if (preg_match("/openlog|syslog|readlink|symlink|popepassthru|stream_socket_server|scandir|pcntl_exec|fwrite|curl|system|eval|assert|flag|passthru|exec|chroot|chgrp|chown|shell_exec|proc_open|proc_get_status|popen|ini_alter|ini_restore|http|cookie|script|select|into|from|where|join|sleexml|extractvalue|regex|copy|read|file|create|grand|dir|insert|link|server|drop|=|>|<|;|\"|\'|\^|\|/i", $str)) {
    die('no!');
}

?>
