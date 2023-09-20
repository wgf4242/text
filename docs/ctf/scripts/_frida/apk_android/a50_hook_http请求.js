// frida -U -l network_hook.js -f com.target.app

// Android应用程序中的JavaScript代码
Java.perform(function () {
    var HttpURLConnection = Java.use('java.net.HttpURLConnection');
    
    HttpURLConnection.setRequestMethod.implementation = function (method) {
        console.log('Request Method: ' + method);
        return this.setRequestMethod(method);
    };


    HttpURLConnection.connect.implementation = function () {
        console.log('Connecting to URL: ' + this.getURL());
        return this.connect();
    };
});