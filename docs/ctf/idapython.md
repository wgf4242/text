Byte(ea) 将地址解释为Byte
Word(ea)
DWord(ea)
QWord(ea)
GetFloat(ea)
GetDouble(ea)
GetString(ea, length = -1, strtype = ASCSTR_C) 获取字符串
GetCurrentLine() 获取光标所在行反汇编



ScreenEA()
　　获取 IDA 调试窗口中，光标指向代码的地址。通过这个函数，我们就能够从一个已知 的点运行我们的脚本。

GetInputFileMD5()
　　返回 IDA 加载的二进制文件的 MD5 值，通过这个值能够判断一个文件的不同版本是否 有改变。

FirstSeg()
　　访问程序中的第一个段。

NextSeg()
　　访问下一个段，如果没有就返回 BADADDR。

SegByName( string SegmentName )
　　通过段名字返回段基址，举个例子，如果调用.text 作为参数，就会返回程序中代码段的开始位置。

SegEnd( long Address )
　　通过段内的某个地址，获得段尾的地址。

SegStart( long Address )
　　通过段内的某个地址，获得段头的地址。

SegName( long Address )
　　通过段内的某个地址，获得段名。

Segments()
　　返回目标程序中的所有段的开始地址。

Functions( long StartAddress, long EndAddress )
　　返回一个列表，包含了从 StartAddress 到 EndAddress 之间的所有函数。

Chunks( long FunctionAddress )
　　返回一个列表，包含了函数片段。每个列表项都是一个元组（chunk start, chunk end）

LocByName( string FunctionName )
　　通过函数名返回函数的地址。

GetFuncOffset( long Address )
　　通过任意一个地址，然后得到这个地址所属的函数名，以及给定地址和函数的相对位移。 然后把这些信息组成字符串以"名字+位移"的形式返回。

GetFunctionName( long Address )
　　通过一个地址，返回这个地址所属的函数。

CodeRefsTo( long Address, bool Flow )
　　返回一个列表，告诉我们 Address 处代码被什么地方引用了，Flow 告诉 IDAPython 是否要 跟踪这些代码。

CodeRefsFrom( long Address, bool Flow )
　　返回一个列表，告诉我们 Address 地址上的代码引用何处的代码。

DataRefsTo( long Address )
　　返回一个列表，告诉我们 Address 处数据被什么地方引用了。常用于跟踪全局变量。

DataRefsFrom( long Address )
　　返回一个列表，告诉我们 Address 地址上的代码引用何处的数据。

Heads(start=None, end=None)
　　得到两个地址之间所有的元素

GetDisasm(addr)
　　得到addr的反汇编语句

GetMnem(addr)
　　得到addr地址的操作码

BADADDR
　　验证是不是错误地址

GetOpnd(addr，long n)
　　第一个参数是地址，第二个long n是操作数索引。第一个操作数是0和第二个是1。

idaapi.decode_insn(ea)
　　得到当前地址指令的长度

idc.FindFuncEnd(ea)
　　找到当前地址的函数结束地址

Entries()
　　入口点信息

Structs()
　　遍历结构体

StructMembers(sid)
　　遍历结构体成员

DecodePrecedingInstruction(ea) 获取指令结构
DecodePreviousInstruction(ea)
DecodeInstruction(ea)

Strings(object) 获取字符串
GetIdbDir() 获取idb目录
GetRegisterList() 获取寄存器名表
GetInstructionList 获取汇编指令表

atoa(ea) 获取所在段
Jump(ea) 移动光标
Eval(expr) 计算表达式
Exec(command) 执行命令行
MakeCode(ea) 分析代码区
MakeNameEx(ea, name, flags) 重命名地址
MakeArray(ea, nitems) 创建数组
MakeStr(ea, endea) 创建字符串
MakeData(ea, flags, size, tid) 创建数据
MakeByte(ea)
MakeWord(ea)
MakeDWord(ea)
MakeQWord(ea)
MakeOWord(ea)
MakeYWord(ea)
MakeFlot(ea)
MakeDouble(ea)
MakePackReal(ea)
MakeTbyte(ea)
MakeStructEx(ea)
MakeCustomDataEx(ea)

PatchByte(ea, value) 修改程序字节
PatchWord(ea, value)
PatchDword(ea, value)
PatchByte(ea, value)
PatchByte(ea, value)

Byte(ea) 将地址解释为Byte
Word(ea)
DWord(ea)
QWord(ea)
GetFloat(ea)
GetDouble(ea)
GetString(ea, length = -1, strtype = ASCSTR_C) 获取字符串
GetCurrentLine() 获取光标所在行反汇编

ItemSize(ea) 获取指令或数据长度

FindText(ea, flag, y, x, searchstr)查找文本
FindBinary(ea, flag, searchstr, radix=16) 查找16进制

GetEntryPointQty() 获取入口点个数
GetEntryOrdinal(index) 获取入口点地址
GetEntryName(ordinal) 入口名


idc.GetFunctionAttr(ea, attr) //得到当前地址所在函数的数据
(
FUNCATTR_START = 0 # function start address
FUNCATTR_END = 4 # function end address
FUNCATTR_FLAGS = 8 # function flags
FUNCATTR_FRAME = 10 # function frame id
FUNCATTR_FRSIZE = 14 # size of local variables
FUNCATTR_FRREGS = 18 # size of saved registers area
FUNCATTR_ARGSIZE = 20 # number of bytes purged from the stack
FUNCATTR_FPD = 24 # frame pointer delta
FUNCATTR_COLOR = 28 # function color code
FUNCATTR_OWNER = 10 # chunk owner (valid only for tail chunks)
FUNCATTR_REFQTY = 14 # number of chunk parents (valid only for tail chunks)
)


class DbgHook(DBG_Hooks):
# Event handler for when the process starts
def dbg_process_start(self, pid, tid, ea, name, base, size)
return
# Event handler for process exit
def dbg_process_exit(self, pid, tid, ea, code):
return
# Event handler for when a shared library gets loaded def
dbg_library_load(self, pid, tid, ea, name, base, size):
return
# Breakpoint handler
def dbg_bpt(self, tid, ea):
return

这个类包含了我们在创建调试脚本时，会经常用到的几个调试事件处理函数。安装 hook 的方式如下:
debugger = DbgHook()
debugger.hook()
现在运行调试器，hook 会捕捉所有的调试事件，这样就能非常精确的控制 IDA 调试器。 下面的函数在调试的时候非常有用:
AddBpt( long Address )
在指定的地点设置软件断点。
GetBptQty()
返回当前设置的断点数量。
GetRegValue( string Register )
通过寄存器名获得寄存器值。
SetRegValue( long Value, string Register )
 

这个是用IDApytohon编写的查找strcpy函数以及他的参数是否在栈区域