// frida -U -f owasp.mstg.uncrackable1 --no-pause -l a01_device_spawn.js
Java.perform(function () {
    send("hook start");

    let c = Java.use("sg.vantagepoint.a.c");
    c["a"].implementation = function () {
        console.log('a is called');
        return false;
    };

    c["b"].implementation = function () {
        console.log('b is called');
        return false;
    };

    c["c"].implementation = function () {
        console.log('c is called');
        return false;
    };

    send("hook end");
});