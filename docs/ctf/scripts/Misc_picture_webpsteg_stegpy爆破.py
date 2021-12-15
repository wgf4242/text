# 参考[VNCTF 2021]HAPPYNEWYEAR，https://github.com/L1near/CTFpics-1/blob/master/webpsteg.py
# 需要一个大的password.txt
# Linux下运行

# -*- coding: utf-8 -*-
import os
from subprocess import Popen,PIPE
import sys
def checkwebp(pic):
    print("IF you don't need a password for the pic please input 1") # 无密钥
    print("IF you know the password of the pic please input 2") # 有密钥且已知
    print("IF not input 3 I will use the password.txt") # 有密钥但未知
    choice = input()
    if choice == '1':
        os.system("stegpy {}".format(pic))
    elif choice == '2':
        print("INPUT THE password:")
        password = input()
        cmd = ["stegpy", "-p",pic]
        subp = Popen([sys.executable, '-c', 'import pty, sys; pty.spawn(sys.argv[1:])', *cmd],stdin=PIPE,stdout=PIPE,stderr=PIPE)
        print(subp.stdout.read(len("Enter password (will not be echoed):")))
        subp.stdin.write(bytes((password+'\n').encode('utf-8')))
        subp.stdin.flush()
        print(subp.stdout.readlines())
        # print(subp.stdout.readlines()[1])
        print('\n')
    elif choice == '3':
        file = open('password.txt', 'r')
        line = file.readline()
        while line:
            print(line)
            cmd = ["stegpy", "-p", pic]
            subp = Popen([sys.executable, '-c', 'import pty, sys; pty.spawn(sys.argv[1:])', *cmd], stdin=PIPE, stdout=PIPE,stderr=PIPE)
            print(subp.stdout.read(len("Enter password (will not be echoed):")))
            subp.stdin.write(bytes((line + '\n').encode('utf-8')))
            subp.stdin.flush()
            print('result:')
            result = subp.stdout.readlines()[1]
            print(result)
            if result != b'Wrong password.\r\n':
                break
            # print(subp.stdout.readlines()[1])
            print('\n')
            line = file.readline()
    else :
        print('Input Wrong!')
if __name__ == "__main__":
    checkwebp('flag.png')