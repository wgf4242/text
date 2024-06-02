"""https://mp.weixin.qq.com/s/kxW1GymNM8ECXZyHL4mwXQ
方案一
有些公司，安全部门的人员，会通过编写 so文件，检测frida是否在运行，如果运行，就自动终止app，安全人员写的so，是单独的，不会跟app的业务功能关联，我们可以通过删除这些so文件，实现绕过。
我们在尝试删除操作时，要测试app是否能正常使用，如果能正常使用，说明这个so跟业务无关，如果app不能使用了，说明这个so跟业务有关，我们不能删除。
通过hook安卓底层，依次打印运行app时加载的so文件，一个个打印出so文件，当打印到某个so文件时，如果app退出了，这个so文件，就是在检测frida是否运行

方案二 https://github.com/hzzheyang/strongR-frida-android/releases
"""

import frida
import sys

rdev = frida.get_remote_device()
pid = rdev.spawn(["com.xxxx.xxxx"])
session = rdev.attach(pid)

scr = """
Java.perform(function () {

    var dlopen = Module.findExportByName(null, "dlopen");
    var android_dlopen_ext = Module.findExportByName(null, "android_dlopen_ext");

    Interceptor.attach(dlopen, {
        onEnter: function (args) {
            var path_ptr = args[0];
            var path = ptr(path_ptr).readCString();
            console.log("[dlopen:]", path);
        },
        onLeave: function (retval) {

        }
    });

    Interceptor.attach(android_dlopen_ext, {
        onEnter: function (args) {
            var path_ptr = args[0];
            var path = ptr(path_ptr).readCString();
            console.log("[dlopen_ext:]", path);
        },
        onLeave: function (retval) {

        }
    });
});
"""
script = session.create_script(scr)


def on_message(message, data):
    print(message, data)


script.on("message", on_message)
script.load()
rdev.resume(pid)
sys.stdin.read()