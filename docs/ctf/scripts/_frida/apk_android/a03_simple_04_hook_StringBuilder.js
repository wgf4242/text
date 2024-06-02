// frida -U com.richfit.qixin.partybuild.product -l l2.js
// frida -UF -l l3.js

Java.perform(function () {
    var strCls = Java.use("java.lang.StringBuilder");
    strCls.toString.implementation = function () {
        var result = this.toString();
        console.log(result.toString());
        return result;
    }

});
