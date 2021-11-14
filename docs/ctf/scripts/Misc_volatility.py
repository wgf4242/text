# 关键词 tips
# 管理员登录密码 
import os

os.system("volatility -f raw.raw --profile=Win7SP1x64 iehistory > 03iehistory.txt")
os.system("volatility -f raw.raw --profile=Win7SP1x64 cmdscan &> 04cmdscan.txt")
# 管理员登录密码 
os.system("volatility -f raw.raw --profile=Win7SP1x64 mimikatz>password.txt")
os.system("volatility -f raw.raw --profile=Win7SP1x64 cmdline>cmdline.txt")

# vol3
os.system("python3 vol.py -f ../raw.raw windows.pslist > 01pslist.txt")
os.system("python3 vol.py -f ../raw.raw windows.filescan > 02filescan.txt")
# os.system("python3 vol.py -f ../raw.raw windows.dumpfiles --physaddr 0x3e5e94c0")

