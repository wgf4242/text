// [挂钩clock_gettime](https://mp.weixin.qq.com/s/ksGjGGeYjvWpgmRA5xyBpg)
const fn_clock_gettime = Module.getExportByName(null, "clock_gettime")
const mod_fancy = Process.getModuleByName("fancy")
 
Interceptor.attach(fn_clock_gettime, {
    onEnter: (params) => {
        this.timespec = params[1];
    }, 
    onLeave: (retval) => {
        console.log(`clock_gettime() tv_sec => ${this.timespec.readU64()}`)
        this.timespec.writeU64(1702565185);
        console.log(`clock_gettime() tv_sec => ${this.timespec.readU64()}`)
 
    }
})
var i = 0
Interceptor.attach(mod_fancy.base.add(0xFA35),function (args) {
    if (i == 0) {
        i++
        let sbox =  this.context.rcx.readByteArray(256);
        var sboxArr = new Uint8Array(sbox);
        console.log(JSON.stringify(sboxArr));
 
    }
})