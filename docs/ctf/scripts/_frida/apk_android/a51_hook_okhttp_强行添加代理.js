// frida -U com.r0ysue.okhttp3demo -l ./a51_hook_okhttp_强行添加代理.js
function main(){
    Java.perform(function(){
        // 在内存中获取okhttp3.OkHttpClient$Builder内部句柄
        var Builder = Java.use("okhttp3.OkHttpClient$Builder")
        // 为创建代理对象做准备
        var Proxy = Java.use("java.net.Proxy")
        var TYPE = Java.use("java.net.Proxy$Type")
        var InetSocketAddress = Java.use("java.net.InetSocketAddress")
        var String = Java.use("java.lang.String")
        console.log(Builder)
        // hook okhttp3.OkHttpClient$Builder内部类的build方法代表最终构造OkHttpClient对象
        Builder.build.implementation = function(){
            // 设置代理服务器IP地址
            var ip_str = String.$new("192.168.110.125")
            // 创建代理服务器对象
            var Proxy_IP_PORT = InetSocketAddress.$new(ip_str, 8080)
            // 调用当前对象的proxy强行设置代理
            this.proxy(Proxy.$new(TYPE.HTTP.value, Proxy_IP_PORT))
            console.log("设置代理成功：协议：", TYPE.HTTP.value)
            return this.build()
        }
    })
}

setImmediate(main)