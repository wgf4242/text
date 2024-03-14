<?php
function fetchUrlContent($url)
{
//    // 允许的协议列表
//    $allowedProtocols = ['http', 'https'];
//
//    // 分离协议部分
//    $protocol = parse_url($url, PHP_URL_SCHEME);
//
//    // 检查协议是否在允许的协议列表内
//    if (!in_array($protocol, $allowedProtocols)) {
//        die('Invalid protocol provided. Only "http" and "https" are allowed.');
//    }

    // 尝试获取内容
    $content = @file_get_contents($url);

    // 检查是否成功获取内容
    if ($content === false) {
        die('Failed to fetch content from the given URL.');
    }

    return $content;
}

// 假设$_GET['url']是由用户提供的URL参数
if (isset($_GET['url'])) {
    $url = filter_input(INPUT_GET, 'url', FILTER_SANITIZE_URL);
    echo fetchUrlContent($url);
} else {
    echo 'Please provide a URL via the "url" query parameter.';
}
?>