# abc可执行
import os
import paramiko 
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.50.119', username="kali", password="kali")
sftp = ssh.open_sftp()
localpath = 'abc.txt'
remotepath = '/home/kali/abc.sh'
sftp.put(localpath, remotepath)
sftp.close()
ssh.close()
