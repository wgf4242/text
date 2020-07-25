[TOC]
# pwn
[pwn解题本](http://note.taqini.space/#/?id=pwn-note-book)

[Tcache Exploitation](https://www.slideshare.net/AngelBoy1/tcache-exploitation-127268389)
[Linux binary Exploitation - Basic knowledge](https://www.slideshare.net/AngelBoy1/linux-binary-exploitation-basic-knowledge)
[Linux Binary Exploitation - Heap Exploitation](https://www.slideshare.net/AngelBoy1/linux-binary-exploitation-heap-exploitation)
## Tools
[shellcodeexec](https://github.com/inquisb/shellcodeexec)

## Pwndbg快速入门实战

gcc test.c -m32
gdb a.out
start
context

GDB 启动方式
gdb file_path
gdb attach pid

  ps -aux 可以找 ./a.out 在 explorer ,看pid
  ps -e | grep bin

添加程序的命令行参数
run <args>
set args <args>

gdb 常用命令
q quit

开始调试 

start /s 启动程序并中断在程序的入口｡如果是源码调试,会停在main函数否则会在程序的入口点｡
run /r 不暂停,直接执行程序｡
continue /c 在程序暂停之后,继续执行程序｡
strip -s 去掉 symbol

跟踪代码

next/n普通调试器的单步步过｡如果是逆向调试,一次执行一条指令｡
step/s单步步入｡如果是逆向调试,则会跟踪call跳转｡
finish普通调试器的跳出操作｡执行到函数返回处｡


break/b target if condition
break用来下普通的断点,一般称之为软断点｡target是要设置断点的位置,源码调试时可以使用代
码的行号｡而逆向调试时使用*加上地址在一个绝对地址上设置断点｡

break后可以加上if和表达式生成条件断点｡在满足expr表达式时中断｡如
*0×08040101==0xfffff等等｡

watch expr
watch可以用来设置条件断点或者是内存断点｡靠表达式(expr)来决定｡通常expr为一个变量或者逆
向调试时候的内存地址｡watch会监视内存的变化,一旦内存变化就会中断程序｡同理,还有一个命令
rwatch只监控内存的读取｡
ib/d num
通过ib命令可以查看目前所有断点以及编号｡然后通过d加上编号可以删除断点｡
b printf
i b 查看断点位置 info
d 1 删除断点1号

查看数据
print/p symbol_name 
P命令用来打印符号信息(寄存器,变量等等)源码调试中很有用,但是在逆向调试中很少用｡
X/FMT ADDRESS
用来显示内存信息｡其中target是内存地址｡也可以是一个类似a+b的表达式｡
FMT用来控制打印形式｡两个字母组成加一个数字组成｡
第一个字母控制打印格式｡有o(八进制),x(十六进制),d(+进制),u(无符号十进制),t(二进制),f(浮点类型),a(地址类型),i(解析成指令并反编译),C(字符)和s(字符串)
第二个字母用来设定输出长度b(byte),h(halfword),w(word),g(giant,8 bytes)｡其后加一个数字表述输出多少信息｡
backtrace
打印函数调用栈｡通过这个命令可以查看程序到底经过怎样的函数调用过程｡

x /wx 地址  --- 显示地址信息 w4节点 x 16进制 b-1个字节 h-8 g-16 , s--按字符串打印
x /10i 地址 --- 打印10条指令


Context
pwndbg的额外添加的函数｡显示pwndbg默认的context信息｡
dps
dps用于显示地址上的指针和符号信息｡通常在显示栈或者是数据结构的时候使用
Dsassemble
用来反汇编函数｡该命令与x/i不同之处是Dsassemble必须在有函数名符号的情况下才能使用,而
且一次反汇编一个函数｡没法指定长度
Dsassemble main

pwndbg 高级功能
vmmap
此命令可以显示程序的内存结构｡通常从/proc/self/maps中读出｡
search
Pwndbg的search搜索功能｡可以支持各种长度的数据以及字符串搜索的功能｡可以在内存中寻找需要的数据｡
  serach -h
  search hello
checksec
checksec是一个安全检查用脚本,在pwndbg中也有集成｡其作用是查看程序是否开启nx,canary等攻击保护｡

defcone Al赛题的第2个题目是一个通过格式化字符串触发的栈溢出漏洞｡这次我们就以这一题作为这次课程的最后考验｡来实际测试一下如何用pwntools来编写利用脚本｡

    import pwn
    pwn.context.log_level = 'debug'

    def compress(data):
        ...

    shellcode = pwn.shellcraft.i386.linux.sh()
    shellcode = pwn.asm(shellcode)

    payload = ''
    payload += '%259c' #填充259的垃圾数据
    payload += pwn.cyclic(40)
    pyaload = compress(payload)

    t = pwn.process('/tmp/bin')

    t.recvuntil('size: ')

    t.sendline(str(len(payload)))

    t.sendline(payload)
    
    raw_input()
    t.interactive()

把 py 运行起来,gdb attach 它｡ ps -e | grep bin 找到PID来Attach
gdb $ c 继续运行｡ 输入值｡｡非法退出了｡看 Invalid address 
0xy61618('haaa') 内存应该是aaah｡ 看之前的cyclic｡把这段haaa替换成别的就行了
pwn.cyclic_find('haaa') 长度是28｡修改py文件 

另开进程

    >>>import pwn
    >>>a =  pwn.LEF('/bin')
    >>>a.search('jmp esp').next()
    >>>pwn.asm('jmp esp')
    '\xff\xe4'
    >>>a.search('\xff\xe4')
    ----generate object ...
    >>>c.next()
    134717254
    >>>hex(134717254)
    '0x8079f46'
    >>>c.next()
    135040543

修改代码 payload部分为 


    payload = ''
    payload += '%259c' #填充259的垃圾数据
    payload += 'a'*28

    payload += pwn.p32(0x8079f46)
    pyaload += shellcode
    pyaload = compress(payload)

python poc.py 就拿到shell

Misc: 跑起来会输出 pid, 这时用 gdb attach pid可以绑定程序｡

## pwntools 快速入门
pwntools中包含很多三方软件包｡包括capstone等二进制软件｡推荐在linux或者
mac os上新开python virtualenv安装｡(pwntools不支持windows或者python3)
安装详细教程:https://docs.pwntools.com/en/stable/install.html

pwntoosl的模块多 wiki地址:https://docs.pwntools.com/en/stable/

1.pwnlib.asm
asm模块主要通过capstone进行汇编的编译与反编译｡通常用来编译各种平台构架的shellcode
2.pwnlib.constants
头文件宏定义的封装,通过此模块,可以直接获取一下系统宏定义对应的整数数据｡
3.pwnlib.context
上下文管理器,通过它来控制一些全局的信息｡比如目标计算机体系结构,log等级等｡控制生
成shellcode,log时候的默认行为｡
4.pwnlib.dynelf
通过内存leak数据来自动化定位程序中函数位置｡极其实用｡
5.pwnlib.encoders
shellcode编码工具｡通过编码排除shellcode中特定字符｡经常无法转换｡

1.pwnlib.elf
读写elf文件结构中的各种信息｡非常方便实用｡
2.pwnlib.fmtstr
格式化字符串自动化利用工具｡有缺陷,只能使用少数情况｡
3.pwnlib.gdb
可以在脚本中直接使用此模块attach进程或者启动gdb｡有缺陷,不实用｡
4.pwnlib.libcdb
Libc的database,可以通过一些信息查找对应libc｡通常配合dynelf使用｡
5.pwnlib.log
通常是pwntools内部代码使用｡偶尔用它打印一些信息｡大部分时候还是会直接print｡

1.pwnlib.memleak
内存泄露管理工具｡方便拼接多次泄露出来的内存｡不过通常只在dynel的时候由后者使用｡
2.pwnlib.shellcraft
shellcode生成工具｡生成shellcode时候非常遍历｡
3.pwnlib.tubes
主要的io工具,pwntools最最常用的功能｡
4.pwnlib.util
包含一些列有效的小工具｡虽然都不是复杂的工具,但是直接使用能节省很多时间｡
5.pwnlib.rop
rop生成工具,可以自动生成32位rop｡

tubes的作用是于被攻击目标进行通信,处理各种io数据并提供统一的API接口｡
    
    import pwn
    t=pwn.remote("127.0.0.1",12345)
    t.sendline("hello")
    t.recvline()
    t.interactive()

process 和 remote 都是tubes的子类｡

    t=pwn.remote("127.8.0.1",12345)

remote返回的为tubes的子类｡此类型主要用于和互联网主机进行交互｡一般只需要有ip和端口即可｡ 其它参数可以保持默认｡

    t=pwn.process("./bin",shell=True)

process和remote的类方法基本相似｡process主要用于启动本地的程序然后进行交互｡用于本地调试
通常情况下,会使用调用process启动本地程序,方便gdb调试｡等到脚本编写完成再改成远程利用

    t.send("hello")
    t.sendline("hello")

二者都是向目标发送数据｡而sendline会在发送数据最后添加一个回车｡慎用sendline,往往因为忽视多出来的一个回车导致利用无法成功

    t.recv(1824)
    t.recvline()
    t.recvuntil('welcome')

三者都是接受数据并将接受的数据返回｡recvline会一直读取直到读出到回车｡recvunit则读到指定
的数据才会停止｡recv稍有不同,它会读取指定长度的数据或者缓冲区无数据可以读取时返回｡
慎用recv,多用recvunitl

    pwn.p32(exdeadbeef)
    pwn.p64(exdeadbeefdeadbeef)
    pwn.u32('1234')
    pwn.u64('12345678')
将字节数组与数组进行以小端对齐的方式相互转化｡32负责转化dword,64负责转化qword

### shelcraft 与 asm
pwntools的shellcraft主要用来生成汇编代码形式的shellcode,而asm的作用是根据
汇编代码编译出二进制shellcode｡
二者最大的特点是对大部分主流cpu构架的支持以及大量的linux下shellcode模板｡

例子1:生成执行sh的shellcode并编译

    asm(pwnlib.shellcraft.thumb.linux.sh(),arch='thumb')
可以将其中的thumb换成i386,mips,arm或者amd64来切换shellcode构架

例子2:读取flag并输出到标准输出

pwnlib.shellcraft.i386.1inux.cat("flag",fd=1)
  
    1是stdout, 标准输出
例子3:使用forkbomb搞坏系统(慎用)

    pwn1ib.she11craft.i386.1inux.forkbomb()
除此之外,还有大量的shellcode模板可以使用｡全部模板可以查阅pwntools文档

### context
context是pwntools的一个上下文管理器｡可以理解成一个包含了很多元素的类｡通过
设置它可以改变pwntools中很多模块的运行行为｡最经常设置的有log _level,arch｡
通过 `pwn.context.log_level="debug"`
可以将log等级调到debug等级｡pwntools会将所有io数据等输出｡非常方便编写poc的时候的调试｡
而arch可以设置攻击目标的指令构架｡会修改asm等与构架相关模块的默认构架｡不用再手动指定｡
pwn.context.arch = 'amd64'

### ELF

ELF模块主要用来读取elf文件中的各种结构数据｡包括plt,got表位置,函数地址等等｡
虽然也可以直接使用ida读取｡但是通过ELF模块自动获取会更加简单｡尤其是针对本地与
远程libc不同的情况｡

defcone A赛题的第3个题目是一个通过菜单交互,执行任意shellcode的题目｡这次我们就以这一题作为这次课程的最后考验｡来实际测试一下如何用pwntools来编写利用脚

技巧确认得到shell前先输出｡再用until

    t.sendline('echo "do I get shell?"")
    t.recvuntil("do I get shel1?\n")
    t.success("get shell")
    t.interactive()

## 常见漏洞

__缓冲区溢出(Buffer Overflow)__

* 堆溢出､栈溢出､bss溢出､data溢出(通常覆盖指针)

wellpwn,AliCTF 2016 vss,Hitcon 2015 readable,stkof,zerostorage

__整数溢出(Integer Overflow)__

* 无符号型与有符号的转换(MMACTF 2016 shadow)

* 整数加减乘除法,如malloc(size-2)(pwnhub.cn calc)
* 整数溢出通常会进一步转换为缓冲区溢出､逻辑漏洞等其他漏洞

__格式化字符串(Format String)__

* printf(s).sprintf(s).fprintf(s)等,可能导致任意地址读写(MMACTF 2016 greeting)

* 可以用来leak(HCTF2016 fheap)

释放后使用(Use-After-Free)
* 释放掉的内存可能会被重新分配,释放后使用会导致重新分配的内存被旧的使用所改写

* Double free是一种特殊的UAF
* Defcon 2014 Qualifier shitsco,AliCTF 2016 router,OCTF2016 freenote(double free),

HCTF2016 fheap(double free)

__逻辑漏洞__

* 访问控制,协议漏洞,多线程竟态条件(fakefuzz等

关键数据结构分析:还原结构体､接口､类等｡
控制流分析:理清楚程序的执行逻辑,基本要做到从反汇编代码到源码的还原｡
数据流分析:理清楚数据的流向｡

__CTF漏洞挖掘中的分析策略:__

* 目标文件较小时,通常采用对整个目标文件进行控制流分析,做到整个程序从反汇编代码到接

近源码级别的还原,还原的同时查找漏洞
* 目标文件较大时,逆向整个文件所需工作量太大,通常需要额外的关注数据流,并理清楚数据

流所经之处的控制流,因为漏洞的触发与数据流离不开关系
* 无论是数据流分析和控制流分析,还原结构体､接口､类都会促进逆向工程

* 控制流分析

控制流分析的主要作用是理清楚程序的逻辑,对于规模较小的目标文件,一般选择理清 整个目标文件｡
代码以识别为主,不要硬逆｡
* 需要熟悉常见的数据结构､算法在目标文件一般“长啥样"

.链表､树､图､堆､各种加密算法等
* 逆向分析是一个经验性的工作,刚开始慢慢来,逆多了自会有所感悟

* 善用标记,标记结构体､标记变量名､标记变量类型
* F5大法好,但是F5不是万能的,当发现F5结果比较诡异时需要在汇编层分析(如mmactf2016

shadow)
* 再次强调,需要熟悉各类漏洞,否则碰到漏洞也不知道是漏洞

目标文件较大,全盘逆向不现实
* 追溯用户输入的走向,重点关注对用户输入数据处理的函数

｡可以在不用逆清楚控制流即可找到漏洞,需要一定的技巧性
plaidCTF 2015 datastore


# 第三章：漏洞利用技术

## 课时1 :栈溢出-这些都是套路

*  Call func->push pc, jmp func.

*  Leave->mov esp, ebp, pop ebp
*  Ret->pop pc

栈上的数据无法被当成指令来执行
* 数据执行保护（NX/DEP）

* 绕过方法：ROP
让攻击者难以找到shellcode地址
* 地址空间布局随机化（ASLR）

* 绕过方法：infoleak、ret2dlresolve、ROP
检测Stack Overflow
* Stack Canary/Cookie

* 绕过方法：infoleak
现在NX+Stack Cananry+ASLR基本是标配

现代栈溢出利用技术基础：ROP
利用signal机制的ROP技术：SROP
没有binary怎么办：BROP
劫持栈指针：stack pivot
利用动态链接绕过ASLR:ret2dl resolve、fake linkmap
利用地址低12bit绕过ASLR:Partial Overwrite
绕过stack canary：改写指针与局部变量、leak canary、overwrite canary
溢出位数不够怎么办：覆盖ebp，Partial Overwrite


__现代栈溢出利用技术基础：ROP__

一种代码复用技术，通过控制栈调用来劫持控制流。
Google 关键字：Ret2libc，ROP

__CTF中ROP常规套路：__

* 第一次触发漏洞，通过ROP泄漏libc的address（如puts_got），计算system地址，然后返回到一

个可以重现触发漏洞的位置（如main），再次触发漏洞，通过ROP调用system（“/bin/sh"）
* 直接execve（"/bin/sh”，["/bin/sh]，NULL），通常在静态链接时比较常用

__习题：__

* Defcon 2015 Qualifier:ROpbaby

* AliCTF 2016：VSs
* PlaidCTF 2013：ropasaurusrex

作业1：根据rOpbaby的writeup重写exploit
作业2：尝试做一下vss和ropasaurusrex


__利用signal机制的ROP技术-SROP__

SROP:Sigreturn Oriented Programming
系统Signal Dispatch之前会将所有寄存器压入栈，然后调用signal handler，signal
handler返回时会将栈的内容还原到寄存器。
如果事先填充栈，然后直接调用signal return，那在返回的时候就可以控制寄存器的值。
用的不是特别多，但是有时候很好用，推荐资料：
* http://angelboy.logdown.com/posts/283221-srop

http://www.2cto.com/article/201512/452080.html
例题
Defcon 2015 Qualifier fuckup（这题比较难）
建议自己写一个demo自己测试

__没有binary怎么办-BROP__

BROP:Blind Return Oriented Programming
目标：在拿不到目标binary的条件下进行ROP
条件：必须先存在一个已知的stack overflow的漏洞，而且攻击者知道如何触发这个漏洞；
服务器进程在crash之后会重新复活，并且复活的进程不会被re-rand
用的不是特别多，但是在CTF中出现过
推荐资料：
* http://ytiu.info/blog/2014/05/31/blind-return-oriented-programming-brop-attack-yil

* http:/ytiu.info/blog/2014/06/01/blind-return-oriented-programming-brop-attack-er/
例题：
HCTF 2016出题人跑路了（pwn50）
作业（选做）：重现一下推荐资料2中实现

__劫持栈指针：stack pivot__

将栈劫持到其他攻击者控制的缓冲区
* 向目标缓冲区填入栈数据（如ROP Chains），然后劫持esp到目标缓冲区。劫持esp的方法有很

多，最常用的就是ROP时利用可以直接改写esp的gadget，如pop esp，ret；
* 是一种相对常用的利用技术，不仅用于栈溢出，也可以用在其他可以劫持控制流的漏洞。

Stack Piovt的动机
* 溢出字节数有限，无法完成ROP

* 栈地址未知且无法泄漏，但是某些利用技术却要求知道栈地址（ret2 dlresolve）
* 劫持esp到攻击者控制的区域，也就变相的控制了栈中的数据，从而可以使非栈溢出的控制流劫

持攻击也可以做ROP

__Stack Pivot的利用条件：__

* 存在地址已知且内容可控的buffer

* bss段，由于bss段尾端通常具有很大的空余空间（pagesize-usedsize），所以bss段段尾端也
往往是stack pivot的目标，
.堆块，如果堆地址已泄且堆上的数据可被控制，那堆也可以作为stack pivot的目标
* 控制流可劫持

* 存在劫持栈指针的gadgets
* 如pop esp，ret，除此之外还有很多，要具体binary具体分析

__作业：__

* EKOPARTY CTF 2016 fuckzing-exploit-200（基于栈溢出的stack pivot，必做作业）

HACKIM CTF 2015-Exploitation 5（基于堆溢出的stackpivot，选做作业）

__利用动态链接绕过ASLR:ret2dl resolve、fake linkmap__

动态链接的过程就是从函数名到函数地址转换的过程，所以我们可以通过动态链接器来
解析任何函数，且无需任何leak
前置技能：了解动态链接的过程
* http://blog.chinaunix.net/uid-24774106-id-3053007.html

* 《程序员的自我修养》
伪造动态链接的相关数据结构如inkmap、relplt，详见以下内容
* http://rk700.github.io/2015/08/09/return-to-dl-resolve/

* http://angelboy.logdown.com/posts/283218-return-to-dl-resolve
* http://www.inforsec.org/wp/？p=389

__习题：__

* Codegate CTF Finals 2015 yocto（fake relplt）http://o0xmuhe.me/2016/10/25/yocto-writeup/

* HITCON QUALS CTF 2015 readable（fake linkmap）
* Hack.lu's 2015 OREO（htp://wapiflapi.github.io/2014/11/17/hacklu-oreo-with-ret2dl-resolve/）

理论上任何可以stack pivot且FULLRELRO未开的题目都可以利用这种技术，所以可以
试试用这种技术去做一些之前的习题
作业：选择一道题目去完成ret2dlresolve的利用

__利用地址低12bit绕过ASLR:Partial Overwrite__

在PIE开启的情况下，一个32地址的高20bit会被随机化，但是低12bit是不变的。
所以可以通过只改写低12bit来绕过PIE，不仅在栈溢出使用，在各种利用都经常使用。
Example：
Return address=0x？？？？？abc
System（"/bin/sh"）=0x？？？？def
Overwrite abc by def，we can prompt a shell
作业：了解Partial Overwrite
http:/lyOn.me/2015/07/30/bypass-aslr-with-partial-eip-overwritel
习题：
HCTF 2016 heap（基于堆溢出的parital overwrite）


__绕过stack canary__

至此所讲的所有套路，一旦遇到Stack Canary均无法使用！！
绕过思路：
* 不覆盖Stack Canary，只覆盖Stack Canary前的局部变量、指针。

* 已经几乎不可行，因为编译器会根据占用内存大小从小到大排列变量
* 但是在某些情况下依然可用，如右图可以覆盖fmtstr buf2.

* Leak Canary
.可以通过printf世漏，Canary一般从00开始
* Overwrite Canary

* Canary在TLS，TLS地址被随机化

__溢出位数不够怎么办：覆盖ebp，Partial Overwrite__

Func1：
Call func2
leave（mov esp ebp，pop ebp）
ret（pop ip）
Func 2：
Stack overflow
leave（mov esp ebp，pop ebp）
ret（pop ip）
可以覆盖Func2的ebp，会影响到Func1的esp，进而影响func1的IP
可以部分覆盖返回地址
习题：
XMAN 2016广外女生-pwn
Codegate CTF Finals 2015，chess



## 堆溢出-玩转堆中的各种数据结构
CTF题中堆管理机制：大多数是ptmalloc/dlmalloc，少数题中自己实现
ptmalloc/dlmalloc是glibc的默认内存管理机制，了解它对PWN堆题来说至关重要！
强烈推荐：glibc内存管理ptmalloc源代码分析.pdf 建议先通读，再用作工具书
作业：精读“glibc内存管理ptmalloc源代码分析，pdf”的1-27页，粗读28-130页（end）
arena, bin, chunk. Know it and pwn it!


堆漏洞的利用技术与技巧
Use After Free & Double Free
Heap Overflow
* Overflow directly

* Fast bin attack
* Unsorted bin attack

* Overwrite Topchunk
* Classical&Modern Unlink Attack

* Off by one &Off by null
* Other techniques

General exploit techniques
* Heap fengshui

* Heap spray
* Exploit mmap chunk

Use After Free&Double Free Double Free:UAF中的use为再次free，是一种特殊的UAF，且可转换为普通的UAF转换：free（p），p2=malloc（），p2与p指向同一个内存free（p），p2为Dangling pointer=>UAF习题：
* UAF:DEFCON CTF Qualifier 2014：shitsco、BCTF 2016：router、HCTF2016 5-days（较难）

* Double Free:OCTF2016：freenote、HCTF2016 fheap、HCTF2016 5-days（较难）作业：完成习题shitsco（writeup很多）参考阅读：
* https://blog.skullsecurity.org/2014/defcon-quals-writeup-for-shitsco-use-after-free-vuln

* htp://www.tuicool.com/articles/yquU732
* http://blog.csdn.net/sdulibh/article/details/47375969



Heap Overflow-Overflow Directly
直接覆盖相邻堆块的内存的内容。
关键：如何让想被覆盖的堆块正好在具有溢出漏洞的堆块之后。
* 堆风水/堆排布：通过操纵内存的分配与释放，来控制堆块装内存中的相对位置。

* 堆排布几乎是所有堆漏洞利用所必需的技能，需要对glibc内存管理策略非常熟悉。知道什么时
候分析什么内存。再次强调：一定要阅读且经常翻阅“glibc内存管理ptmalloc源代码分析.pdf”
！！！
例题：XMAN2016 fengshui（zijinghua pwn），SSC安全大会百度展厅heapcanary
作业：完成heapcananry
其实真实环境中大多数漏洞都是通过这种方式进行利用的。但是CTF中不算特别常见。
（因为太简单了）

Heap Overflow-Fast bin attack改写fastbin单向链表中的fd，那再次分配就会分配到被改写的d指向的地址改写目标必须有一个正确的size对应，否则会挂
CTF中的套路：如果bss上有指针，通常会改到bss的指针附近，再次分配可以分配到bss地址，修改新分配的内容便可以修改bss上的指针。
另外还有：House of Spirit例题：
alictf 2016fb（作业，推荐完成）alictf 2016 starcraft Octf 2016 zerostorage（比较难）推荐阅读：
另外还有：House of Spirit
例题：
alictf 2016fb（作业，推荐完成）
alictf 2016 starcraft
Octf 2016 zerostorage（比较难）
推荐阅读：
* http://www.freebuf.com/news/88660.html

* http:/angelboy.logdown.com/posts/291983-heap-exploitation

__Heap Overflow-unsorted bin attack__

利用思路：
* 通过堆溢出覆盖victim->bk为要写入的地址-4，再次分配时bck->fd=unsorted_chunks（av）会触

发一个任意地址写。写入的内容是libc中的一个地址。只不过此时unsortbin被破坏，再次分配代
码会崩掉，所以要谨慎考虑写入的地址，通常可以改写global_max_fast，从而导致接下来所有分
配都是在fastbin进行。
* 通过堆溢出覆盖victim->bk为一个size为x的fake chunk，再次分配unsorted_chunks（av）->bk=

bck会改写unsortbin链表头的bk，此时再分配x-4大小的内存即可返回fakechunk。
习题：
* Octf2016 Zerostorage（http://brieflyx.me/2016/ctf-writeups/0ctf-2016-zerostorage/）

* 第一步unsortedbin attack改写global max fast，第二步fastbin attack


当需要分配的内存无法在fastbin或者smallbin找到时，glibc会从unsort bins的链表头的bk
开始遍历，遍历过程中会把unsortbin中的块加入合适的smalbin/largebin中，如果找到合适
大小内存块则会返回。
bck=victim->bk；
unsorted_chunks（av）->bk=bck；
bck->fd=unsorted_chunks（av）；

__Heap Overflow-Overwrite Topchunk__

House of Force：
* Bin中没有任何合适的内存时会从Topchunk分配内存：

* Iftopchunk->size>alloc_size）（victim=topchunk；topchunk =topchunk-alloc_size；return
victim；}
* 改写Topchunk的size为一个很大的数，如0xfff，分配alloc_size-4大小的内存。由于alloc_size

可控，所以此时topchunk位置可控，再次分配即可分配到想分配的位置
* 需要预先泄漏topchunk的地址

例题：BCTF 2016bcloud（推荐完成）BCTF 2016ruin（arm结构的程序，选做）
推荐阅读：
* htps://gbmaster.wordpress.com/2015/06/28/x86-exploitation-10 1-house-of-force-iedi-overflowl

* http://angelboy.logdown.com/posts/291983-heap-exploitation


__Heap Overflow-Classical&Modern Unlink Attack__

Unlink：当free（mem）调用时，如果与mem相邻的块是空闲的，则会将其从空闲链表中拿
（unlink）下来并与mem合并。
#define unlink（P，BK，FD）{
BK=P->bk；
FD=P->fd：
FD->bk=BK；
BK->fd=FD；
Classical Unlink Attack：
如果通过heapoverflow将P->bk以及P->fd覆盖为攻击者可控制的地址，那FD->bk=BK；BK->fd=
FD；=>P->fd->bk=P->bk；P->bk->fd=p->fd；造成任意写。不过要求（要写的内容+4）or（要写的内容+8）
必须可写，否则会崩。
已不可用，现代glibc已有此检查：P->fd->bk==P&&P->bk->fd==P

Heap Overflow-Classical&.Modern Unlink Attack
Modern Unlink Attack：
* 找一个Pointer X，“X=P，Overflow P->bk=X-4；P->fd=X-8

* P->bk->fd==X-4->fd ==P，P->fd->bk==X-8->bk==P
* Unlink可得到‘P=X，此时可通过P修改X，如果X是数据指针则可能造成任意地址读写。

例题：
* Hitcon 2014 qualifier stkof （Modern Unlink Attack）（作业推荐完成）

* MMA CTF 2016Dairy （Off by one+Classic Unlink Attack +sandbox bypass）
* PlaidCTF 2014200 ezhp（Classic Unlink Attack）（作业推荐完成）

推荐阅读：
* https://gbmaster.wordpress.com/2014/08/11/×86-exploitation-101-heap-overflows-unlink-me-would-you-

please/
* http:/lacez.re/ctf-writeup-hitcon-ctf-2014-stkof-or-modern-heap-overflowl

__Off by one & Off by null__

off by one：溢出位数为1的溢出漏洞
off by null：溢出位数为1且溢出内容为nul的溢出漏洞
在glibc中，如果攻击者可以控制malloc的大小和malloc与free的时机，堆中的Off by one
和Off by nu是可用的，通常可以构造出UAF，进而构造任意地址读写&控制流劫持。
主要利用思路：改写下一个chunk的chunk size（including inuse bit）
作业：阅读论文Glibc_Adventures-The_Forgotten_Chunks.pdf
习题：
* Off By one:MMA CTF 2016 Dairy （Off by one+Classic Unlink Attack +sandbox bypass）

* Off By nullplaid CTF 2015 datastore，XMAN 2016 Final love_letter
其他推荐阅读
* http://angelboy.logdown.com/posts/567673-advanced-heap-exploitation


__General exploit techniques-Heap fengshui__

高级堆排布技术：Heap fengshui
动机：真实漏洞在利用的时候，堆是混乱的，因为存在漏洞的服务可能已经服务过很多
用户，在触发漏洞时无法预计堆已经做了多少次malloc多少次ree。
Heap fengshui可以让堆从混乱状态转换为确定状态
不同的内存管理策略对应的heap fengshui的方法不同，Example：
* For glibc fastbin：把每种可能的大小都分配好多次。

CTF题目一般不需要利用这种技术，因为大多数CTF题目都是程序启动后立刻被攻击者
利用，堆处于确定的状态。
例题：XMAN 2016 fengshui，33c3 CTF babyfengshui
作业：完成以上题目

__General exploit techniques-Heap spray__

Heap spray，堆喷：不断分配内存，并填充（大量0x0c）+shellcode，直到0x0c0c0c0c内存
地址被分配，多用于脚本语言漏洞的利用。
大多数内存地址的值都是0x0c0c0c0c，0x0c0c0c0c地址也是0xOcslide+shellcode可以
用其绕过ASLR，控制流劫持（jmp addr/jmp *addr）时，只要addr是喷过地址都可以执行

shellcode，注意`*addr=0x0c0c0c0c**addr=0x0c0c0c0c***addr=0x0c0c0c`。

必须在NX关闭时才能直接利用heap spray劫持控制流
例题：pwnhub.cn calc
推荐阅读：

* http://www.tuicool.com/articles/3ul

* https://www.corelan.be/index.php/2011/12/31/exploit-writing-tutorial-part-11-heap-spraying-demystified/BJv

## 其他漏洞-内存破坏可不止溢出

### 01格式化字符串

格式化串介绍：https:/len.wikipedia.org/wiki/Printf format string
格式化串相关函数：printf、fprintf、sprint等
格式化漏洞：

* 触发形如printf（fimtstr）的调用，fmtstr="%S22p”时可以打印栈指针之后第22个DWORD，

fmtstr=*%1000c%S22n”时可以将栈指针之后第22个DWORD作为地址写入1000

* https/www.exploit-db.com/docs/28476.pdf

例题

* MMACTF 2016greeting

* HCTF 2016heap（利用格式化串漏洞leak栈中的数据）

* RuCTF 2016 weather

* 作业：完成MMACTF 2016 greeting


### 02竞争条件漏洞

竞争条件漏洞
竞争条件：竞争条件指多个线程或者进程在读写一个共享数据。竞争条件发生时程序最
终的结果依赖于多个进程的指令执行顺序
通过竞争条件，我们可以让程序执行超出预期的行为，如：

* Thread1：free（p1），p1=0；

* Thread2：p2=malloc（），read（p2），p1->calfunc（）

如果Thread1执行完第一条语句，Thread2开始执行并执行至最后一条语句，则会产生Use After Free
进而控制流劫持。
关键：如何控制线程执行的顺序。大名鼎鼎的脏牛就是这类漏洞
例题：
·安恒杯武汉大学邀请赛fackfuzz（多线程竞争条件造成UAF）
·Stupid shell（多进程竞争条件造成越权读文件）


### 03代码逻辑漏洞

代码在实现过程中因逻辑错误所产生的漏洞，如：
    
    if（len>=size）free（ptr）；
    if（len>size）ptr=malloc（en），read（ptr）；
    else read（ptr）

第二个f少了一个等号，从而导致了UAF。
代码逻辑漏洞的表现方式多种多样，没有定式，难以自动化检测
例题：UCTF 2016note代码逻辑漏洞导致的控制流劫持

### 04类型混淆漏洞

将类型A的对象当作类型B的对象进行引用与操作

* 显式类型转换导致的类型混淆：static_cast 子类转父类

static_cast在编译时C++编译器会检查转换前的类型和转换后的类型是否兼容，编译器只允许derived class
转换为base class或base class转换为derived class。前者称为upcast，后者称为downcast。由于derived
class的内存布局通常包含base class，所以upcast通常会存在安全问题，但是downcast却可能会存在类型
混滴的问题。如说在base class的对象中使个只有derived class存在的成员就会产内存越界访问

* 代码中的逻辑错误或漏洞导致的类型混淆：破坏了类/结构体中的表示类型数据（广义）

* 如修改vatable也算一种类型混淆

例题：无，建议看看类型混滴的CVE，如CVE-2015-3077，目前在CTF中没有看到相关题目

### 05缓冲区未初始化

栈未初始化时，栈中数据为上次函数调用留下的栈帧
堆未初始化时，堆中数据为上次使用该堆块所留下的数据
利用举例：

* 若data在栈上且未初始化，代码read（data），puts（data）；可能会造成栈中数据被打印出来

* 若ptr在栈上且未初始化，代码read（ptr）；可能会导致任意写

* 若ptr在堆上且未初始化，i（ptr->datal=null）read（ptr->data）可能导致任意写

例题：
UCTF 2016 note（可以用栈未初始化漏洞做）
华山杯2016决赛SU_PWN（栈未初始化漏洞泄漏栈地址）
33C3 CTF PWN


# WriteUp
## CTF中PWN赛题解析
## 百度杯 pwn2
浮点数在二进制表示方法（内存中显示方法）
## Q
gdb: fini 是什么