sudo apt install linux-kbuild-5.10
wget https://debian.sipwise.com/debian-security/pool/main/l/linux/linux-headers-5.10.0-21-common_5.10.162-1_all.deb
wget https://debian.sipwise.com/debian-security/pool/main/l/linux/linux-headers-5.10.0-21-amd64_5.10.162-1_amd64.deb
wget https://debian.sipwise.com/debian-security/pool/main/l/linux/linux-image-5.10.0-21-amd64-unsigned_5.10.162-1_amd64.deb
dpkg -i linux-headers-5.10.0-21-common_5.10.162-1_all.deb
dpkg -i linux-headers-5.10.0-21-amd64_5.10.162-1_amd64.deb
dpkg -i linux-image-5.10.0-21-amd64-unsigned_5.10.162-1_amd64.deb

echo "更换一个启动内核"
