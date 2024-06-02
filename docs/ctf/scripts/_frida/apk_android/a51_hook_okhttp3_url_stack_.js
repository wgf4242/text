// frida -U com.richfit.qixin.partybuild.product -l l2.js
// frida -UF -l l3.js

Java.perform(function () {
    var threadef = Java.use('java.lang.Thread')
    var threadinstance = threadef.$new()

    function Where(stack){
        var at = ""
        for(var i = 0; i < stack.length; ++i){
            at += stack[i].toString() + "\n"
        }
        return at
    }

    var URL = Java.use('java.net.URL');
    URL.openConnection.overload().implementation = function () {
        var retval = this.openConnection();
        console.log('URL openConnection' + retval);
        return retval;
    };
    var OkHttpClient = Java.use("okhttp3.OkHttpClient");
    OkHttpClient.newCall.implementation = function (request) {
        var result = this.newCall(request);
        console.log(request.toString());
        var stack = threadinstance.currentThread().getStackTrace();
        console.log("http >>> Full call stack:" + Where(stack));
        return result;
    };

});


