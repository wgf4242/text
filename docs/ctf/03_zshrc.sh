#!/bin/zsh
rm $HOME/.oh-my-zsh -rf
rm install.sh
sudo apt-get install -y autojump

wget https://ghproxy.com/https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh
sed -i "s/-https:\/\/github.com/-https:\/\/github.com.cnpmjs.org/g" install.sh
bash install.sh

git clone https://github.com.cnpmjs.org/zsh-users/zsh-autosuggestions $HOME/.oh-my-zsh/custom/plugins/zsh-autosuggestions --depth=1

sed -i "s/^plugins=.*/plugins=\(zsh-autosuggestions\)/g" ~/.zshrc
sudo tee -a ~/.zshrc <<-'EOF'

# xset r rate 220 30 # add to .xsessionrc or .xinitrc file.

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

function c() {
    checksec --debug --file="$1"
}

. /usr/share/autojump/autojump.sh

bindkey -s '\eo'   'cd ..\n'    # 按下ALT+O 就执行 cd .. 命令
bindkey -s '\ep'   'vmdir\n'    # 按下ALT+P go to vmware
bindkey -s '\e;'   'ls -l\n'    # 按下 ALT+; 就执行 ls -l 命令
bindkey -s '\ed'   'cd ~/vmware/dbg/\n./linux_server'    # 按下 ALT+d 执行 debug
bindkey '\e0'    autosuggest-accept

bindkey -s '\ep'   '^[[Hproxychains ^M'    # Alt+p在行首添加proxychains回车
export PATH=$PATH:/home/$USER/.local/bin

function c() {
    checksec --debug --file="$1"
}

# if [ "$TMUX" = "" ]; then tmux; fi

EOF

source ~/.zshrc

tee -a ~/.pwn.conf <<-'EOF'
[context]
terminal = ["tmux", "splitw", "-h"]
EOF

sudo apt install -y tmux
echo "set -g mouse on" > ~/.tmux.conf
