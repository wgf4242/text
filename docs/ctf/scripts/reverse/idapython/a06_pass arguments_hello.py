"""
在控制台会显示 argv 信息
D:\CTF\IDA_Pro_v8.3_Portable\ida64.exe -S"hello.py arg1 arg2 arg3" miaomiaomiao.exe.i64
手动再次显示
Python>idc.ARGV
"""
import idaapi
import idc

print(f"Hello, my name is {idc.ARGV[0]}")
for i in range(1, len(idc.ARGV)):
    print(f"ARGV[{i}] {idc.ARGV[i]}")