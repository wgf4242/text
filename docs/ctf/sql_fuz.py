import requests

import json

url = 'http://e15d0fd0-4e7b-43d8-aaaa-c39e12197b02.challenge.ctf.show:8080/here_1s_your_f1ag.php?query=1{}'
a = open('sql_fuzz.json', 'r', encoding='utf8').read()
b = json.loads(a)
pattern = 'alert'


def available(find_txt, txt):
    return find_txt in txt


c = {}
for k, v in b.items():
    res = requests.get(url.format(v))
    if available(pattern, res.text):
        c[k] = v
print('fuzzed string is')
print(c)