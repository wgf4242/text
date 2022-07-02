// api
// https://www.anquanke.com/post/id/195869
// https://www.zhangkunzhi.com/index.php/archives/191/

// 读取const char* 类型的数据需要使用: Memory.readCString

var intClass = Java.use("java.lang.Integer");
var num1 = intClass.$new(1);
var num2 = intClass.$new(2);
var intArray = Java.array("Ljava.lang.Object;", [num1, num2]);


function stringToBytes(str) {
    var javaString = Java.use('java.lang.String');
    var bytes = [];
    bytes = javaString.$new(str).getBytes();
    return bytes;
}

function readPointerValue(ptr_addr) {
    var pointer = ptr(ptr_addr)
    let size = 10;
    console.log(pointer.readByteArray(size))
    // console.log(pointer.readU8())
}

function read(){
    // so 地址 ： soAddr

    // 方法1：（字符串）根据地址直接读
    soAddr.add(0x2c00).readCString();

    // 方法2 hexdump（根据地址显示dump内容）
    hexdump(soAddr.add(0x2c00));

    // 方法3 功能同上，但指定长度
    // 读16个字节 将内存数据，输出可见数据 （必须用console.log才能输出）
    soAddr.add(0x2c00).readByteArray(16);

    // 使用和 navcat 中相同的方法转换成 cstring, 如果是 jstring 需要先转换为 cstring 才能阅读
    Interceptor.attach(nativePointer, {
        onEnter: function(args){
            var env = Java.vm.getEnv();
            var jstring = env.getStringUtfChars(args[2], null).readCString();
        },
        onLeave: function(retval){}
    });
}

function hook(){ // hook so function
    send("Running Script");
    Java.perform(function(){
        MainActivity = Java.use("com.yaotong.crackme.MainActivity");
        // public native boolean securityCheck(String arg1) {}
        MainActivity.securityCheck.implementation = function(v){
            send("securityCheck hooked");
            return true;
        }
    });
}