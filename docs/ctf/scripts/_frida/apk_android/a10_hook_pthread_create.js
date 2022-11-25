// frida -U -f  owasp.mstg.uncrackable1 --no-pause -l uncrackable1.js
// frida -U -f  com.oneplus.note --no-pause -l del1.js

function hook_pthread_create() {
  var pthread_create_addr = Module.findExportByName("libc.so", "pthread_create")
  console.log("pthread_create_addr => ", pthread_create_addr)

  Interceptor.attach("pthread_create_addr", {
    onEnter: function (args) {
      var func_addr = args[2]
      console.log('CCCryptorCreate called from:\n' +
      Thread.backtrace(this.context, Backtracer.ACCURATE)
      .map(DebugSymbol.fromAddress).join('\n') + '\n');
    },
  })
}

function load_so() {
  var dlopen_addr = Module.findExportByName("libc.so", "dlopen")
  var android_dlopen_ext_addr = Module.findExportByName("libc.so", "android_dlopen_ext")

  // console.log('dlopen_addr => ', dlopen_addr);
  // console.log('android_dlopen_ext_addr => ', android_dlopen_ext_addr);
  Interceptor.attach("dlopen_addr", {
    onEnter: function (args) {
      console.log("dlopen => ", args[0].readCString())
      var soName = args[0].readCString()
      if (soName.indexOf("libc.so") > -1) {
        console.log("Enter libc ...")
        this.flag = true
      }
    },
    onLeave: function (retval) {
      if (this.flag) {
          hook_pthread_create();
      }
    },
  })
  Interceptor.attach("android_dlopen_ext_addr", {
    onEnter: function (args) {
      console.log("android_dlopen_ext => ", args[0].readCString())
    },
    onLeave: function (retval) {},
  })
}


function main() {
  Java.perform(function () {
    console.log('hello ...')
    load_so()
 }) 
}