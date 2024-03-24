# 关键词 tips
# 管理员登录密码 
# 有时用Win2003SP1x86 
export file=../dacong.raw
# export profile=--profile=Win10x64_10240_17770

rm -rf dump-dir mftoutput 2>/dev/null
mkdir screenshots mftoutput 2>/dev/null

python3 vol.py -f $file imageinfo
python3 vol.py -f $file windows.psscan.PsScan > psscan.txt
python3 vol.py -f $file windows.filescan > filescan.txt
python3 vol.py -f $file windows.envars.Envars > 03envars.txt
cat filescan.txt |grep -E ".doc|.zip|.rar|.jpg|.png|.txt|.bmp|.7z|.snt|contact">rarzip_list.txt
python3 vol.py -f $file dumpfiles --virtaddr 0xe0007a54f970
# windows.dumpfiles --physaddr <offset>
python3 vol.py -f $file hivelist > 04_reginfo.txt
python3 vol.py -f $file printkey > printkey.txt
# python3 vol.py -f $file printkey --key "Software\Microsoft\Windows\CurrentVersion"



# vol3
# os.chdir('volatility3')
# python3 vol.py -f ../$file windows.pslist > ../01pslist.txt
# python3 vol.py -f ../$file windows.filescan > ../02filescan.txt
echo '010搜 Rar!\\x1a\\x07\\x01\\x00.{1,100}<文件名>'
echo 尝试手动提取关键文件。
echo 文件过滤: 桌面|Desktop
# python3 vol.py -f ../$file windows.dumpfiles --physaddr 0x3e5e94c0
# python vol.py -f $file --profile=$profile linux_recover_filesystem -D ./filesystem # 恢复系统