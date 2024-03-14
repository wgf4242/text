<?php
// http://localhost/@training/file.php?file=php://filter/read=convert.base64-encode/resource=../index.php

include($_GET['file']);
highlight_file(__FILE__);
