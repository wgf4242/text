- 2023 年 7 月培训相关视频 - pwn_linux_syscalls.html

先把系统调用号保存到 EAX 寄存器中，然后执行 int \$0x80，然后转入 system\_ call 系统调用指令开始执行

1.将 rax 设置为 3B（59），调用了 execve，execve 函数作用是执行一个新的程序，程序可以是二进制的可执行程序，也可以是 shell、pathon 脚本，这个跟 system 函数差不多

2. ------- 15 的系统号是 rt_sigreturn

3.sys_read 的调用号 为 0 ；sys_write 的调用号 为 1

| 调用号    | value      |     |
| --------- | ---------- | --- |
| sys_read  | 0          |     |
| sys_write | 1          |     |
| sys_call  | int \$0×80 |
| sys_call  | int \$0×80 |

# x64 syscall

| 调用号   | value | rax       | rdi         | rsi | rdx |
| -------- | ----- | --------- | ----------- | --- | --- |
| sys_call | 0F 05 |           |             |     |
| execve   | 0     | 59 (0x3b) | & '/bin/sh' | 0   | 0   |

# SigreturnFrame

https://blog.csdn.net/A951860555/article/details/115205281
