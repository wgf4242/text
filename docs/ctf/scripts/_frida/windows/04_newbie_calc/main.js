var baseaddr = Module.getBaseAddress("Newbie_calculations.exe")

var ptr_func_1000 = baseaddr.add(0x1000) // int *add(int *a, int *b)
var ptr_func_1100 = baseaddr.add(0x1100) // int *mul(int *a, int *b)
var ptr_func_1220 = baseaddr.add(0x1220) // int *sub(int *a, int *b)

Interceptor.replace(ptr_func_1000, new NativeCallback(function (pa, b) {
    var a = pa.readS32()
    pa.writeS32(a + b)
    return pa
}, 'pointer', ['pointer', 'int']))

Interceptor.replace(ptr_func_1100, new NativeCallback(function (pa, b) {
    var a = pa.readS32()
    pa.writeS32(a * b)
    return pa
}, 'pointer', ['pointer', 'int']))

Interceptor.replace(ptr_func_1220, new NativeCallback(function (pa, b) {
    var a = pa.readS32()
    pa.writeS32(a - b)
    return pa
}, 'pointer', ['pointer', 'int']))
