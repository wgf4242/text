放到  unidbg-master\unidbg-android 执行


# 调用 Native Function
[使用Unidbg进行安卓逆向实例讲解](https://mp.weixin.qq.com/s/72woqjXnva2yzgKRtSgTOw)

```java
long addFuncAddr = module.findSymbolByName("add").getAddress();

// 设置参数并调用
int a = 2;
int b = 3;
Number result = emulator.getBackend().emulate(addFuncAddr, null, new int[]{a, b});
System.out.println("Result of add: " + result.intValue());
```
# 模拟 JNI 调用

```java
public class JNIExample {
    public static void main(String[] args) {
        AndroidEmulator emulator = AndroidEmulator.builder().setProcessName("com.example.app").build();
        VM vm = emulator.createDalvikVM(new File("path/to/apkfile.apk"));

        // 加载本地库
        Module module = emulator.loadLibrary(new File("path/to/libnative-lib.so"), true);

        // 获取JNIEnv指针
        long jniEnv = vm.getJNIEnv();

        // 模拟JNI调用
        DvmClass nativeClass = vm.resolveClass("com/example/app/NativeMethods");
        nativeClass.callStaticJniMethodInt(emulator, "nativeAdd(II)I", 2, 3);
    }
}
```

## 逆向复杂函数

```java

public class ComplexCalculation {
    public static void main(String[] args) {
        AndroidEmulator emulator = AndroidEmulator.builder().setProcessName("com.example.app").build();
        Module module = emulator.loadLibrary(new File("path/to/libnative-lib.so"));

        // 找到函数地址
        long calcFuncAddr = module.findSymbolByName("complexCalculation").getAddress();

        // 设置参数
        int x = 5;
        int y = 7;

        // 调用函数并分析返回值
        Number result = emulator.getBackend().emulate(calcFuncAddr, null, new int[]{x, y});
        System.out.println("Result of complexCalculation: " + result.intValue());

        // 使用Inspector工具查看寄存器和内存状态
        Inspector.inspect(emulator.getBackend().reg_read_unicorn(ArmConst.UC_ARM_REG_R0), "R0");
    }
}
```