// 这个类一定存在于内存中无需延迟注入。

function main(){
    Java.perform(function(){
        var File = Java.use("java.io.File")  // 获取java.io.File
        File.exists.implementation = function(){  // Hook exists方法并获取path值
            var path = this.path.value;  // 获取path值
            var result = this.exists()  // 获取exists()原始值
            // console.log(path)
            if(path == "/system/bin/su" || path == "/system/xbin/su" || path == "/sbin/su" || path == "/vendor/bin/su"){
                result = false  // 将返回值设为false代表未获取root
            }
            return result
        }
    })
}

setImmediate(main)