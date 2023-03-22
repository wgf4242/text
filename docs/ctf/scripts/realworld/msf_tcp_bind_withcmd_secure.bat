net user administrator @@@@@@999999
set ip="192.168.50.0/24"
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server\Wds\rdpwd\Tds\tcp" /v PortNumber /t reg_dword /d 33089 /f
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v PortNumber /t reg_dword /d 33089 /f
::netsh advfirewall firewall add rule name="RDP_33089" dir=in action=allow protocol=TCP localport=33089 

wmic RDTOGGLE WHERE ServerName="%COMPUTERNAME%" call SetAllowTSConnections 0
wmic RDTOGGLE WHERE ServerName="%COMPUTERNAME%" call SetAllowTSConnections 1
netsh advfirewall firewall add rule name="blueteamTCP" dir=in protocol=tcp localport=139,445 action=block
netsh advfirewall firewall add rule name="blueteamUDP" dir=in protocol=udp localport=137,138 action=block
netsh advfirewall firewall add rule name="Allow from %ip%" dir=in action=allow remoteip=%ip%
netsh advfirewall set allprofiles firewallpolicy blockinbound,blockoutbound
::netsh advfirewall firewall add rule name="Block All Other Traffic" dir=in action=block remoteip=any
netsh advfirewall set allprofiles state on
