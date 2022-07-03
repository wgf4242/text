
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


function getSoBaseAddress() {
    let base = Module.findBaseAddress('libcreateso.so');
    console.log('base addr', base)
}
function enumberateSoFunction() {
// http://dogewatch.github.io/2017/05/15/Hook-Native-Function-Use-Frida/
// https://github.com/Wyc0/AndroidRevStww/blob/master/note-3/crackme1.apk
    send('start script')
    let securityCheck = undefined;
    const exports = Module.enumerateExportsSync("libcrackme.so");
    for (let i = 0; i < exports.length; i++) {
        if (exports[i].name === "Java_com_yaotong_crackme_MainActivity_securityCheck") {
            securityCheck = exports[i].address;
            send("securityCheck is at " + securityCheck);
            break;
        }
    }
}

function readFromPointer() {
    send('start script')
    let base = Module.findBaseAddress('libcreateso.so');
    let keyAddr = base.add(0x2000);
    console.log('base addr', base)
    console.log('keyAddr addr', keyAddr)
    console.log('-------')
    console.log(keyAddr.readByteArray(16))
    // 00000000  11 00 00 00 65 00 00 00 49 00 00 00 4b 00 00 00  ....e...I...K...
    console.log(keyAddr.readU8()) // 17
    console.log(keyAddr.readCString(16)) // ....e...I...K...
    console.log(keyAddr.readU64()) // '0x6500000011'
    console.log(hexdump(keyAddr)) // '0x6500000011'
}

function writeToMemory() {
    const addr = Memory.alloc(4);
    let numbers = [0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38];
    addr.writeByteArray(numbers)
    console.log(hexdump(addr))
}
