# 修改ssh密码 by txt
# python update_passwd.py root toor toor iplist.txt
import paramiko
import sys
import re

name = sys.argv[1]
passwd = sys.argv[2]
new_passwd = sys.argv[3]
filename = sys.argv[4]

with open(filename, 'r') as f1:
    ip_list = f1.readlines()

def strip_n(s: str):
    return s.strip("\n")


ip_list = list(map(strip_n, ip_list))

com = re.compile("^\d+\.\d+\.\d+.\d+$")

for ip in ip_list:
    if not com.search(ip):
        print(f"ip error {ip}")
        continue
    try:
        ssh = paramiko.SSHClient()  # 创建SSH对象
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 允许连接不在know_hosts文件中的主机
        ssh.connect(hostname=ip, port=22, username=name, password=passwd)  # 连接服务器
        # stdin, stdout, stderr = ssh.exec_command('cat flag.txt')  # 执行命令并获取命令结果
        # print(stdout.read())
        password_change_command = f"echo '{new_passwd}' | passwd --stdin {name}"
        stdin, stdout, stderr = ssh.exec_command(password_change_command)
        recv = stdout.read().decode()
        if "成功" in recv or "Success" in recv:
            print(f"{ip} 更改成功")
        else:
            print(f"{ip} 更改失败")
        ssh.close()
        print('%s yes!' % ip)
    except:
        print('no %s' % ip)
