#!/bin/zsh
# alias doc https://kapeli.com/cheat_sheets/Oh-My-Zsh_Git.docset/Contents/Resources/Documents/index
rm $HOME/.oh-my-zsh -rf
rm install.sh
sudo apt-get install -y zsh autojump

wget https://ghproxy.com/https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh --no-check-certificate
sed -i "s/-https:\/\/github.com/-https:\/\/github.com.cnpmjs.org/g" install.sh
# sed -i '' "s/-https:\/\/github.com/-https:\/\/github.com.cnpmjs.org/g" install.sh # macos
bash install.sh

git clone https://ghproxy.com/https://github.com/zsh-users/zsh-autosuggestions $HOME/.oh-my-zsh/custom/plugins/zsh-autosuggestions --depth=1

sed -i "s/^plugins=.*/plugins=\(git zsh-autosuggestions\)/g" ~/.zshrc
sudo tee -a ~/.zshrc <<-'EOF'

alias cls="clear && printf '\e[3J'"

# xset r rate 220 30 # add to .xsessionrc or .xinitrc file.

bindkey  "^[[H"   beginning-of-line
bindkey  "^[[F"   end-of-line
bindkey  "^[[3~"  delete-char
function chpwd() {
    emulate -L zsh
    ls -a
}
function de() {
    rm -rf output
    strings $1 | grep -Ei "(ctf|flag|tip|key|fl0g|secret|ZmxhZw)"
    foremost $1
    zsteg -a $1
    exiftool $1
    binwalk -e $1
    steghide extract -p ""  -sf $1
    stegpy $1
}

function de1() {
    exiftool * | grep flag
    strings *| grep -Ei "(ctf|flag|tip|key|fl0g|secret|ZmxhZw)"
    grep -REai "(ctf|flag|tip|key|fl0g|secret|ZmxhZw)" .
    cat * | grep -Paoh "([\!-z]\x00){2,}\}"
}

function c() {
    checksec --file="$1"
}

. /usr/share/autojump/autojump.sh

bindkey -s '\eo'   'cd ..\n'    # 按下ALT+O 就执行 cd .. 命令
bindkey -s '\ep'   'vmdir\n'    # 按下ALT+P go to vmware
bindkey -s '\e;'   'ls -l\n'    # 按下 ALT+; 就执行 ls -l 命令
# bindkey -s '\ed'   'cd ~/vmware/dbg/\n./linux_server'    # 按下 ALT+d 执行 debug
bindkey '\e0'    autosuggest-accept

bindkey -s '\ep'   '^[[Hproxychains ^M'    # Alt+p在行首添加proxychains回车
export PATH=$PATH:/home/$USER/.local/bin:/usr/local/bin

# if [ "$TMUX" = "" ]; then tmux; fi

EOF

source ~/.zshrc

tee -a ~/.pwn.conf <<-'EOF'
[context]
terminal = ["tmux", "splitw", "-h"]
[update]
interval=never
EOF

sudo apt install -y tmux
echo "set -g mouse on" > ~/.tmux.conf
