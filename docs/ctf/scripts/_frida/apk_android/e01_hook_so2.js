function hook() {
  // 1,拿到目标 so 的基址
  // https://frida.re/docs/javascript-api/
  var base = Module.findBaseAddress("libwolf.so")

  console.log("base =", base)

  /*
   * public static native void greywolf(Context context, String str);
   * int __fastcall bc(JNIEnv *a1, int a2, int context, int input_str);  参数3 之后 对应的 native方法参数
  */

  // 由于该 so 是 arm 架构,所以偏移要加1, ida里显示是0x14074
  var bc = base.add(0x14074).add(0x1)

  Interceptor.attach(bc, {
    onEnter: function (args) {
      console.log("enter bc")
      var arg3 = args[3] // jstring
      // https://github.com/frida/frida-java-bridge 如 frida中是getStringUtfChars, 开发中是大写 getStringUTFChars

      console.log("arg3=" + arg3) // hex地址
      var arg3_c = Java.vm.getEnv().getStringUtfChars(arg3)

      console.log("arg3=" + hexdump(arg3_c))
      // https://frida.re/docs/javascript-api/#nativepointer
      console.log("arg3=" + arg3_c.readCString()) // 确定是字符串后可用这个读取
    },
    onLeave: function (retval) {},
  })


  var dc = base.add(0x14508).add(0x1)

  Interceptor.attach(dc, {
    onEnter: function (args) {
      var arg2 = args[2]

      console.log("enter dc arg2=" + arg2.readCString())
    },
    onLeave: function (retval) {
      console.log("leave dc retval = " + retval)
      retval.replace(0x1)
    },
  })

  var Decrypt = base.add(0x13F34).add(0x1)

  Interceptor.attach(Decrypt, {
    onEnter: function (args) {
      var arg0 = args[0]
      var arg1 = args[1]

      console.log("enter Decrypt arg0=" + arg0.reaDecryptString() + "---arg1=" + hexdump(arg1))
    },
    onLeave: function (retval) {
      console.log("leave Decrypt retval = " + hexdump(retval))
      // retval.replace(0x1)
    },
  })

}

setImmediate(hook)
// frida - UF -l hook.js -o out2.log
