// frida -UF -l .\a.js
// https://frida.re/docs/javascript-api/#nativefunction

function main() {
    Java.perform(function () {
        console.log('start ')
        var aes_addr = Module.findExportByName("libJNIEncrypt.so", "AES_128_ECB_PKCS5Padding_Decrypt");
        console.log(aes_addr)
        var aes_128 = new NativeFunction(aes_addr, 'pointer', ['pointer', 'pointer']);

        var encry_text = Memory.allocUtf8String("9YuQ2dk8CSaCe7DTAmaqAA==");

        var key = Memory.allocUtf8String('thisisatestkey==');

        console.log("The result is: ", Memory.readCString(aes_128(encry_text, key)));
    });
}


setImmediate(main)
