"D:\Program Files\Total Commander\TotalCMD64.exe" /O /T /S /R="%~dp0..\awdp_rdg\"
call ping 127.0.0.1 -n 1 -w 0 > nul
"D:\Program Files\Total Commander\TotalCMD64.exe" /O /T /S /R="%~dp0..\binary_pwn_reverse\"
