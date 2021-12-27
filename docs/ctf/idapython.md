# IDAPython入门教程
## 一、函数入门 
https://www.cnblogs.com/iBinary/p/14642662.html

### 获取地址

```python
print(hex(idc.here()))          #获取当前地址
print(hex(idc.get_screen_ea())) #另一种获取当前地址的函数
print(hex(ida_ida.inf_get_min_ea())) #获取当前最小地址
print(hex(ida_ida.inf_get_max_ea())) #获取当前最大地址
print(hex(idc.read_selection_start()))#如果你选择了某块地址 那么使用此函数则返回你选择的这块地址的起始地址
print(hex(idc.read_selection_end())) #同上 返回结束地址.

if idaapi.BADADDR == idc.here(): 
    print("BadAddress addr invalid")
else: 
    print("addr is ok")
```
### 1.4 IDAPython中的数值获取

|      旧的函数        |              新的函数              |
| -------------------- | ---------------------------------- |
|     Byte(addr)       |      idc.get_wide_byte(addr)       |
|     Word(addr)       |      idc.get_wide_word(addr)       |
|    Dword(addr)       |      idc.get_wide_dword(addr)      |
|    Qword(addr)       |        idc.get_qword(addr)         |

获取当前机器码

```python
import idc

ea = idc.get_screen_ea()
value = idc.get_wide_byte(ea)
print("当前指令的硬编码为 {}".format(hex(value)));
```
### 1.5 IDAPython中的数值操作.
指令 | 说明
- | -
idc.PatchByte(addr,value)  | 修改addr地址的值为value.每次修改一个字节
idc.PatchWord(addr,value)  | 同上一次修改变为2个字节
idc.PatchDword(addr,value) | 4
idc.PatchQword(addr,value) | 8

这些指令在IDA7.5中统统不使用了. 统统移植到 ida_bytes里面了

下面说一下这些新函数

旧函数 | 新函数
-|-
idc.PatchByte(addr,value)  | ida_bytes.patch_byte(addr,value)
idc.PatchWord(addr,value)  | ida_bytes.patch_word(addr,value)
idc.PatchDword(addr,value) | ida_bytes.patch_Dword(addr,value)
idc.PatchQword(addr,value) | ida_bytes.patch_Qword(addr,value)

```python
ea = idc.get_screen_ea()
value = idc.get_wide_byte(ea)
print("我是没被修改的当前=  {}".format(hex(value)))
ida_bytes.patch_byte(ea,0x90)

value = idc.get_wide_byte(ea)
print("我被修改过了当前我的值为 {} ".format(hex(value)))
```
## 第二讲 段 函数 汇编指令等操作
https://www.cnblogs.com/iBinary/p/14672540.html



### 二丶汇编中的指令操作

我们现在要分别获取 movups , xmmword ptr,xmm0 等类似汇编的操作.



| 指令                            | 使用以及作用                                                 | 高版本替代函数                       |
| ------------------------------- | ------------------------------------------------------------ | ------------------------------------ |
| idc.GetDisasm(addr)             | 获取地址处的汇编语句 如: mov ebp,esp                         | 无替代                               |
| idc.GetDisasmEx(addr,flags)     | 更高级的获取.带有标志. 一般是给一个0 高版本已经被替代        | idc.generate_disasm_line(addr,flags) |
| idc.GetOpnd(addr,index)         | 获取指定地址位置的操作数.参数1是地址.参数2是操作数索引.如  mov ebp,esp ebp是操作数1 esp是操作数2 mov则是汇编指令不是操作数 | idc.print_operand(addr,index)        |
| idc.GetMnem(addr)               | 操作汇编指令 mov ebp,esp 获取mov                             | idc.print_insn_mnem(addr)            |
| idaapi.get_imagebase()          | 获取基地址                                                   |                                      |
| idc.GetOpType(ea,index)         | 获取操作数的类型                                             | idc.get_operand_type(addr,index)     |
| idc.GetOperandValue(addr,index) | 获取指定索引操作数中的值: 如 calll 0x00402004  对应汇编为: FF 15 04 20 40 00 FF15=Call 而操作数的值则为04 20 40 00 (小端) 使用函数之后获取则为地址  00402004 | get_operand_value(addr,index)        |
| idc.NextHead                    | 获取下一行汇编                                               | idc.next_head(ea)                    |
| idc.PrevHead                    | 获取上一行汇编                                               | idc.PrevHead(ea)                     |

```python
import idc
import idaapi
import idautils

ea = idc.here();
print("当前模块基址为: {}".format(hex(idaapi.get_imagebase())))
print("当前的汇编语句为: {}".format(idc.GetDisasm(ea)))
print("当前的汇编指令为: {}".format(idc.print_insn_mnem(ea)))
print("当前的操作数为: {}".format(idc.print_operand(ea,0)))
print("当前的操作数值为: {}".format(idc.get_operand_value(ea,0)))

```

### 三丶IDA中的段操作

对于一个段最直观的介绍就是他的名字 起始地址 结束地址等.

那么介绍一下段操作中的函数吧.

