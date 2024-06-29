Aa123456!
Aa123456!WGF@
18245922906
https://192.168.100.254

ssh 10.201.1.91 22 用户名:root 密码:PPj8$ZGA
curl -X POST --data '{"action": "exists", "filename": "/var/spool/cron/crontabs/root"}' http://10.201.1.54:56002/api/v1/file/json

sudo apt install cifs-utils_2%3a7.0-2_amd64.deb

# Host

```sh
mkdir -p /mnt/win
sudo mount -t cifs //192.168.1.3/temp /mnt/win -o user=root,username=wgfabc,password=wgf123456,dir_mode=0777,file_mode=0777
cd /mnt/win
tcpdump -nn -s0 -w "test$(date +%F-%H%M%S).pcap"

sshpass -p "kali" scp -r kali@192.168.88.130:~/tmp D:/temp/vmware/nengyuan/temp
scp -r kali@192.168.88.130:~/tmp D:/temp/vmware/nengyuan/temp | echo "kali"
```

## bak

tcpdump -nn -s0 -w test.pcap

scp -r root@10.201.1.91:~/tmp ~/tmp
scp -r kali:kali@192.168.88.130:~/tmp ~/vmware/nengyuan/temp
scp -r kali@192.168.88.130:~/tmp ~/vmware/nengyuan/temp

sshpass -p "kali" scp -r kali@192.168.88.130:~/tmp ~/vmware/nengyuan/temp

## 挂载远程linux
```
sudo apt-get update
sudo apt-get install sshfs
sudo mkdir /mnt/tmp1
sudo chown kali /mnt/tmp1
sshfs kali@192.168.88.129:/home/kali/tmp /mnt/tmp1

# 自动挂载
sudo vi /etc/fstab
username@remote_host:/path/to/remote/directory /path/to/local/mount/point fuse.sshfs defaults,_netdev,password_stdin 0 0
```
