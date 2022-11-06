# Centos+docker不行，用Ubuntu+docker吧
# x 宿主机先换内核, 安装后修改启动项, vi /boot/grub/grub.cfg
# x apt install -y linux-headers-$VER linux-image-$VER 

FROM ubuntu:18.04
ARG VER=5.4.0-74-generic

RUN mkdir /code
COPY run.sh /code/

RUN sed -i s@/archive.ubuntu.com/@/mirrors.ustc.edu.cn/@g /etc/apt/sources.list && \
    sed -i s@/security.ubuntu.com/@/mirrors.ustc.edu.cn/@g /etc/apt/sources.list && \
    apt-get update -y
RUN apt install -y linux-headers-$VER linux-image-$VER dwarfdump build-essential git zip
RUN git clone https://gitee.com/Moxin1044/volatility /code/volatility --depth=1

WORKDIR /code/volatility/tools/linux

RUN sed -i.bak -e "s/\$(shell uname -r)/$VER/g" Makefile
RUN make
# RUN zip $(lsb_release -i -s)_$(uname -r)_profile.zip module.dwarf /boot/System.map-$(uname -r)
RUN zip $(tail -n 1 /etc/lsb-release | sed "s/.*=//g" | sed "s/\"\| //g")_${VER}_profile.zip module.dwarf /boot/System.map-${VER}

RUN chmod +x /code/run.sh
# ENTRYPOINT ["/code/run.sh"]