| 指令               | 作用                                                   | 新函数                   |
| ------------------ | ------------------------------------------------------ | ------------------------ |
| idc.SegName(addr)  | 获取段的名字                                           | idc.get_segm_name(addr)  |
| idc.SegStart(addr) | 获取段的开始地址                                       | idc.get_segm_start(addr) |
| idc.SegEnd(addr)   | 获取段的结束地址                                       | idc.get_segm_end(addr)   |
| idautil.Segments() | 返回一个列表记录所有段的地址                           |                          |
| idc.FirstSeg()     | 获取第一个段                                           | idc.get_first_seg(addr)  |
| idc.NextSeg(addr)  | 获取下一个段 参数是当前段的地址 返回的是下一个段的地址 | idc.get_next_seg(addr)   |

上述返回值如果是获取地址的函数 获取不到都会返回 0xFFFFFFF 也就是 BADADDR

利用上述函数则可以遍历一个段输出其内容

脚本如下:

```python
import idc
import idaapi
import idautils

for seg in idautils.Segments():
    segname = idc.get_segm_name(seg)
    segstart = idc.get_segm_start(seg)
    segend   = idc.get_segm_end(seg)
    print("段名 = {} 起始地址= {} 结束地址 = {} ".format(segname,hex(segstart),hex(segend)));
```

> 段名 = .text 起始地址= 0x401000 结束地址 = 0x423000 
> 段名 = .rdata 起始地址= 0x423000 结束地址 = 0x425000 
> 段名 = .data 起始地址= 0x425000 结束地址 = 0x42b000 
> 段名 = .idata 起始地址= 0x42b25c 结束地址 = 0x42b468 



### 四丶IDA中的函数操作

IDA 关于函数也有很多常见功能. 比如可以获取所有函数 函数参数 函数名.函数属性 以及谁调用了函数.

| 老函数                                            | 作用                                                    | 新函数                                                       |
| ------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------ |
| **Functions(startaddr,endaddr)**                  | 获取指定地址之间的所有函数                              | 无                                                           |
| **idc.GetFunctionName(addr)**                     | 获取指定地址的函数名                                    | **idc.get_func_name(addr)**                                  |
| **idc.GetFunctionCmt**                            | 获取函数的注释                                          | **get_func_cmt(ea, repeatable) 1是地址 2是0或1 1是获取重复注释 0是获取常规注释** |
| **idc.SetFunctionCmt**                            | 设置函数注释                                            | **set_func_cmt(ea, cmt, repeatable)**                        |
| **idc.ChooseFunction(title)**                     | 弹出框框要求用户进行选择 参数则是信息                   | **idc.choose_func(title)**                                   |
| **idc.GetFuncOffset(addr)**                       | 返回: addr 距离函数的偏移形式                           | **idc.get_func_off_str(addr)**                               |
| **idc.FindFuncEnd(addr)**                         | 寻找函数结尾,如果函数存在则返回结尾地址,否则返回BADADDR | **idc.find_func_end(addr)**                                  |
| **idc.SetFunctionEnd(addr,newendaddr)**           | 设置函数结尾                                            | **ida_funcs.set_func_end**                                   |
| **ida_funcs.func_setstart(addr,newstartaddr)**    | 设置函数开头                                            | **ida_funcs.set_func_start(addr, newstart)**                 |
| **idc.MakeName(addr, name) 与之同名了还有Ex函数** | 设置地址处的名字                                        | **idc.set_name(ea, name, SN_CHECK) Ex函数也使用set_name**    |
| **idc.PrevFunction**                              | 获取首个函数                                            | **idc.get_prev_func**                                        |
| **idc.NextFunction**                              | 获取下一个函数                                          | **idc.get_next_func**                                        |

下面请看函数使用例子:

脚本:

```python
import idc
import idaapi
import idautils

for seg in idautils.Segments():
    segname = idc.get_segm_name(seg)
    segstart = idc.get_segm_start(seg)
    segend   = idc.get_segm_end(seg)
    print("段名 = {} 起始地址= {} 结束地址 = {} ".format(segname,hex(segstart),hex(segend)));
    if (segname == '.text'):
        for funcaddr in Functions(segstart,segend): 
            funname = idc.get_func_name(funcaddr)
            funend =  idc.find_func_end(funcaddr)
            funnext = idc.get_next_func(funcaddr)
            funnextname = idc.get_func_name(funnext)
            print("当前函数名 = {} 当前结束地址 = {} 下一个函数地址 = {} 下一个函数名= {}  ".format(funname,hex(funend),hex(funnext),funnextname))
            

ea = idc.get_screen_ea()
funnextoffset = idc.get_func_off_str(ea)
print("当前选择地址距离当前函数的偏移为: {} ".format(funnextoffset))
```

## IDAPython实战

首先选择这一块内容 (0x004015D1 - 0X0040166B)

然后进行脚本编写

import idc
import idaapi
import idautils

*获取当前选择的起始地址

StartSeclectAddr = idc.read_selection_start()

*获取当前选择的终止地址

EndSeclectAddr = idc.read_selection_end()

*计算出当前指令长度

SelLen = EndSeclectAddr - StartSeclectAddr;

*从选择地址开始 - 选择地址结束进行遍历. 获取其指令字节. 如果是0x66 则替换成0xFF


```python
for index in range(SelLen):
    curaddr = StartSeclectAddr+index
    tmpValue = idc.get_wide_byte(curaddr)
    if (tmpValue == 0x66):
        ida_bytes.patch_byte(curaddr,0x70)
```

# Untitled

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