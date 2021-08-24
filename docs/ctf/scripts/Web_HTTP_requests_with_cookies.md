# requests with cookie
```python
import requests
url1 = 'http://www.wechall.net/challenge/training/programming1/index.php?action=request'
cookies={}

cookies_txt = 'WC=12549122-53374-0f885ngX8sc4r2cp'
for x in cookies_txt.split('; '):
	a,b = x.split('=')
	cookies[a] = b

a = requests.get(url1, cookies=cookies)
# # res=requests.get("https://cloud.flyme.cn/browser/index.jsp",cookies=cookies)
txt = a.text
print(txt)

url2 = 'http://www.wechall.net/challenge/training/programming1/index.php?answer={}'.format(txt)
b = requests.get(url2, cookies=cookies)
print(b.text)
```


# post with data , filter exclude

```python
url = 'http://inject2.lab.aqlab.cn:81/Pass-07/index.php'
data ={
	'username': 'admin',
	'password': '123456'
}
exclude = '账号密码错误'

def post(url, data, exclude):
	res = requests.post(url, data=data).text
	if exclude not in res:
		print(res)
```