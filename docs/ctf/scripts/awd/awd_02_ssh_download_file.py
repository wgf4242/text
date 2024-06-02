import os
import paramiko 
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.50.119', username="kali", password="kali")


localpath = 'abc.txt'
remotepath = '/home/kali/abc.txt'

ftp_client=ssh.open_sftp()
ftp_client.get(remotepath,localpath)
ftp_client.close()
