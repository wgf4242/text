## 准备工作

```sh
adb push frida-server /data/local/tmp/
adb shell
su
cd /data/local/tmp/
chmod 777 ./frida-server
setprop persist.device_config.runtime_native.usap_pool_enabled false
./frida-server
```
