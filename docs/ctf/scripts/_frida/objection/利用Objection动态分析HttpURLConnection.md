[利用Objection动态分析HttpURLConnection](https://mp.weixin.qq.com/s/dIKGsYlQQtuWBU-7trLBCA)


```sh
# Hook 类构造方法
android hooking watch class_method java.net.URL.$init --dump-args --dump-backtrace --dump-return

(agent) [399935] Arrguments jav.net.URL.URL(http://www.baidu.com)
## 通过 url 字符串构造的URL对象

# Hook setRequestProperty()方法，发现无日志信息。
android hooking watch class_method java.net.HttpURLconnection.setRequestPropterty --dump-args --dump-backtrace --dump-return

# Hookjava.net.HttpURLConnection整个类的方法调用，观察调用了哪些方法。
android hooking watch class HttpURLconnection
(agent) [672010] Called java.net.HttpURLconnection.getFollowRedirects()
## 发现只Hook到了getFollowRedirects()方法
## 当hook HttpURLConnection类的方法时，没有打印出预想的setRequestProperty()、setRequestMethod()等方法的调用，这是因为HttpURLConnection是一个抽象类，无法创建对象实例所以内存中没有对象实例，需要Hook它的子类实例。

## 通过断点调试查看实现HttpURLConnection的子类实例。在获取HttpURLConnection对象后断点。
## HttpURLConnectoin具体实现类com.android.okhttp.internal.huc.HttpURLConnectionImpl

# hook com.android.okhttp.internal.huc.HttpURLConnectionImpl类获取请求头部和参数信息。
android hooking watch class com.android.okhttp.internal.huc.HttpURLConnectionImpl
## 这次看到 setRequestMethod() 和 setRequestProperty() 等方法被调用

```

* 根据Hook HttpURLConnection的结果编写“自吐”脚本
```
function main(){
    Java.perform(function(){
        var URL = Java.use("java.net.URL")
        var HttpURLConnection = Java.use("com.android.okhttp.internal.huc.HttpURLConnectionImpl")
        var BufferedReader = Java.use("java.io.BufferedReader")
        var StringBuilder = Java.use("java.lang.StringBuilder")
        var InputStreamReader = Java.use("java.io.InputStreamReader")

        // Hook URL构造方法获取请求url
        URL.$init.overload("java.lang.String").implementation = function(url){
            console.log("--NetWork Start--")
            console.log("--url--", url)
            this.$init(url)
        }

        // Hook setRequestMethod方法获取请求方法
        HttpURLConnection.setRequestMethod.implementation = function(method){
            console.log(method)
            this.setRequestMethod(method)
        }

        // Hook setRequestProperty方法获取请求参数
        HttpURLConnection.setRequestProperty.implementation = function(key, value){
            console.log("--param-- : key=>", key, "value=>",value)
            this.setRequestProperty(key, value)
        }
      
        // Hook getInputStream方法获取响应报文
        HttpURLConnection.getInputStream.implementation = function(){
            var inputStream = this.getInputStream()
            var buffer = BufferedReader.$new(InputStreamReader.$new(inputStream));
            var sb = StringBuilder.$new()
            var line = null;
            while((line = buffer.readLine()) != null){
                sb.append(line);
            }
            var data = sb.toString()
            console.log("--response--: " +data)
            console.log("--Network Stop--")
            return inputStream
        }
    }
    )
}

setImmediate(main)
```




