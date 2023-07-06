sudo mv /usr/bin/pip2 /usr/bin/pip2.bak
sudo ln -sf /home/kali/.local/bin/pip /usr/bin/pip2
pip2 install --upgrade pip
pip2 install pathlib2 pwntools