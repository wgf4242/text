import os
import paramiko

filename = 'abc.txt'
host_obj = ['192.168.50.119', 'kali', 'kali']


def ssh_command(ssh):
    ssh.invoke_shell()

    command = ''
    while command != 'exit':
        command = input("Command:")
        stdin, stdout, stderr = ssh.exec_command(command)
        print(stdout.read().decode('utf8', 'ignore'))


def ssh_connect(host, user, password):
    try:
        ssh = paramiko.SSHClient()
        print('Calling paramiko')
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, username=user, password=password)

        ssh_command(ssh)
    except Exception as e:
        print('Connection Failed')
        print(e)


if __name__ == '__main__':
    ssh_connect(*host_obj)
