package com.kanxue.test2;

import com.github.unidbg.AndroidEmulator;
import com.github.unidbg.LibraryResolver;
import com.github.unidbg.arm.backend.DynarmicFactory;
import com.github.unidbg.linux.android.AndroidEmulatorBuilder;
import com.github.unidbg.linux.android.AndroidResolver;
import com.github.unidbg.linux.android.dvm.DalvikModule;
import com.github.unidbg.linux.android.dvm.DvmObject;
import com.github.unidbg.linux.android.dvm.VM;
import com.github.unidbg.linux.android.dvm.jni.ProxyDvmObject;
import com.github.unidbg.memory.Memory;

import java.io.File;

/**
 * https://bbs.pediy.com/thread-263345.htm
 * TODO: 1. Java_com_kanxue_test2_MainActivity_jnitest 包名、文件名要和so文件中的一样。
 */
public class MainActivity {

    public static void main(String[] args) {
        long start = System.currentTimeMillis();
        MainActivity mainActivity = new MainActivity();
        System.out.println("load offset=" + (System.currentTimeMillis() - start) + "ms");
        mainActivity.crack();
    }

    private final AndroidEmulator emulator;
    private final VM vm;

    private MainActivity() {
        emulator = AndroidEmulatorBuilder
                .for32Bit() // TODO: 32 64bit
                .addBackendFactory(new DynarmicFactory(true))
                .build();
        Memory memory = emulator.getMemory();
        LibraryResolver resolver = new AndroidResolver(23);
        memory.setLibraryResolver(resolver);

        vm = emulator.createDalvikVM();
        // new File: Copy path from repository root 或直接补全 , 可能要 git init
        // vm = emulator.createDalvikVM(new File("unidbg-android/src/test/resources/example_binaries/xx.apk")); // 使用apk可过签名校验, 有时需要
        vm.setVerbose(false); // vm.setVerbose(true);
        // 方式1 TODO: load so file, init 有时用 true
        DalvikModule dm = vm.loadLibrary(new File("unidbg-android/src/test/resources/example_binaries/armeabi-v7a/libnative-lib.so"), false);
        // 方式2. 文件名为 libmatch02.so // DalvikModule dm = vm.loadLibrary("match02", true); // 去掉 "lib",".so"
        dm.callJNI_OnLoad(emulator);
    }

    private static final char[] LETTERS = {
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    };

    private void crack() {
        DvmObject<?> obj = ProxyDvmObject.createObject(vm, this);
        long start = System.currentTimeMillis();
        for (char a : LETTERS) {
            for (char b : LETTERS) {
                for (char c : LETTERS) {
                    String str = "" + a + b + c;
                    boolean success = obj.callJniMethodBoolean(emulator, "jnitest(Ljava/lang/String;)Z", str);
                    if (success) {
                        System.out.println("Found: " + str + ", off=" + (System.currentTimeMillis() - start) + "ms");
                        return;
                    }
                }
            }
        }
    }
}
