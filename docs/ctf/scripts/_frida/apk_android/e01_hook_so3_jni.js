// frida -UF -l e01_hook_so3_jni.js
// frida -U -f com.example.re11113 -l e01_hook_so3_jni.js

function hook() {
  let jni = Java.use("com.example.re11113.jni");

  var res = jni.getiv();
  console.log("iv = :" + res);
  //var key = jni.getkey();
  //console.log("key = :" + key);
  // 尝试直接Hook JNI函数
  var getkeybase = Module.findExportByName("libSecret_entrance.so", "Java_com_example_re11113_jni_getkey");//获取getkey函数地址
  console.log("yes");
  if (getkeybase) {
      Interceptor.attach(getkeybase, {//hook getkey函数
          onEnter: function(args) {//进入函数时调用
              console.log("JNI getkey called");
          },
          onLeave: function(retval) {//离开函数时调用
            if (!retval.isNull()) {//如果返回值不为空/
              try {
                  var result = Memory.readUtf8String(retval);//读取返回值UTF-8字符串
                  console.log("Reconstructed key = " + result);//打印返回值
                  retval.replace(ptr(result));//替换返回值
              } catch (memError) {
                  console.log("Memory read error: " + memError.message);//打印错误信息
              }
            }
          }
      });

      // 调用getkey方法以触发Hook
      var key = jni.getkey();
      console.log("key = :" + key);//打印key
  } else {
      console.log("Failed to find the export 'Java_com_example_re11113_jni_getkey'");//打印错误信息无法找到导出
  }
}

function main() {
  Java.perform(function () {
      hook();
  });
}

setTimeout(main, 200);
