"""
第三届个人赛 re_ez
"""

import subprocess
import time

# a.exe 的路径
exe_path = "a.exe"
# 字符集
#charset = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+','=', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '/', '?', ' ', '\t', '\n']
charset = [' ','"','!','#',]
#已经爆破出的字符列表
correct_inputs = []

#字符输入的错误会导致程序立即退出
while True:
    for char in charset:
        process = subprocess.Popen(exe_path, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        time.sleep(0.1)

        #先输入已知正确的字符
        for c in correct_inputs:
            #写入字符并且发送一个回车字符
            process.stdin.write((c + '\n').encode())
            process.stdin.flush()
            time.sleep(0.1)
            #检查程序是否已经退出
            if process.poll() is not None:
                break

        #如果程序退出，就跳到下一个字符
        if process.poll() is not None:
            continue

        #尝试新的字符
        process.stdin.write((char + '\n').encode())
        process.stdin.flush()
        time.sleep(0.1)

        #检查程序是否退出
        if process.poll() is None:
            correct_inputs.append(char)
            print("新的正确字符: ", char)
            break
        #else:
            #print("尝试失败的字符: ", char)
            
    #if "good" in process.stdout.read().decode()  :
       # break

#最后打印出爆破的结果
print('爆破的正确序列是：')
for char in correct_inputs:
    print(char)