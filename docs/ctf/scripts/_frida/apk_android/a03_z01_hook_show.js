// frida -U com.example.demo02 -l 6_example.js

function main(){
    // Java.perform() 函数表示将参数中的函数注入到Java运行时
    Java.perform(function(){
        // Java.use() 函数表示从内存中获取指定类(包名.类名)的handle句柄
        var MainActivity = Java.use('com.example.demo02.example')
        // hook show()重载方法
        MainActivity.show.overload().implementation = function(){
            // 在控制台打印"Hook show()" 
            console.log("Hook show()")
            this.show()
        }
      
        // hook show(tag) 重载方法
        MainActivity.show.overload("java.lang.String").implementation = function(tag){
            // 修改APP内存中的值
            var result = this.show("Hook")
            // // 获取 Hook 到方法的返回值并在控制台打印
            var AppTag = this.show(tag)
            console.log("show(tag) retval => ", AppTag)
            // 返回修改后的值(Hook)
            return result
        }
    }
    )
}


// 指定要注入到APP进程的函数
setImmediate(main)

