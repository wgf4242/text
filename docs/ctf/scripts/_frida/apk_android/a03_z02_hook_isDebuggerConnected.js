// frida -U com.xyctf.ezapk -l 6_example.js

Java.perform(function () {
    var c = Java.use('android.os.Debug')

    c.isDebuggerConnected.implementation = function () {
        var res = this.isDebuggerConnected();
        console.log('Hook 前', res)
        res = false;
        console.log('Hook 后', res)
        return false
    }
    c.waitForDebugger.implementation = function () {
        console.log(this.waitForDebugger());
        return false
    }
});
