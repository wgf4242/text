"""
适用于单字节比较程序
示例: 2023 第七届 HECTF 信息安全挑战赛 ezre
0. CFF 关闭动态地址
1. 程序patch不要循环输出，要一次输出后 exit

lea     rcx, qword ptr [aC]               ; "%c" , hex: 2563, data或bss上找个地方写就行
mov edx, dword ptr [rsp+rax*4+0x378+Str2]  ; ArgList   ; 这也行 movzx   edx, [rsp+rax+0x108+Inp]
call    vprintf
for ( i = 0; i < 30; ++i )
  vprintf("%c", Str2[i]);

1. 用汇编修改程序输出加密后的Input值
2. 填写
    length,
    comand,
    get_output 调试
"""
import subprocess
import string

target_output = [0x00000032, 0x0000003D, 0x00000028, 0x00000065, 0x00000028, 0x0000001C, 0x0000002E, 0x0000004B, 0x0000005A, 0x00000042, 0x00000031, 0x00000056, 0x00000009, 0x00000027, 0x0000002A, 0x0000006E, 0x00000003, 0x00000026, 0x0000001D, 0x00000049, 0x00000008, 0x00000050, 0x0000005F, 0x00000038, 0x00000049, 0x00000010, 0x0000005A, 0x0000005F, 0x00000009, 0x0000001A]
btarget_output = bytes(target_output)
length = 30
command = ['ezre.exe']
val = 'a' * length

charset = string.ascii_letters + string.digits + string.punctuation
charset = '''flagbcdehijkmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'''


def get_output(out):
    prefix = b'please input your flag'
    out = out.replace(prefix, b'')
    return out[2:]


for i in range(length):
    for c in charset:
        val = list(val)
        val[i] = c
        bval = ''.join(val).encode()
        res = subprocess.check_output(command, input=bval)
        boutput = get_output(res)
        print(f'trying input {bval.decode()}')
        if boutput[i] == btarget_output[i]:
            print(f'success: {c}')
            break
    else:
        raise "Error not found"
