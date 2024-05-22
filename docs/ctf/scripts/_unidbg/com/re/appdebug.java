// https://www.bilibili.com/video/BV1qm421K7HN/
// re11113  apk及so文件放在  apks/CTF_re/app-debug.apk
package re;

import com.github.unidbg.AndroidEmulator;
import com.github.unidbg.Module;
import com.github.unidbg.linux.android.AndroidEmulatorBuilder;
import com.github.unidbg.linux.android.AndroidResolver;
import com.github.unidbg.linux.android.dvm.*;
import com.github.unidbg.memory.Memory;

import java.io.File;

public class appdebug extends AbstractJni {
    public static AndroidEmulator emulator;
    public static Memory memory;
    public static VM vm;
    public static DalvikModule dm;
    public static Module module;


    public appdebug() {
        // 1.创建设备(32位或64位模拟器), 具体看so文件在哪个目录, 在armeabi-v7a就选择32位
        emulator = AndroidEmulatorBuilder.for64Bit().setProcessName("com.example.re11113").build();

        // 2.获取内存对象（可以操作内存）
        memory = emulator.getMemory();

        // 3.设置安卓sdk版本（只支持19、23）
        memory.setLibraryResolver(new AndroidResolver(23));

        // 创建虚拟机（运行安卓代码需要虚拟机）
        vm = emulator.createDalvikVM(new File("apks/CTF_re/app-debug.apk"));
        vm.setJni(this);

        // vm.setVerbose(true);// 打印日志

        // 5. 加载so
        dm = vm.loadLibrary(new File("apks/CTF_re/libSecret_entrance.so"), false);
        dm.callJNI_OnLoad(emulator);

        // 6. dm代表so文件, dm.getModule()得到 module对象, 基于module对象可以访问so中的成员
        module = dm.getModule();
    }

    public String getKey() {
        DvmClass KeyInfo = vm.resolveClass("com/example/re11113/jni");
        // 2. 方法的符号表示
        String method = "getkey()Ljava/lang/String";

        StringObject result = KeyInfo.callStaticJniMethodObject(
                emulator,
                method
        );
        String keyString = result.getValue();
        return keyString;
    }

    public String getIV() {
        DvmClass KeyInfo = vm.resolveClass("com/example/re11113/jni");
        // 2. 方法的符号表示
        String method = "getiv()Ljava/lang/String";

        StringObject result = KeyInfo.callStaticJniMethodObject(
                emulator,
                method
        );
        String ivString = result.getValue();
        return ivString;
    }

    public static void main(String[] args) {
        appdebug obj = new appdebug();
        String key = obj.getKey();
        System.out.println("key: " + key);
        String iv = obj.getIV();
        System.out.println("iv: " + iv);
    }
}



