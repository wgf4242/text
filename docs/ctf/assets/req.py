# python req.py -u http://101.230.70.253:24954/?tpl=
from argparse import ArgumentParser

import requests

parser = ArgumentParser(description="dirsearch 平替")
parser.add_argument('-u', '--url', dest='url', default=None, type=str, required=True)
parser.add_argument('-w', '--wordlists', dest='wordlist', default=r'D:\wgf\My Documents\GitHub\blog\text\docs\ctf\assets\db\dicc_file_paths.txt', type=str)
args = parser.parse_args()

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}
proxies = {}
# host = 'http://101.230.70.253:24954/?tpl='
url = args.url
wordlist = args.wordlist

f = open(wordlist, 'r', encoding='utf8')
for param in f.read().splitlines():
    # param = '/../../../../../../app/tpl/main.go'
    target = f"{url}{param}"
    res = requests.get(target, proxies=proxies)
    print(f"[{res.status_code}] - {res.headers['Content-Length'] + 'B':>7}   {param}")
f.close()
