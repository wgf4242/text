function get_pid() {
    Process.enumerateModules({
        onMatch: function (exp) {
            send(exp.name);
        },
        onComplete: function () {
            send("stop");
        }
    })
}

function hook_system_exit() {
    Java.perform(function () {
        var sysexit = Java.use("java.lang.System");
        sysexit.exit.overload("int").implementation = function (var_0) {
            send("java.lang.System.exit(I)V  // We avoid exiting the application  :)");
        };
    });
}


function hook_onStart() {
    var mainactivity = Java.use("sg.vantagepoint.uncrackable1.MainActivity");
    mainactivity.onStart.overload().implementation = function () {
        send("MainActivity.onStart() HIT!!!");
        var ret = this.onStart.overload().call(this);
    };
    //var mainactivity = Java.use("sg.vantagepoint.uncrackable1.MainActivity");
    mainactivity.onCreate.overload("android.os.Bundle").implementation = function (var_0) {
        send("MainActivity.onCreate() HIT!!!");
        var ret = this.onCreate.overload("android.os.Bundle").call(this, var_0);
    };


    var activity = Java.use("android.app.Activity");
    activity.onCreate.overload("android.os.Bundle").implementation = function (var_0) {
        send("Activity HIT!!!");
        var ret = this.onCreate.overload("android.os.Bundle").call(this, var_0);
    };
}

function arrayIntToString() {
    var ret = this.a.overload("[B", "[B").call(this, var_0, var_1);
    send("Decrypted : " + ret);

    flag = "";
    for (var i = 0; i < ret.length; i++) {
        flag += String.fromCharCode(ret[i]);
    }
    send("Decrypted flag: " + flag);
}