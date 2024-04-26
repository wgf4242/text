# 关键词 tips
# 管理员登录密码 
# 有时用Win2003SP1x86 
export file=../browser.raw
# export profile=--profile=Win10x64_10240_17770

rm -rf dump-dir mftoutput 2>/dev/null
mkdir out screenshots mftoutput 2>/dev/null

python3 vol.py -f $file windows.info.Info
python3 vol.py -f $file windows.psscan.PsScan > psscan.txt
python3 vol.py -f $file windows.filescan > filescan.txt
python3 vol.py -f $file windows.envars.Envars > 03envars.txt
cat filescan.txt |grep -E ".doc|.zip|.rar|.jpg|.png|.txt|.bmp|.7z|.pdf|.snt|contact|.swp|.toml">07rarzip_list.txt
cat filescan.txt |grep -E ".exe">07_file_exe.txt
cat filescan.txt |grep Users | grep -vE "thumbcache|\.raw|.DAT\{|AppData|desktop.ini|thumbcache_.*db|\.url|\.lnk|DumpIt.exe|rwd \\\\|index.dat|\.LOG\d?|Content.IE5|\}.dat" > 07_export_file_out.txt
strings $file | grep -i server > 07_server.txt

python3 vol.py -f $file dumpfiles --virtaddr 0xe0007a54f970
# windows.dumpfiles --physaddr <offset>
python3 vol.py -f $file hivelist > 04_reginfo.txt
python3 vol.py -f $file printkey > printkey.txt
python3 vol.py -f $file windows.netscan.NetScan > NetScan.txt
python3 vol.py -f $file windows.netstat.NetStat > NetStat.txt
# python3 vol.py -f $file printkey --key "Software\Microsoft\Windows\CurrentVersion"



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