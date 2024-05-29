// 广东财经大学-信息安全-基于IDA Pro和Frida的微信消息撤回无效实验 [BV1di421U7qD].mp4

// 首先我们需要找到 WeChatWin.dll 映射到内存的根地址
const baseAddr = Module.findBaseAddress("WeChatWin.dll")
console.log('WeChatWin.dll baseAddr: ' + baseAddr)

const revokeMsgFunAddr = resolveAddresss('0x181CDE330')
console.log('revokeMsgFunAddr: ' + revokeMsgFunAddr)

Interceptor.attach(revokeMsgFunAddr, {
    // 一旦进入地址的回调函数
    onEnter(args) {
        console.log(this.context.rdi)
        this.context.rdi = 0x0;
        console.log('test!');
    },
})

// 从虚拟地址转化到实际内存地址
function resolveAddresss(addr) {
    const idaBase = ptr('0x180000000')
    const offset = ptr(addr).sub(idaBase)
    const result = baseAddr.add(offset)
    return result;
}

