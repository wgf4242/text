file=../mem.vmem
profile=LinuxUbuntu18_04_6LTS_5_4_0-42-generic_profilex64
python vol.py -f $file --profile=$profile linux_banner
python vol.py -f $file --profile=$profile linux_bash >02_bash
python vol.py -f $file --profile=$profile linux_enumerate_files >01files
strings 01files | grep /Documents > 01file_hint1
strings 01files | grep /home/ > 01file_hint2
python vol.py -f $file --profile=$profile linux_pslist >pslist
python vol.py -f $file --profile=$profile linux_pstree  >linux_pstree
python vol.py -f $file --profile=$profile linux_lsof  >linux_lsof
python vol.py -f $file --profile=$profile linux_netstat  >linux_netstat
# 恢复系统 python vol.py -f $file --profile=$profile linux_recover_filesystem -D ./filesystem


node=$(grep '/etc/shadow' 01files | cut -d" " -f 1  )
python vol.py -f $file --profile=$profile linux_find_file -i $node -O shadow
# 过滤 /用户名/  , 分析相关文件
#python vol.py -f $file --profile=$profile linux_find_file -F "/home/bob/Desktop/app.py"
#python vol.py -f $file --profile=$profile linux_find_file -i 0xffff97ce55ca2328 -O app
#python vol.py -f $file --profile=$profile linux_find_file -i 0xffff97ce3448dad0 -O sth