sudo apt-get install -y autojump

sed -i "s/^plugins=.*/plugins=\(zsh-autosuggestions\)/g" ~/.zshrc
sudo tee -a ~/.zshrc <<-'EOF'

xset r rate 220 30

bindkey  "^[[H"   beginning-of-line
bindkey  "^[[F"   end-of-line
bindkey  "^[[3~"  delete-char
function chpwd() {
    emulate -L zsh
    ls -a
}
function de() {
    binwalk -e $1
    foremost $1
}

. /usr/share/autojump/autojump.sh

bindkey -s '\eo'   'cd ..\n'    # 按下ALT+O 就执行 cd .. 命令
bindkey -s '\ep'   'vmdir\n'    # 按下ALT+P go to vmware
bindkey -s '\e;'   'ls -l\n'    # 按下 ALT+; 就执行 ls -l 命令
bindkey -s '\ed'   'cd ~/vmware/dbg/\n./linux_server'    # 按下 ALT+d 执行 debug
export PATH=$PATH:/home/$USER/.local/bin

function c() {
    checksec --debug --file="$1"
}
EOF

source ~/.zshrc
