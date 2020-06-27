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