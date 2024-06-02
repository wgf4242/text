import os
import paramiko

filename = 'Pictures'
remote_path = f'/home/kali/{filename}'
hosts_lst = [
    ['192.168.50.119', 'kali', 'kali', True] # host, user, pass, zipfile
]


def ssh_command(ssh):
    ssh.invoke_shell()

    command = ''
    while command != 'exit':
        command = input("Command:")
        stdin, stdout, stderr = ssh.exec_command(command)
        print(stdout.read().decode('utf8', 'ignore'))


def ssh_connect(host, user, password, tar):
    def get_ip():
        for value in ssh._host_keys.items():
            return value[0]

    def tar_file(remote_path):
        stdin, stdout, stderr = ssh.exec_command(f'tar zvcf {remote_path}.tar.gz {remote_path}')
        print(stdout.read().decode('utf8', 'ignore'))

    def download(localpath, remotepath):
        # localpath = 'abc.txt'
        # remotepath = '/home/kali/abc.txt'

        ftp_client = ssh.open_sftp()
        ftp_client.get(remotepath, localpath)
        ftp_client.close()

    try:
        ssh = paramiko.SSHClient()
        print('Calling paramiko')
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, username=user, password=password)

        # ssh_command(ssh)
        if tar:
            tar_file(remote_path)
            download(f'{filename}_{get_ip()}.tar.gz', f'{remote_path}.tar.gz')
        else:
            download(f'{filename}_{get_ip()}', f'{remote_path}')
    except Exception as e:
        print('Connection Failed')
        print(e)


if __name__ == '__main__':
    for host_obj in hosts_lst:
        host, user, password, tar = host_obj
        ssh_connect(host, user, password, tar)
