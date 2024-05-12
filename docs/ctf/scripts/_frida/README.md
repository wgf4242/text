[frida-snippets](https://github.com/iddoeldor/frida-snippets)
[FRIDA-API 使用篇：Java、Interceptor、NativePointer](https://cloud.tencent.com/developer/article/1758879)

# Documents

## command/load js

```sh
# spawn模式运行 crackme.exe
frida -l tmp.js -f crackme.exe
# attach模式运行 crackme.exe
frida -l tmp.js crackme.exe
```

## Basic

```
# 进入App
frida -UF
```

## functions

```
// a02_breakpoint_addr.js
const addr = 0x4000100
ptr(addr); // 转成pointer 可以 hook 寄存器值
```

## Int

```js
//整数类型，可以使用toInt32()函数将其转换为32位有符号整数。需要确保传入的参数是合法的整数类型
var intValue = toInt32(args[0])
```

## String

```js
args[0].writeUtf8String("mystring")

const buf = Memory.allocUtf8String("mystring")
this.buf = buf

args[0].readUtf8String(4).includes("MZ")

// readCString()方法是从给定的内存地址开始读取 并以空字符（'\0'）结尾的C字符串，例如"Hello, World!\0"
Memory.readCString(strArgPtr)

// 二进制数据
var bufferData = Memory.readByteArray(bufferAddr, bufferLength)
var textDecoder = new TextDecoder("utf-8")
var bufferString = textDecoder.decode(bufferData)

// hexdump() 以十六进制输出
var data = Memory.readByteArray(ptr(address), length)
console.log(
  hexdump(data, {
    offset: 0, // offset：指定要打印的数据的起始位置在缓冲区中的偏移量，默认为0。
    length: length, // length：指定要打印的数据的长度，默认为整个缓冲区的长度。
    prefix: "[+] ", // ansi：指定是否在控制台中使用ANSI转义序列来改变打印输出的颜色，默认为true。
    indent: 4, // prefix：指定每一行的前缀，默认为空字符串。
    width: 32, // indent：指定每一行的缩进量，默认为0。
    uppercase: false, // uppercase：指定是否将十六进制数字显示为大写字母，默认为true。
    ansi: true // width：指定每一行显示的字节数，默认为16。
  })
)
```

### Java/String

https://www.cnblogs.com/hetianlab/p/17545726.html

- 爆破 1

```js
function main() {
  Java.perform(function x() {
    console.log("In Java perform")
    var verify = Java.use("org.teamsik.ahe17.qualification.Verifier")
    var stringClass = Java.use("java.lang.String")
    var p = stringClass.$new("09042ec2c2c08c4cbece042681caf1d13984f24a")

    for (var i = 999; i < 10000; i++) {
      var v = stringClass.$new(String(i))
      var vSign = verify.encodePassword(v)
      if (parseInt(p) == parseInt(stringClass.$new(vSign))) {
        console.log("yes: " + v)
        break
      }
      console.log("not :" + v)
    }
  })
}
setImmediate(main)
```

- 爆破 2

```js
function main() {
  Java.perform(function x() {
    console.log("[+] script load")

    var b = Java.use("com.a.easyjava.b")
    var a = Java.use("com.a.easyjava.a")
    var IntClass = Java.use("java.lang.Integer")
    var StringClass = Java.use("java.lang.String")
    var ArrayList = Java.use("java.util.ArrayList")
    var MainActivity = Java.use("com.a.easyjava.MainActivity")

    var flag = new Array()
    var cipher = "wigwrkaugala"

    var bvar = b.$new(IntClass.$new(2))
    var avar = a.$new(IntClass.$new(3))

    for (var _ = 0; _ < cipher.length; _++) {
      for (var i = 97; i < 123; i++) {
        // 97 - 123是字母a-z
        // reset static value
        bvar._b.value = StringClass.$new("abcdefghijklmnopqrstuvwxyz")
        bvar.d.value = IntClass.$new(0)
        bvar._a.value = ArrayList.$new()
        bvar["$init"](IntClass.$new(2))

        avar.b.value = StringClass.$new("abcdefghijklmnopqrstuvwxyz")
        avar.d.value = IntClass.$new(0)
        avar._a.value = ArrayList.$new()
        avar["$init"](IntClass.$new(3))

        var s = String.fromCharCode(i)
        flag.push(s)

        for (var e = 0; e < flag.length; e++) {
          var c = MainActivity.a(flag[e].toString(), bvar, avar)
          if (c != cipher[e]) {
            break
          }
        }
        if (c == cipher[flag.length - 1]) {
          console.log(flag)
          break
        }
        flag.length -= 1
      }
    }
    console.log("flag{" + flag.join("") + "}")
    console.log("[+] script end")
  })
}
setImmediate(main)
```
