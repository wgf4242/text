// 2015阿里移动安全挑战赛第二题AliCrackme_2
// frida -UF -l android_e02_readSoPointer2.js -o out2.log
Java.perform(function () {
    function readSoPointer() {
        var securityCheck = undefined;
        send('aaaaaaa')
        var exports = Module.enumerateExportsSync("libcrackme.so");
        send(exports)

        for (let i = 0; i < exports.length; i++) {
            if (exports[i].name == "Java_com_yaotong_crackme_MainActivity_securityCheck") {
                securityCheck = exports[i].address
                break
            }
        }

        send("key is:" + Memory.readUtf8String(Memory.readPointer(securityCheck.sub(0x11a8).add(0x628c))))
    }

    readSoPointer();
})
