# 关键词 tips
# 管理员登录密码 
# 有时用Win2003SP1x86 
import os

os.system("volatility -f raw.raw --profile=Win7SP1x64 iehistory > 03iehistory.txt")
os.system("volatility -f raw.raw --profile=Win7SP1x64 cmdscan > 04cmdscan.txt")
# os.system("volatility -f raw.raw --profile=Win7SP1x64 cmdscan &> 04cmdscan.txt")
# &>表示 stdout pipe
# 管理员登录密码 
os.system("volatility -f raw.raw --profile=Win7SP1x64 mimikatz>password.txt")
os.system("volatility -f raw.raw --profile=Win7SP1x64 cmdline>cmdline.txt")
os.system("""volatility -f raw.raw --profile=Win7SP1x64 filescan|grep -E ".zip|.rar|.jpg|.png|.txt|.bmp|.7z|.snt|contact">rarzip_list.txt""")
os.system("mkdir 123 mftoutput")
os.system("volatility -f raw.raw --profile=Win7SP1x64 screenshot --dump-dir=123/")
os.system("volatility -f raw.raw --profile=Win7SP1x64 mftparser -D mftoutput>output.txt")
# os.system("volatility -f raw.raw --profile=Win7SP1x64 memdump -p 1992 --dump-dir=./")

# vol3
os.system("python3 vol.py -f ../raw.raw windows.pslist > 01pslist.txt")
os.system("python3 vol.py -f ../raw.raw windows.filescan > 02filescan.txt")
# os.system("python3 vol.py -f ../raw.raw windows.dumpfiles --physaddr 0x3e5e94c0")

