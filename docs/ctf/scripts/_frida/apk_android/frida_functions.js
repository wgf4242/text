// 输出 public char[] G;
// console.log(this.G.value);
// Arrays.toString

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

function hook_onclick() {
    Java.perform(
        function () {
            console.log("[*] Hook begin")
            var mainActivity$1 = Java.use("sg.vantagepoint.uncrackable1.MainActivity$1");
            mainActivity$1.onClick.implementation = function () {
                console.log("[*] Hook mainActivity$1.onClick")
            }
        }
    )
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
    // 输出 public char[] G;
    let MainActivity = Java.use("com.dionysus.ez_android.MainActivity");
    MainActivity["G0"].implementation = function () {
        this.G0();
        let ret1 = this.G;
        console.log(ret1.value);
    }
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

// https://github.com/OWASP/owasp-mastg/raw/master/Crackmes/Android/Level_02/UnCrackable-Level2.apk
function hook_so_function() {
    Interceptor.attach(Module.findExportByName('libfoo.so', 'strncmp'), {
        //  strcpy(input, flag);

        onEnter: function (args) {

            if (Memory.readUtf8String(args[1]).length == 23 && Memory.readUtf8String(args[0]).includes("I want your secret asap")) {
                console.log("*******SECRET********")
                console.log(Memory.readUtf8String(args[1]))
                console.log("*******SECRET********")
            }

        },

        onLeave: function (retval) {

        }
    });
}