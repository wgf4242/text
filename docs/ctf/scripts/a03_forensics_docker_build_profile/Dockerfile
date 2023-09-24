# Centos+docker不行，用Ubuntu+docker也得切内核才行。无法直接通过docker 构建
# x1 宿主机先换内核 例 sudo apt install -y linux-headers-5.4.0-84-generic linux-image-5.4.0-84-generic
# x2 修改启动项, vi /boot/grub/grub.cfg
# x4 修改VER版本
# x5 docker build . # 得到id
# x6 docker run -it e31206b5e9ab /bin/bash  # 得到container id 2d778c3d376d
# x7 docker cp 2d778c3d376d:/code/volatility/tools/linux/profile.zip ./
# x8 profile.zip 放到 volatility2\volatility\plugins\overlays\linux\ 下面
# x9 python vol.py --info | grep Linux  # 查看是否已经制作了目标系统的profile
# header 下载 https://mirrors.ustc.edu.cn/ubuntu/pool/main/l/linux/
# http://archive.ubuntu.com/ubuntu/pool/main/l/linux/linux-headers-5.4.0-42_5.4.0-42.46_all.deb# 
# http://archive.ubuntu.com/ubuntu/pool/main/l/linux/linux-headers-5.4.0-42-generic_5.4.0-42.46_amd64.deb
# https://mirrors.ustc.edu.cn/ubuntu/pool/main/l/linux-hwe-5.4/
# debian https://debian.sipwise.com/debian-security/pool/main/l/linux/

FROM ubuntu:18.04
ARG VER=5.4.0-42-generic

VOLUME /data

RUN mkdir /code

RUN sed -i s@/archive.ubuntu.com/@/mirrors.ustc.edu.cn/@g /etc/apt/sources.list && \
    sed -i s@/security.ubuntu.com/@/mirrors.ustc.edu.cn/@g /etc/apt/sources.list && \
    apt-get update -y
RUN apt install -y linux-headers-$VER linux-image-$VER dwarfdump build-essential git zip
RUN git clone https://gitee.com/Moxin1044/volatility /code/volatility --depth=1

WORKDIR /code/volatility/tools/linux

RUN sed -i.bak -e "s/\$(shell uname -r)/$VER/g" Makefile
RUN make
# # RUN zip $(lsb_release -i -s)_$(uname -r)_profile.zip module.dwarf /boot/System.map-$(uname -r)
RUN zip $(tail -n 1 /etc/lsb-release | sed "s/.*=//g" | sed "s/\"\| //g")_${VER}_profile.zip module.dwarf /boot/System.map-${VER}

COPY entrypoint.sh /code/volatility/tools/linux/
RUN chmod +x /code/volatility/tools/linux/entrypoint.sh
ENTRYPOINT ["/code/volatility/tools/linux/entrypoint.sh"]