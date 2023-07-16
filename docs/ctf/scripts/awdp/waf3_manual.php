<?php

function waf($str){
    return preg_replace("/cookie|http|script|openlog|syslog|readlink|symlink|popepassthru|stream_socket_server|scandir|assert|pcntl_exec|fwrite|curl|system|eval|flag|passthru|exec|chroot|chgrp|chown|shell_exec|proc_open|proc_get_status|popen|ini_alter|ini_restore|select|and|or|into|from|where|join|sleexml|extractvalue|regex|co py|read|file|create|grand|dir|insert|link|server|drop|=|>|<|;|\"|\'|\^|\|/i","",$str);
}
?>