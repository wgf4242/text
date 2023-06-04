# 注意 requests.get 如果使用params传参，会自动添加一层url编码。。。
# 如果php已经urlencode了，手动解码再发，或者不要使用params
import os
from urllib.parse import unquote
import subprocess
from requests_html import HTMLSession

s = HTMLSession()

php_path = r'E:\Program files\php'
os.environ['path'] = php_path + ';' + os.environ['path']
# stdout = os.popen("php exp.php").read()  # 执行并输出命令的执行结果
# urlencoded = stdout.split('\n')[-1]
p = subprocess.Popen("php exp.php", shell=True, stdin=subprocess.PIPE,stdout=subprocess.PIPE)
urlencoded = p.stdout.readlines()[-1]
print(urlencoded)

url = 'http://192.168.61.141/1.php'
proxies = {'http': 'http://127.0.0.1:8080'}
# 方式1
params = {'pks': unquote(urlencoded)}
res = s.get(url, params=params)
# 方式2
# res = s.get(php + '?pks=' + urlencoded)

# post
# data = {
#     "name": 'name',
#     'phone': 'phone',
#     'email': 'email'
# }
# url = url + '?cata=' + urlencoded
# res = s.post(url, data=data)


print(res.text)