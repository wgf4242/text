package com.yuanrenxue.match2022.fragment.challenge;

import com.github.unidbg.AndroidEmulator;
import com.github.unidbg.LibraryResolver;
import com.github.unidbg.arm.backend.DynarmicFactory;
import com.github.unidbg.linux.android.AndroidEmulatorBuilder;
import com.github.unidbg.linux.android.AndroidResolver;
import com.github.unidbg.linux.android.dvm.DalvikModule;
import com.github.unidbg.linux.android.dvm.DvmObject;
import com.github.unidbg.linux.android.dvm.StringObject;
import com.github.unidbg.linux.android.dvm.VM;
import com.github.unidbg.linux.android.dvm.jni.ProxyDvmObject;
import com.github.unidbg.memory.Memory;

import java.io.File;

public class ChallengeTwoFragment {

    public static void main(String[] args) {
        long start = System.currentTimeMillis();
        ChallengeTwoFragment mainActivity = new ChallengeTwoFragment();
        System.out.println("load offset=" + (System.currentTimeMillis() - start) + "ms");
        System.out.println("result ---->" + mainActivity.sign("1:16221212"));
    }

    private final AndroidEmulator emulator;
    private final VM vm;

    private ChallengeTwoFragment() {
        emulator = AndroidEmulatorBuilder
                .for64Bit()
                .addBackendFactory(new DynarmicFactory(true))
                .build();
        Memory memory = emulator.getMemory();
        LibraryResolver resolver = new AndroidResolver(23);
        memory.setLibraryResolver(resolver);

        vm = emulator.createDalvikVM(new File("unidbg-android/src/test/java/com/yuanrenxue/match2022/fragment/challenge/yuanrenxuem106.apk")); // 使用apk可过签名校验, 有时需要
        vm.setVerbose(false);
        DalvikModule dm = vm.loadLibrary("match02", true);
        dm.callJNI_OnLoad(emulator);
    }

    public String sign(String str) {
        DvmObject obj = ProxyDvmObject.createObject(vm, this);
        StringObject stringObject = (StringObject) obj.callJniMethodObject(emulator, "sign(Ljava/lang/String;)Ljava/lang/String;",
                vm.addLocalObject(new StringObject(vm, str)));
        return stringObject.getValue();
    }
}

