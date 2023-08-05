// frida -UF -l android_e02_readSoPointer2.js -o out2.log
function hook() {
  // 1,拿到目标 so 的基址
  // https://frida.re/docs/javascript-api/

    var securityCheck = undefined
    var exports = Module.enumerateExportsSync("libcrackme.so")
    send(exports)

    for (let i = 0; i < exports.length; i++) {
      if (exports[i].name == "Java_com_yaotong_crackme_MainActivity_securityCheck") {
        securityCheck = exports[i].address
        break
      }
    }

    send("key is:" + Memory.readUtf8String(Memory.readPointer(securityCheck.sub(0x11a8).add(0x628c))))

}

setImmediate(hook);