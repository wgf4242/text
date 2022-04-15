// 用 spawn 启动
console.log('script running')

var baseaddr = Module.getBaseAddress('Newbie_calculations.exe')

// 确定不了加载基地址,所以我们获取模块基地址加上函数偏移得到函数地址
var ptr_func_1000 = baseaddr.add(0x1000) // int *add(int *a, int *b)
var ptr_func_1100 = baseaddr.add(0x1100) // int *mul(int *a, int *b)
var ptr_func_1220 = baseaddr.add(0x1220) // int *sub(int *a, int *b)

// 分配一小块内存
var buf = Memory.alloc(4)
var func_1000 = new NativeFunction(ptr_func_1000, 'pointer', ['pointer', 'int'])

// 主动调用来测试函数功能
buf.writeS32(123)
func_1000(buf, 456)
// 因为返回的就是第一个参数,也就是buf这个指针,所以不创健新的变量来保存返回值了
console.log('func_1000(&123,456) = ', buf.readS32())
