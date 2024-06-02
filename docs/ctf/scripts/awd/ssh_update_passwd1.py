# 修改ssh密码 by range
# python update_passwd.py root toor toor 192.168.1.1-254

import paramiko
import sys

name = sys.argv[1]
passwd = sys.argv[2]
new_passwd = sys.argv[3]
ip_range = sys.argv[4]
ip_range = ip_range.split("-")
ip_range = [ip_range[0].split('.'), ip_range[1]]

ip_c = ip_range[0][0] + "." + ip_range[0][1] + "." + ip_range[0][2]

ip_list = []

for i in range(int(ip_range[0][3]), int(ip_range[1]) + 1):  # [1,254]
    ip_list.append(f"{ip_c}.{i}")


for ip in ip_list:
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
