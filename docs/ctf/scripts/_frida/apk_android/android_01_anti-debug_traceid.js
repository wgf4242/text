// CTF 《2015移动安全挑战赛》第二题 AliCrackme_2
// frida -U -f owasp.mstg.uncrackable1 --no-pause -l a01_device_spawn.js
// https://mp.weixin.qq.com/s/X5B3TABoV8nQ1BHHlQHAZg  frida 先执行hook代码后，ida进行附加调试，程序并不退出，反调试点就确定了，Tracepid值检测。
// Q:无法调试
// A: 2. AndroidMinifest.xml文件中添加android:debuggable="true"后进行重编译 或用  mprop 工具修改 ro.debuggable 的值修改为 1(每次重启要执行)
function Tracepid() {
    console.warn(".............")
    var fgetsPtr = Module.findExportByName("libc.so", "fgets");
    var fgets = new NativeFunction(fgetsPtr, 'pointer', ['pointer', 'int', 'pointer']);
    Interceptor.replace(fgetsPtr, new NativeCallback(function (buffer, size, fp) {
        var retval = fgets(buffer, size, fp);
        var bufstr = Memory.readUtf8String(buffer);
        if (bufstr.indexOf("TracerPid:") > -1) {
            Memory.writeUtf8String(buffer, "TracerPid:\t0");
        }
        return retval;
    }, 'pointer', ['pointer', 'int', 'pointer']));
    var killptr = Module.findExportByName("libc.so", "kill");
    var kill = new NativeFunction(fgetsPtr, 'int', ['int', 'int']);
    Interceptor.replace(killptr, new NativeCallback(function (pid,sig) {
        console.log("kill")
        return 0;
    }, 'int', ['int', 'int']));
}


/*
https://blog.csdn.net/MarketAndTechnology/article/details/82111729
mprop 工具：https://github.com/wpvsyou/mprop，具体操作步骤如下：
  adb push mprop /data/local/tmp # 将下载好的 mprop 工具放入 /data/local/tmp 当中
  adb shell
  su
  cat default.prop | grep debug # 查看default.prop里面的配置值，此处是 0
  getprop ro.debuggable         # 获取ro.debuggable 此处应该是 0
  cd /data/local/tmp
  chmod 777 mprop               # 修改权限
  ./mprop ro.debuggable 1       # 修改 ro.debuggable 1 的值为 1
  cat default.prop | grep debug # 查看default.prop里面的配置值，此处是应该还是 0
  getprop ro.debuggable         # 获取 ro.debuggable 此处应该是 1	
  adb shell getprop | findstr debuggable # 检查参数
  stop;start
*/