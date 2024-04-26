# 关键词 tips
# 管理员登录密码 
# 有时用Win2003SP1x86 
export file=mem.raw

rm -rf dump-dir mftoutput 2>/dev/null
mkdir out screenshots mftoutput 2>/dev/null

vol.py -f $file imageinfo
vol.py -f $file --profile=Win7SP1x64   envars   > 03envars.txt
vol.py -f $file --profile=Win7SP1x64   iehistory> 03iehistory.txt
vol.py -f $file --profile=Win7SP1x64   cmdscan  > 04cmdscan.txt
# vol.py -f $file --profile=Win7SP1x64 cmdscan &> 04cmdscan.txt
# &>表示 stdout pipe
# 管理员登录密码 
vol.py -f $file --profile=Win7SP1x64 mimikatz > 05password.txt
vol.py -f $file --profile=Win7SP1x64 cmdline  > 06cmdline.txt

vol.py -f $file --profile=Win7SP1x64 screenshot --dump-dir=screenshots/
vol.py -f $file --profile=Win7SP1x64 mftparser -D mftoutput>output.txt
vol.py -f $file --profile=Win7SP1x64 filescan > filescan.txt
cat filescan.txt |grep -E ".doc|.zip|.rar|.jpg|.png|.txt|.bmp|.7z|.pdf|.snt|contact|.swp|.toml">07rarzip_list.txt
cat filescan.txt |grep -E ".exe">07_file_exe.txt
cat filescan.txt |grep Users | grep -vE "thumbcache|\.raw|.DAT\{|AppData|desktop.ini|thumbcache_.*db|\.url|\.lnk|DumpIt.exe|rwd \\\\|index.dat|\.LOG\d?|Content.IE5|\}.dat" > 07_export_file_out.txt

vol.py -f $file --profile=Win7SP1x64 pslist > pslist.txt
cat pslist.txt | grep "mspaint" > 10_mspaint_dmp改成data用gimp看看.txt
vol.py -f $file --profile=Win7SP1x64 clipboard>clipboard
vol.py -f $file --profile=Win7SP1x64 psscan > psscan.txt
vol.py -f $file --profile=Win7SP1x64 printkey -K "SAM\Domains\Account\Users\Names" > username.txt
vol.py -f $file --profile=Win7SP1x64 connscan > connscan.txt
vol.py -f $file --profile=Win7SP1x64 hashdump > hashdump.txt
vol.py -f $file --profile=Win7SP1x64 printkey > printkey.txt
vol.py -f $file --profile=Win7SP1x64 netscan > netscan.txt


# vol.py -f $file --profile=Win7SP1x64 dumpfiles -Q [PID] -D ./
# vol.py -f $file --profile=Win7SP1x64 dumpfiles -Q 0x000000003dceaf20 -D ./
# vol.py -f $file --profile=Win7SP1x64 memdump -p 1992 --dump-dir=./

# vol3
# os.chdir('volatility3')
# python3 vol.py -f ../$file windows.pslist > ../01pslist.txt
# python3 vol.py -f ../$file windows.filescan > ../02filescan.txt
nohup cat 07_export_file_out.txt | awk '{print $1}' | xargs -I{} vol.py -f $file --profile=Win7SP1x64 dumpfiles -Q {} -D ./out/ > /dev/null 2>&1 &
strings $file | grep -i server > 07_server.txt

echo '010搜 Rar!\\x1a\\x07\\x01\\x00.{1,100}<文件名>'
echo 尝试手动提取关键文件
echo 尝试手动提取关键文件 raw文件搜flag。
echo 尝试手动提取关键文件zip。 50 4b 03 04
echo 文件过滤: 桌面|Desktop

# python3 vol.py -f ../$file windows.dumpfiles --physaddr 0x3e5e94c0
# python vol.py -f $file --profile=$profile linux_recover_filesystem -D ./filesystem # 恢复系统
