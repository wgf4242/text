/* 【2023春节】解题领红包之四.apk
* jadx 打开 右击 cipher 复制为 frida 片段
* public class C{
    public final String cipher(String str, int i) {
    }
  }
* frida -UF -l a03.js
*/
Java.perform(function() {
  let C = Java.use("com.zj.wuaipojie2023_1.C")
  C["cipher"].overload("java.lang.String", "int").implementation = function(str, i) {
    console.log("cipher is called" + ", " + "str: " + str + ", " + "i: " + i)
    let ret = this.cipher(str, i)
    console.log("cipher ret value is " + ret)
    return ret
  }
})
